# Django-Task Management API
Project README

Overview
This project is a robust Task Management API built using Django and Django REST Framework. The API allows users to manage their tasks efficiently, providing full CRUD (Create, Read, Update, Delete) functionality. It includes user authentication, task filtering, sorting, and proper handling of task status and due dates. The project is designed to simulate a real-world backend development environment, including database management and API deployment.

Key Features
Task Management (CRUD): Users can create, retrieve, update, and delete their tasks. Each task includes a Title, Description, Due Date, Priority Level (Low, Medium, High), and Status (Pending, Completed).

User Authentication: Secure user management is implemented using Django's built-in authentication system, ensuring that each user can only access and manage their own tasks.

Task Status Updates: Dedicated endpoints are available to mark tasks as complete or incomplete. Once a task is completed, it becomes read-only unless reverted to the incomplete status.

Filters & Sorting: The API provides powerful filtering options for tasks based on their Status, Priority, and Due Date. Tasks can also be sorted by Due Date or Priority Level.

RESTful Design: All endpoints adhere to RESTful principles, using appropriate HTTP methods (GET, POST, PUT, DELETE) and returning clear HTTP status codes for efficient error handling.

Database Management: The API uses Django ORM to define and manage database models for Tasks and Users, with a clear one-to-many relationship ensuring task ownership.

Technical Stack
Backend Framework: Django

API Framework: Django REST Framework (DRF)

Database: Django ORM (compatible with SQLite, PostgreSQL, etc.)

Authentication: Django's built-in authentication with optional JWT integration for a more secure API.

Deployment: The API is designed to be deployed on platforms like Heroku or PythonAnywhere.
