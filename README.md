# StepStyle - Django Shoes Store

A modern and responsive online shoes store built with Django 4+ and Bootstrap 5, similar to Campus Shoes.

## Features

### 🏠 Homepage
- Hero carousel with featured products
- Product categories section
- Trending products grid
- Features section (Free shipping, Returns, Support, Security)

### 🛍️ Product Management
- Product listing page with filters and search
- Category-based filtering
- Product detail pages with image gallery
- Stock management
- Related products

### 🛒 Shopping Cart
- Session-based cart management
- Add/remove/update cart items
- Cart persistence across sessions
- Recommended products in cart

### 💳 Checkout Process
- Secure checkout form
- Customer information collection
- Multiple payment options (Card, PayPal, COD)
- Order confirmation page

### 👤 Admin Panel
- Full Django admin integration
- Product and category management
- Order management
- Image upload support

### 📱 Additional Pages
- About Us page with company info
- Contact Us page with form and FAQs
- Responsive design for mobile and desktop

## Technology Stack

- **Backend**: Django 5.2.5
- **Database**: SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Images**: Pillow for image handling
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd shoes_store_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data**
   ```bash
   python manage.py populate_data
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
shoes_store_project/
│
├── shoes_store/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── products/              # Main products app
│   ├── models.py         # Category, Product, Order models
│   ├── views.py          # All view functions
│   ├── urls.py           # URL patterns
│   ├── admin.py          # Admin configuration
│   └── management/       # Custom management commands
│
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Homepage
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
│   └── products/         # Product-related templates
│
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Custom CSS
│   └── js/
│       └── main.js       # Custom JavaScript
│
└── media/               # User uploaded files
    └── products/        # Product images
```

## Models

### Category
- `name`: Category name (unique)
- `created_at`: Creation timestamp

### Product
- `name`: Product name
- `description`: Product description
- `price`: Product price (DecimalField)
- `image`: Product image (ImageField)
- `stock`: Available quantity
- `category`: Foreign key to Category
- `created_at`: Creation timestamp

### Order
- `product`: Foreign key to Product
- `quantity`: Order quantity
- `customer_name`: Customer name
- `customer_email`: Customer email
- `address`: Shipping address
- `created_at`: Order timestamp

## Sample Data

The project includes 10 sample shoe products across 4 categories:
- **Sports Shoes**: Nike Air Max 270, Adidas Ultraboost 22
- **Casual Shoes**: Converse Chuck Taylor, Vans Old Skool, Timberland Boot
- **Formal Shoes**: Cole Haan Oxford, Clarks Desert Boot
- **Sneakers**: Jordan 1 Retro, New Balance 990v5, Puma RS-X3

## Features Overview

### User Features
- Browse products by category
- Search products by name/description
- View detailed product information
- Add products to cart
- Manage cart items (update quantity, remove items)
- Secure checkout process
- Contact form

### Admin Features
- Full CRUD operations for products and categories
- Image upload and management
- Order management and tracking
- User-friendly admin interface

### Technical Features
- Responsive Bootstrap 5 design
- Session-based cart management
- Search functionality
- Image handling with Pillow
- Custom management commands
- Clean URL structure
- SEO-friendly templates

## Customization

### Adding New Products
1. Access the admin panel
2. Go to Products section
3. Click "Add Product"
4. Fill in product details and upload image
5. Save the product

### Modifying Design
- Edit `static/css/style.css` for custom styles
- Modify templates in the `templates/` directory
- Update `static/js/main.js` for additional JavaScript functionality

### Extending Functionality
- Add new models in `products/models.py`
- Create new views in `products/views.py`
- Add URL patterns in `products/urls.py`
- Create corresponding templates

## Deployment

For production deployment:

1. **Environment Variables**
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Use environment variables for sensitive data

2. **Database**
   - Switch to PostgreSQL or MySQL for production
   - Configure database settings

3. **Static Files**
   - Configure `STATIC_ROOT` and `MEDIA_ROOT`
   - Use a web server (Nginx) to serve static files
   - Consider using cloud storage for media files

4. **Security**
   - Use HTTPS
   - Configure security settings
   - Set up proper authentication

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is for educational purposes. Please check individual component licenses for commercial use.

## Support

For support and questions:
- Email: admin@stepstyle.com
- Phone: +1 (555) 123-4567

---

**StepStyle** - Step into Style, Step into Comfort! 👟
