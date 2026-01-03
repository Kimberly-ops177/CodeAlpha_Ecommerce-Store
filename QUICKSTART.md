# Quick Start Guide

## Running the E-Commerce Application

### Step 1: Create an Admin Account (Optional but Recommended)
```bash
python manage.py createsuperuser
```
Enter your desired username, email, and password when prompted.

### Step 2: Start the Development Server
```bash
python manage.py runserver
```

### Step 3: Access the Application
Open your web browser and navigate to:
- **Main Store**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Testing the Application

### As a Customer:
1. Visit http://127.0.0.1:8000/
2. Click "Register" to create a new account
3. Login with your credentials
4. Browse products on the homepage
5. Click "View Details" on any product
6. Click "Add to Cart" to add items
7. Visit your cart to review items
8. Proceed to checkout
9. Enter shipping address and place order
10. View your orders in "My Orders"

### As an Administrator:
1. Visit http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. Manage products, orders, and users
4. Add new products
5. Update order status
6. View customer information

## Sample Data

The application already includes 10 sample products:
- Wireless Headphones ($199.99)
- Smart Watch ($299.99)
- Laptop Stand ($49.99)
- Mechanical Keyboard ($129.99)
- Wireless Mouse ($39.99)
- USB-C Hub ($59.99)
- Portable Charger ($44.99)
- Webcam HD ($79.99)
- Phone Case ($24.99)
- Bluetooth Speaker ($89.99)

## Troubleshooting

### Server won't start?
Make sure you're in the correct directory and Django is installed:
```bash
cd "c:\Users\USER\Documents\CodeSoft\E-Commerce System"
pip install -r requirements.txt
```

### Can't access the site?
Make sure the server is running and visit http://127.0.0.1:8000/ (not localhost)

### Database errors?
Run migrations again:
```bash
python manage.py migrate
```

## Next Steps

- Customize the product catalog through the admin panel
- Add your own products with real images
- Modify the CSS in `static/css/style.css` to match your brand
- Update order status for customer orders
- Explore the code to understand how it works

Enjoy your e-commerce store!
