# StudentSync

## Overview

StudentSync is an academic-focused communication platform built using Python Django and SQLite. This application aims to streamline communication and collaboration among students and educators in an academic setting. Whether it's sharing resources, discussing assignments, or coordinating group projects, StudentSync provides a centralized hub for academic interactions.

## Features

- **User-friendly Interface**: Intuitive design for easy navigation and a seamless user experience.
  
- **Role-based Access**: Distinct user roles for students and educators, ensuring appropriate access levels.

- **Messaging System**: Real-time messaging for direct communication among users.

- **Resource Sharing**: Upload and download resources such as documents, presentations, and more.

- **Discussion Forums**: Create and participate in academic discussions within dedicated forums.


## Installation

### Prerequisites

- Python 3.x
- Django
- SQLite

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/charankulal/StudentSync.git
    cd StudentSync
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1. Login with your superuser credentials to access administrative features.

2. Create student and educator accounts.

3. Explore messaging, resource sharing, discussion forums, and calendar features.


## Acknowledgments

- Special thanks to the Django and Python communities for their incredible support and resources.

Feel free to reach out with any questions, issues, or suggestions. Happy coding!
