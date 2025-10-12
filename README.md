# 📚 Bookaroo

# Bookaroo

## Introduction

**Bookaroo** is a comprehensive web application built with Django that allows users to easily manage
their personal book collections. It provides an organized catalog of books where users can browse,
view detailed information including title, author(s), publication date, description, stock
availability, and cover images.

### User Features

Registered users can:

-   Reserve books and track their reservations.
-   Cancel reservations if needed, with the system automatically updating stock levels.
-   Browse authors and explore books by specific authors.

### Administrator Features

Administrators have full control over the platform:

-   Add, edit, and remove books and authors.
-   Monitor all active reservations to maintain smooth operations.
-   Ensure data integrity and manage stock automatically.

### Technology & Deployment

-   **Backend**: Django with PostgreSQL for reliable data management.
-   **Media Storage**: Cloudinary for efficient handling of book cover images.
-   **Design**: Responsive and accessible, working seamlessly on desktop, tablet, and mobile
    devices.
-   **Deployment**: Deployed on Heroku for easy online access.

### Summary

Bookaroo combines practical book management features with modern web development practices,
providing an intuitive and reliable platform for both casual readers and administrators.

🔗 [Live Site](https://my-project-bookaroo-c4b25e8254c6.herokuapp.com/)

---

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Repository Structure](#repository-structure)
4. [Agile Planning](#agile-planning)
    - [UI Design](#ui-design)
        - [Wireframes](#wireframes)
        - [User Stories](#user-stories)
        - [Project Board](#project-board)
5. [Database](#database)
    - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
6. [AI Usage](#ai-usage)
7. [Deployment](#deployment)
    - [Local Setup](#local-setup)
    - [Heroku Deployment](#heroku-deployment)
8. [Testing](#testing)
9. [Key Features](#key-features)
10. [Site Contents](#site-contents)
11. [Accessibility & UX](#accessibility--ux)
12. [Acknowledgements](#acknowledgements)
13. [Links](#links)
14. [License](#license)

---

## Technologies Used

Bookaroo uses a variety of technologies to provide a secure, responsive, and robust experience. Key
technologies include Django, PostgreSQL, Cloudinary, and Bootstrap.

For a complete list of Python packages, their versions, and purposes, see the
[Technical Stack Wiki](https://github.com/RocioSerrano0921/bookaroo/wiki/Technical-Stack).

**Backend:**

-   Django 4.2 – Python web framework used to build the application.
-   PostgreSQL – Relational database used for storing books, authors, users, and reservations.

**Frontend:**

-   HTML5, CSS3, Bootstrap 5 – Used for building responsive, accessible interfaces.

**Media & Storage:**

-   Cloudinary – Cloud-based service for storing and serving book cover images.

**Deployment:**

-   Heroku – Platform for hosting the web application.
-   Gunicorn – WSGI server for serving Django in production.

**Authentication & Security:**

-   django-allauth – Handles user authentication, registration, and social login.
-   PyJWT – For managing JSON Web Tokens if needed.
-   cryptography – Ensures secure data handling.

**Development & Utilities:**

-   Git & GitHub – Version control.
-   Django Debug Toolbar – For debugging SQL queries and requests.
-   Whitenoise – Efficiently serves static files in production.

---

## Repository Structure

The project is organized as follows:

![Repository Structure](assets/repository-structure2.png)

---

## Agile Planning

### UI Design

## UI Overview

Bookaroo provides an intuitive and responsive interface. Users can:

-   Browse a catalog of books with filtering and sorting options.
-   View detailed book information including authors, stock, and descriptions.
-   Manage reservations through a clear user dashboard.
-   Admins can create, edit, or delete books and authors through structured forms.
-   The layout is consistent across pages, with a shared header, navigation, and footer, and works
    seamlessly on desktop, tablet, and mobile devices.

### Design Principles

-   **Clean and Modern Layout:** The interface uses a simple and intuitive design, with a consistent
    header, footer, and navigation menu.
-   **Responsive Design:** Implemented with **Bootstrap 5**, adapting to different screen sizes
    (desktop, tablet, mobile).
-   **Consistent Styling:** Colors, fonts, and button styles are consistent across pages for a
    professional look.
-   **Accessibility:** Forms include labels and validation messages; color contrast ensures
    readability.

### Navigation

-   **Header Navigation:** Includes links to Home, Books, Authors, Login/Register, and My
    Reservations (for authenticated users).
-   **Footer:** Contains the brand
-   **Forms:** Book creation, author creation, and reservation forms provide clear instructions and
    feedback.

### Color Palette

Bookaroo’s design uses a warm, neutral palette that reflects a calm and elegant reading
environment.  
The combination of light backgrounds, brown tones, and muted blues ensures good readability and a
pleasant user experience.

| Color Role               | Hex Code  | Description                              |
| ------------------------ | --------- | ---------------------------------------- |
| **Background Primary**   | `#f9f9f9` | Main page background                     |
| **Background Secondary** | `#f9f6f1` | Section backgrounds and cards            |
| **Primary Colour**       | `#60422e` | Headings, key highlights, and icons      |
| **Secondary Colour**     | `#aa9581` | Accents and hover states                 |
| **Text Primary**         | `#30465a` | Main body text                           |
| **Text Secondary**       | `#aebacd` | Subtle or secondary text                 |
| **Button Primary**       | `#b08d6f` | Primary buttons and interactive elements |
| **Button Edit**          | `#f9c646` | Edit or warning buttons                  |
| **Button Error**         | `#e43c3c` | Delete or error alerts                   |

---

**Design Notes**

-   The soft beige and brown tones create a cozy “library-like” feel, aligning with the book theme.
-   Muted blue text colors ensure contrast and readability without harshness.
-   Distinct button colors (`#b08d6f`, `#f9c646`, `#e43c3c`) help users clearly identify different
    actions (primary, edit, delete).
-   The palette maintains accessibility standards with sufficient color contrast for legibility.

**Visual Palette:** ![Bookaroo Color Palette](assets/colour_palette.png)

#### 🧩 Accessibility & Colour Contrast

Bookaroo’s color palette was tested to ensure sufficient contrast and accessibility for all users.  
All primary text and background combinations meet **WCAG AA** or higher standards.

**Contrast Testing Tools Used:**

-   [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

**Screenshots of Colour Checks:**

-   **Primary Text on Background:**  
    ![Primary Text Colour Check](assets/colour-checker2.png)

-   **Buttons Contrast Test:**  
    ![Buttons Contrast Test](assets/colour_checker1.png)

### 📱 Key Pages

-   **Landing Page:** Clean welcome page with links to main features.  
    ![Landing Page Screenshot](assets/screenshots_page/landing_page.png)

-   **Book List & Detail Pages:** Cards or lists displaying book information, authors, availability,
    and actions (reserve, edit, delete for admins).  
    ![Book List Screenshot](assets/screenshots_page/admin-list-books.png)

    ![Book Register Form Screenshot](assets/screenshots_page/book_registration_form.png)

-   **Author Pages:** List authors with options to create, edit, or delete (admin) and view their
    books.

    ![Authors List Screenshot](assets/screenshots_page/author_list.png)  
    ![Author Register Form Screenshot](assets/screenshots_page/author_registration_form.png.png)

-   **Available Books Page**  
    Shows the list of all books available for reservation.  
    ![Available Books](assets/screenshots_page/available_books.png)

-   **Book Detail Page**  
    Displays detailed information about a selected book.  
    ![Book Detail](assets/screenshots_page/book_detail.png)

-   **Reservation Pages:** manage reservations (edit days, cancel).  
    ![My Reservations Screenshot](assets/screenshots_page/my_reservations.png)

-   **Authentication Pages:** Login, register(via Django Allauth templates).  
    ![Login Screenshot](assets/screenshots_page/log_in_form1.png)  
    ![Register Screenshot](assets/screenshots_page/register_form.png)

### 📣 Confirmation Messages / Alerts

To demonstrate clear user feedback, the following screenshots show confirmations for key actions:

**Login Confirmation**  
![Login Confirmation](assets/screenshots_page/messages_confirmation_login.png)

**Logout Confirmation**  
![Logout Confirmation](assets/screenshots_page/message_confirmation_signout1.png)

**Registration Confirmation**  
![Registration Confirmation](assets/screenshots_page/register_confirmation.png)

**Book Reserved Confirmation**  
![Book Reserved Confirmation](assets/screenshots_page/message_confirmation_book_reserved.png)

**Duplicate Reservation Error**  
Displayed when a user tries to reserve the same book more than once.  
![Duplicate Reservation Error](assets/screenshots_page/book_reserved_no_duplication.png)

**Reservation Cancelled Confirmation**  
![Reservation Cancelled Confirmation](assets/screenshots_page/reservation_cancelled.png)

**Edit Reservation Days Confirmation**  
![Edit Reservation Days Confirmation](assets/screenshots_page/messages_confirmation_edit_days.png)

**Book Deleted (Admin) Confirmation**  
![Book Deleted Confirmation](assets/screenshots_page/messages_confirmation_book_deleted.png)

**Author Deleted (Admin) Confirmation**  
![Author Deleted Confirmation](assets/screenshots_page/author_deleted_confirmation.png)

### Front-End Stack

-   HTML5, CSS3 (**Bootstrap 5**), JavaScript
-   Django Templates for dynamic content rendering
-   **Cloudinary** for book images

#### Wireframes

The wireframes were designed to plan the structure, user experience, and responsive layout of
**Bookaroo** before development.  
They represent the core user-facing pages and the main interaction flow — from browsing books to
managing reservations.

Below are the main wireframes included in this project:

---

### Landing Page

This is the public entry point of the site.  
It presents the app’s purpose and gives access to login or browsing available books.

![Landing Page Wireframe](assets/wireframes/wireframe-landing.png)

---

### Home Page

The homepage displays a summary of key actions available to the user,  
such as viewing available books, managing reservations, or browsing authors.

![Home Page Wireframe](assets/wireframes/wireframe-home.png)

---

### Available Books

This page lists all active books in the catalog.  
Users can browse, search, or filter books by author or title.

![Available Books Wireframe](assets/wireframes/wireframe-available-books.png)

---

### Book Detail

Displays detailed information about a selected book — including title, author(s), publication date,
and stock.  
Registered users can reserve or cancel a reservation from this page.

![Book Detail Wireframe](assets/wireframes/wireframe-book-detail.png)

---

### 📦 My Reservations

This view allows users to see all their active and past reservations.  
It includes options to cancel an existing reservation when needed.

![My Reservations Wireframe](assets/wireframes/wireframe-reservations.png)

---

### 🧱 Template Structure

The Django template inheritance pattern for **Bookaroo** follows a clear hierarchy for organization
and reusability.

![Template_structure](assets/templates-structure.png)

> **Note:** Administrative templates such as _Book Management_ and _Author Management_ are
> documented in the [Wiki – UI Section](https://github.com/yourusername/bookaroo/wiki/UI-Design) for
> clarity and to maintain a concise README.

## User Stories (Aligned with Code Institute Evaluation Criteria)

### Book Management (CRUD & Display)

-   **As a user**, I want to view a list of all books so that I can browse the collection.
-   **As a user**, I want to view details of each book (title, author(s), published date,
    description, stock) to learn more about each book.
-   **As a user**, I want to add new books (if I am an admin) to expand the collection.
-   **As a user**, I want to edit book details (if I am an admin) to keep information accurate.
-   **As a user**, I want to delete books (if I am an admin) to maintain a relevant catalog.
-   **As a user**, I want to search for books by title or author to quickly find specific books.
-   **As a user**, I want to filter books by author to see only books by a specific author.
-   **As a user**, I want to sort books by title or author to navigate easily.

### Author Management (CRUD)

-   **As an admin**, I want to add new authors to enrich the database.
-   **As an admin**, I want to edit existing author information to keep it accurate.
-   **As an admin**, I want to deactivate authors (soft delete) to maintain data integrity without
    removing associated books.
-   **As a user**, I want to view all authors and their books to explore their works.

### Book Reservations (Stock Management & Business Rules)

-   **As an authenticated user**, I want to reserve a book so that it will be available for me.
-   **As an authenticated user**, I want to cancel a reservation to free the book for others.
-   **As an authenticated user**, I want to view all my current and past reservations to track my
    activity.
-   **As an admin**, I want to see all active reservations to monitor system usage.
-   **As a user**, I want the system to prevent me from reserving a book that has no stock.
-   **As a user**, I want the system to prevent me from reserving the same book more than once at
    the same time.
-   **As an admin**, I want book stock to automatically update when a reservation is created or
    canceled.

### Authentication & User Profiles

-   **As a new user**, I want to register an account to use the application.
-   **As a user**, I want to log in securely to access my profile and reservations.
-   **As a user**, I want to log out to secure my account.
-   **As a user**, I want to update my profile information to keep it accurate.
-   **As a user**, I want to reset my password if I forget it.

### UI & UX (Accessibility & Responsiveness)

-   **As a user**, I want the site to be responsive on mobile, tablet, and desktop devices.
-   **As a user**, I want clear navigation so I can easily find books, authors, and reservations.
-   **As a user**, I want forms to include validation and helpful error messages to prevent
    mistakes.
-   **As a user**, I want color contrasts and readable fonts for accessibility.

### Testing

-   **As a developer**, I want unit tests for models and forms to ensure they work correctly.
-   **As a developer**, I want integration tests to verify relationships between models and views.
-   **As a developer**, I want functional tests for the user workflow (reserving books, CRUD
    operations) to ensure everything works as expected.

### Deployment & Documentation

-   **As a user**, I want the application to be deployed and accessible online.
-   **As a developer**, I want detailed README documentation to guide setup, usage, and
    contribution.

#### Project Board

The project was organized using GitHub Projects. Tasks were tracked through columns:

-   To Do
-   In Progress
-   Review
-   Done

🔗 [Project Board](#)

---

## Database

The database schema was designed to efficiently store book information and user data. Django's ORM
ensures consistency and integrity.

## Models

The Bookaroo application has three main models: **Author**, **Book**, and **BookReservation**. These
models handle the core functionality of managing books, authors, and reservations. Below is a
concise overview of their essential fields and relationships.

| Model               | Essential Fields                                 | Relationships / Notes                                                                                             |
| ------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **Author**          | first_name, last_name, country                   | Many-to-Many with Book. Authors can be soft-deleted without removing associated books.                            |
| **Book**            | title, published_date, stock, is_active          | Many-to-Many with Author. Stock is managed automatically via reservations.                                        |
| **BookReservation** | user (FK), book (FK), days_reserved, reserved_at | Links users to reserved books. Enforces unique active reservation per user & stock management via Django signals. |

**Business Logic Highlights:**

-   Only active authors/books are considered in operations.
-   Users cannot reserve the same book more than once at the same time.
-   Book stock is dynamically updated when reservations are created or canceled.
-   Images are stored in Cloudinary (for book covers).

> Note: Detailed model methods, signals, and constraints are documented in the
> [Models Documentation](https://github.com/RocioSerrano0921/bookaroo/wiki/Models) for developers.

---

### Entity Relationship Diagram (ERD)

[ERD Diagram](#)

---

> **Note:** Mermaid diagrams render on GitHub.  
> If the diagram does not appear, view the [PNG version here](assets/conceptualERD.png).

```mermaid
---
title:  Bookaroo Management System - CONCEPTUAL  ER Diagram
---

erDiagram
    USER {
        int id PK
        string username
        string email
    }

    AUTHOR {
        int id PK
        string first_name
        string last_name
        string country
    }

    BOOK {
        int id PK
        string title
        date published_date
        int stock
        string image
        boolean is_active
    }

    BOOKRESERVATION {
        int id PK
        int user_id FK
        int book_id FK
        int days_reserved
        datetime reserved_at
        boolean is_active
    }

    %% Relationships
    AUTHOR }o--o{ BOOK : "writes"
    BOOK ||--o{ BOOKRESERVATION : "is reserved in"
    USER ||--o{ BOOKRESERVATION : "makes"

    %% ✅ Custom styling (GitHub-safe)
    classDef user fill:#E0F7FA,stroke:#006064,stroke-width:1px,color:#004D40
    classDef author fill:#FFF3E0,stroke:#E65100,stroke-width:1px,color:#E65100
    classDef book fill:#E8F5E9,stroke:#2E7D32,stroke-width:1px,color:#1B5E20
    classDef reservation fill:#F3E5F5,stroke:#6A1B9A,stroke-width:1px,color:#4A148C

    class USER user
    class AUTHOR author
    class BOOK book
    class BOOKRESERVATION reservation

```

---

### 🧩 **Relationship Summary**

| Relationship               | Type         | Description                                                               |
| -------------------------- | ------------ | ------------------------------------------------------------------------- |
| **Author ↔ Book**          | Many-to-Many | An author can write multiple books, and a book can have multiple authors. |
| **Book ↔ BookReservation** | One-to-Many  | A book can have many reservations.                                        |
| **User ↔ BookReservation** | One-to-Many  | A user can make many reservations.                                        |

---

[Technical Flowchart](#)

> **Note:** Mermaid diagrams render on GitHub.  
> If the diagram does not appear, view the [PNG version here](assets/technicalFlowchart.png).

```mermaid
---
title: TECHNICAL FLOWCHART
---

flowchart LR
    %% Entities
    USER["👤 USER
    ----------------------
    • username
    • email"]

    BOOKRESERVATION["📦 BOOK RESERVATION
    ----------------------
    • user (FK)
    • book (FK)
    • days_reserved
    • reserved_at
    • expires_at"]

    BOOK["📘 BOOK
    ----------------------
    • title
    • published_date
    • description
    • stock
    • author (M2M)"]

    AUTHOR["✍️ AUTHOR
    ----------------------
    • first_name
    • last_name
    • country"]

    %% Relationships
    USER -->|"makes"| BOOKRESERVATION
    BOOKRESERVATION -->|"reserves"| BOOK
    BOOK -->|"written by"| AUTHOR
    AUTHOR -->|"writes"| BOOK

    %% Styling
    classDef user fill:#E0F7FA,stroke:#006064,stroke-width:1px,color:#004D40,font-weight:bold
    classDef author fill:#FFF3E0,stroke:#E65100,stroke-width:1px,color:#E65100,font-weight:bold
    classDef book fill:#E8F5E9,stroke:#2E7D32,stroke-width:1px,color:#1B5E20,font-weight:bold
    classDef reservation fill:#F3E5F5,stroke:#6A1B9A,stroke-width:1px,color:#4A148C,font-weight:bold

    class USER user
    class AUTHOR author
    class BOOK book
    class BOOKRESERVATION reservation


```

## 🤖 AI Usage

AI tools, including ChatGPT, were used to:

-   Generate README documentation
-   Draft user stories
-   Improve explanations and descriptions

---

## 🚀 Deployment

### Local Setup

## Local Installation and Configuration

Follow these steps to run **Bookaroo** on your local machine:

---

### 1. Clone the Repository

Open your terminal and execute the following commands:

```bash
git clone https://github.com/RocioSerrano0921/bookaroo.git
cd bookaroo
```

This will download the project into a folder called bookaroo.

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

On macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

-   python3 -m venv venv creates a new virtual environment in a folder called venv.

-   Source venv/bin/activate activates the virtual environment.

-   When activated, your terminal prompt should start with (venv).

### 3. Install Project Dependencies

With the virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

This command reads requirements.txt and installs all necessary libraries for Bookaroo.

### 4. Set Up Environment Variables

Create a file called .env in the root directory of the project and add the following variables:

```bash
DEBUG=True
SECRET_KEY='your_secret_key_here'
DATABASE_URL='postgres://username:password@localhost:5432/bookaroo'
```

-   Replace 'your_secret_key_here' with a secure, unique secret key.

-   Replace username and password with your PostgreSQL credentials.

-   Important: Never commit your .env file to version control for security reasons.

### 5. # PostgreSQL Setup and Django Integration

Follow these steps to set up your PostgreSQL database via Code Institute and connect it to your
Django project.

---

## 5.1 Access Code Institute PostgreSQL Portal

-   Go to [https://dbs.ci-dbs.net/](https://dbs.ci-dbs.net/).
-   Enter your Code Institute LMS email.
-   Create a new database. A unique URL will be generated for your database.
-   Check your email for the management link (acts as your password, keep it safe).

---

## 5.2 Prepare Django Project for PostgreSQL

### Enable Debug Mode

-   Open `codestar/settings.py` and set:

```python
DEBUG = True
```

### Create env.py

-   At the top level of your project:

```python
touch env.py
```

-   Add env.py to .gitignore to prevent sensitive data from being pushed:

```python
env.py
```

-   Add Database URL to env.py

```python
import os

os.environ.setdefault(
    "DATABASE_URL", "<your-database-URL>"
)
```

Make sure to include quotes around your URL.

### 5.3 Install Required Packages

```bash
pip3 install dj-database-url~=0.5 psycopg2~=2.9
pip3 freeze --local > requirements.txt
```

-   psycopg2 → PostgreSQL driver for Python.

-   dj-database-url → Connect Django to a database via URL.

### 5.4. Connect Django Settings to Environment Variables

-   Open bookaroo/settings.py and add imports:

```python
import os
import dj_database_url

if os.path.isfile('env.py'):
    import env
```

-   Delete the default SQLite3 configuration:

```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }
```

-   Add PostgreSQL connection using the environment variable:

```python
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```

### 5.5. Apply Django Migrations

python3 manage.py migrate

### 5.6. Create a Superuser

To access the Django admin panel, create a superuser:

```python
python manage.py createsuperuser
```

You will be prompted to enter:

Username

Email address

Password

### 5.7. Run the Development Server

Start the local Django development server:

```python
python manage.py runserver
```

Once the server is running, open your browser and visit:

http://127.0.0.1:8000/

## You should now see the Bookaroo application running locally.

### 5.8. Notes

To deactivate the virtual environment, run:

```bash
deactivate
```

Remember to keep your .env file secure.
