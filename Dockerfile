# Use official Python 3.13 slim image as base
FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Start the app with gunicorn
CMD ["gunicorn", "ecommerce.wsgi", "--bind", "0.0.0.0:8000"]
