pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = 'kimberlyops/ecommerce'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Django tests...'
                sh "docker build -t ${IMAGE_NAME}:test ."
                sh "docker run --rm ${IMAGE_NAME}:test python manage.py test store --verbosity=2"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo 'Pushing image to DockerHub...'
                sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging server...'
                sh "docker stop ecommerce-staging || true"
                sh "docker rm ecommerce-staging || true"
                sh '''
                    docker run -d \
                        --name ecommerce-staging \
                        --publish 8001:8000 \
                        --env SECRET_KEY=django-insecure-staging-key \
                        --env DEBUG=False \
                        --env ALLOWED_HOSTS=localhost \
                        ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Approval Gate') {
            steps {
                echo 'Waiting for manual approval to deploy to production...'
                input message: 'Deploy to Production?', ok: 'Yes, Deploy!'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production server...'
                sh "docker stop ecommerce-production || true"
                sh "docker rm ecommerce-production || true"
                sh '''
                    docker run -d \
                        --name ecommerce-production \
                        --publish 8002:8000 \
                        --env SECRET_KEY=django-insecure-production-key \
                        --env DEBUG=False \
                        --env ALLOWED_HOSTS=localhost \
                        ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}
