# Project1

A basic Django web application demonstrating form handling, template usage, and integration with SQL databases (SQLite and PostgreSQL).

## Features

- Django-powered homepage and random page
- Custom landing page form with validation
- Bootstrap-based responsive templates
- Switchable database backend (SQLite or PostgreSQL)

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- (Optional) PostgreSQL for advanced database support

### Installation

1. Clone the repository:
    ```powershell
    git clone https://github.com/yourusername/Project1.git
    cd Project1
    ```

2. Install dependencies:
    ```powershell
    pip install -r requirements.txt
    ```

3. (Optional) Install PostgreSQL driver:
    ```powershell
    pip install psycopg2-binary
    ```

### Database Setup

- Default: SQLite (`db.sqlite3`)
- To use PostgreSQL, update `cfehome/settings.py` with your database credentials.

### Running the Project

```powershell
python manage.py migrate
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure

```
Project1/
├── cfehome/
│   ├── forms.py
│   ├── view.py
│   ├── settings.py
│   └── ...
├── templates/
│   ├── base.html
│   ├── home.html
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md
```

## License

This project is licensed under the MIT License.

## Author

MD. Safaet Ullah
BSc in CSE(SUST)
Lecturer 
RPSU
