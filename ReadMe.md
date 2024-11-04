# Django Authentication Project

This project is a Django-based authentication system that includes user registration, login, password reset functionality, and a customized UI with a blurred background effect.

## Features

- User Registration
- User Login
- Password Reset
- Responsive UI with a customized CSS for styling
- RTL (Right-to-Left) support for languages such as Persian

## Installation

### Prerequisites

- Python 3.8+
- Django 5.1+
- Virtual environment (optional but recommended)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/django_auth_project.git
   cd django_auth_project
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your browser and navigate to `http://127.0.0.1:8000`.

## Project Structure

```
django_auth_project/
├── accounts/               # Django app for handling user authentication
├── static/                 # Static files (CSS, fonts, images)
│   ├── css/
│   │   └── style.css       # Custom styles
│   ├── fonts/
│   └── images/
├── templates/              # HTML templates
│   ├── base.html           # Base template for the app
│   ├── home.html           # Home page template
│   ├── login.html          # Login page template
│   ├── register.html       # Registration page template
│   └── forgot_password.html # Password reset page template
├── manage.py               # Django management script
└── django_auth_project/     # Project configuration folder
    ├── settings.py         # Django settings
    ├── urls.py             # URL configuration
    ├── wsgi.py             # WSGI entry point for deployment
    └── asgi.py             # ASGI entry point for asynchronous deployment
```

## Environment Variables

For email functionality (e.g., password reset), you need to configure email settings in `settings.py`. Set the following environment variables or directly configure in the settings file:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
```

> **Note**: Avoid hardcoding credentials. Use environment variables for sensitive data in production.

## Customization

- **Styles**: Modify `static/css/style.css` to adjust the styling of the UI.
- **Templates**: The main templates are located in the `templates/` folder, including `base.html`, `home.html`, `login.html`, `register.html`, and `forgot_password.html`.

## License

This project is licensed under the MIT License.

## Acknowledgments

- The project was created using Django.
- Icons provided by [Boxicons](https://boxicons.com/).
