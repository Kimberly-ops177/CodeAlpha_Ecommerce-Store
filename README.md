# E-Commerce Store

A full-stack e-commerce web application built with Django (Python) backend and vanilla HTML/CSS/JavaScript frontend.

## Features

### Core Functionality
- **Product Listings**: Browse available products with details like name, description, price, and stock
- **Product Details Page**: View detailed information about each product
- **Shopping Cart**: Add products to cart, update quantities, and remove items
- **User Registration/Login**: Secure user authentication system
- **Order Processing**: Complete checkout process with shipping information
- **Order History**: View past orders and their status

### Technical Stack
- **Backend**: Django 5.0.1 (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Authentication**: Django built-in authentication system

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations** (Already done, but if needed)
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Admin User**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

4. **Load Sample Data** (Already loaded)
   ```bash
   python manage.py add_sample_data
   ```

5. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   - Main Site: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
E-Commerce System/
├── ecommerce/              # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
├── store/                 # Main application
│   ├── models.py          # Database models (Product, Order, Cart, etc.)
│   ├── views.py           # View functions and business logic
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Admin panel configuration
│   └── management/        # Custom management commands
│       └── commands/
│           └── add_sample_data.py
├── templates/             # HTML templates
│   ├── base.html          # Base template with navigation
│   └── store/             # Store-specific templates
│       ├── home.html
│       ├── product_detail.html
│       ├── cart.html
│       ├── checkout.html
│       ├── orders.html
│       ├── order_detail.html
│       ├── login.html
│       └── register.html
├── static/                # Static files
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   └── js/
│       └── main.js        # JavaScript functionality
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Database Models

### Product
- name: Product name
- description: Product description
- price: Product price (decimal)
- stock: Available stock quantity
- image_url: Product image URL
- created_at/updated_at: Timestamps

### Order
- user: Foreign key to User
- total_amount: Order total (decimal)
- status: Order status (pending, processing, shipped, delivered, cancelled)
- shipping_address: Delivery address
- created_at/updated_at: Timestamps

### Cart
- user: One-to-one relationship with User
- items: Related CartItems

### OrderItem & CartItem
- Link products to orders/carts with quantity and price

## Usage Guide

### For Customers

1. **Browse Products**: Visit the homepage to see all available products
2. **Register/Login**: Create an account or login to start shopping
3. **Add to Cart**: Click "Add to Cart" on product detail pages
4. **Manage Cart**: Update quantities or remove items from your cart
5. **Checkout**: Enter shipping address and place your order
6. **View Orders**: Check your order history and track status

### For Administrators

1. **Access Admin Panel**: Go to http://127.0.0.1:8000/admin/
2. **Manage Products**: Add, edit, or delete products
3. **Manage Orders**: View and update order status
4. **Manage Users**: View registered users and their information

## Features Implemented

- [x] Product listing with grid layout
- [x] Product detail page
- [x] User registration and login
- [x] Shopping cart functionality
- [x] Add/update/remove cart items
- [x] Checkout process
- [x] Order processing and confirmation
- [x] Order history
- [x] Responsive design
- [x] Clean and functional UI
- [x] Admin panel for management
- [x] Sample product data

## Security Notes

- CSRF protection enabled for all forms
- User authentication required for cart and order operations
- Password validation and hashing
- SQL injection prevention through Django ORM

## Development Notes

- DEBUG mode is currently enabled (set DEBUG=False for production)
- SECRET_KEY should be changed for production deployment
- SQLite is used for development; consider PostgreSQL for production
- Static files are served by Django dev server (use proper static file hosting for production)

## License

This project is created for educational purposes as part of the CodeAlpha Full Stack Development Internship.
