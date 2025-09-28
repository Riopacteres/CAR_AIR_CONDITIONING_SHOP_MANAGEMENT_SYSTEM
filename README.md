# Car Air Conditioning Shop Management System

A comprehensive management system for car air conditioning service shops. This system helps manage customer information, vehicle details, service appointments, inventory, and employee schedules.

## Features

- Customer Management
- Vehicle Information Tracking
- Service Appointments
- Inventory Management
- Employee Management
- Billing and Invoicing
- Service History Tracking

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Riopacteres/CAR_AIR_CONDITIONING_SHOP_MANAGEMENT_SYSTEM.git
cd CAR_AIR_CONDITIONING_SHOP_MANAGEMENT_SYSTEM
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file with your configuration:
```bash
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

5. Initialize the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the application:
```bash
python run.py
```

## Technology Stack

- Python/Flask
- SQLAlchemy
- Flask-Login for authentication
- Bootstrap for frontend
- SQLite/MySQL for database

## License

This project is licensed under the MIT License.