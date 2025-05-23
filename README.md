# Invoice Scanner Application

A Django-based web application for extracting and managing data from bus ticket PDF invoices.

## Features

- **User Authentication**: Secure signup, login, and logout functionality
- **PDF Invoice Processing**: Extract detailed information from bus ticket invoices
- **Data Storage**: Store extracted invoice data in MySQL database
- **Data Export**: Download extracted data as CSV files
- **API Access**: RESTful API endpoints for programmatic data access

## Application Structure

The application follows a standard Django project structure:
- `invoice_app/`: Main application module
- `invoice_scanner/`: Project configuration
- HTML templates for views
- REST API endpoints

## Data Extraction

The system extracts the following information from bus ticket invoices:
- Invoice number and date
- Place of supply
- Document type
- Customer name and location
- PNR number
- Bus operator details
- Origin and destination
- Financial information (bus fare, discounts, taxes, total value)

## Installation

### Prerequisites
- Python 3.10+
- MySQL

### Steps

1. Clone the repository
```bash
git clone https://github.com/yourusername/data-extraction-invoice.git
cd data-extraction-invoice
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up MySQL database
```bash
# Create a MySQL database named 'invoicedb'
# Make sure MySQL is running with these credentials:
# Username: root
# Password: Pass@123
# Host: localhost
# Port: 3306
```

5. Run migrations
```bash
python manage.py makemigrations invoice_app
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

7. Access the application
- Open your browser and navigate to `http://127.0.0.1:8000/`
- Create a new account and log in
- Start uploading and processing invoices

## Usage

1. **Log in** or **Sign up** if you're a new user
2. **Upload Invoice**: Select a PDF bus ticket invoice
3. **View Results**: See extracted data after processing
4. **Download CSV**: Export data for further analysis
5. **View All Invoices**: See list of all processed invoices
6. **API Access**: Use the API endpoints for programmatic access

## API Endpoints

- `/api/invoices/`: List all processed invoices

## Production Deployment Considerations

For production deployment:
1. Update `SECRET_KEY` in settings.py
2. Set `DEBUG = False`
3. Configure proper database credentials
4. Set up proper static files serving
5. Configure web server (Nginx, Apache, etc.)

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: MySQL
- **PDF Processing**: PyPDF2
- **Data Handling**: Pandas
- **Authentication**: Django authentication system

## License

[MIT](LICENSE)

## Disclaimer

This application is designed specifically for bus ticket invoices with a particular structure. It may not work correctly with other types of invoices or documents.
