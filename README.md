# Bookaroo

## 📋 Table of Contents

1. [Introduction](#introduction)
    - [User Features](#user-features)
    - [Administrator Features](#administrator-features)
    - [Technology & Deployment](#technology--deployment)
    - [Summary](#summary)
2. [Technologies Used](#technologies-used)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [Media & Storage](#media--storage)
    - [Deployment](#deployment-1)
    - [Authentication & Security](#authentication--security)
    - [Development & Utilities](#development--utilities)
3. [Repository Structure](#repository-structure)
4. [Agile Planning](#agile-planning)
    - [UI Design](#ui-design)
        - [UI Overview](#ui-overview)
        - [Design Principles](#design-principles)
        - [Navigation](#navigation)
        - [Wireframes](#wireframes)
            - [Landing Page](#landing-page)
            - [Home Page](#home-page)
            - [Available Books](#available-books)
            - [Book Detail](#book-detail)
            - [My Reservations](#my-reservations)
        - [Template Structure](#template-structure)
        - [Color Palette](#color-palette)
        - [Accessibility & Colour Contrast](#accessibility--colour-contrast)
        - [Key Pages](#key-pages)
        - [Confirmation Messages / Alerts](#confirmation-messages--alerts)
        - [Front-End Stack](#front-end-stack)
    - [Roles and Access Control](#roles-and-access-control)
        - [User Roles Overview](#user-roles-overview)
        - [Access Control Matrix](#access-control-matrix)
        - [Implementation Details](#implementation-details)
            - [Authentication System](#authentication-system)
            - [Authorization Logic](#authorization-logic)
            - [Regular User Views](#regular-user-views)
            - [Database and Model Permissions](#database-and-model-permissions)
            - [User Feedback and Messaging](#user-feedback-and-messaging)
            - [Forms & Validations](#forms--validations)
5. [Project Board](#project-board)
6. [Database](#database)
    - [Models](#models)
    - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
    - [Relationship Summary](#relationship-summary)
    - [Technical Flowchart](#technical-flowchart)
7. [AI Usage](#ai-usage)
8. [Deployment](#deployment)
    - [Local Setup](#local-setup)
    - [PostgreSQL Setup and Django Integration](#postgresql-setup-and-django-integration)
    - [Heroku Deployment](#heroku-deployment)
9. [Testing](#testing)
10. [Acknowledgments](#acknowledgments)
11. [Links](#links)
12. [License](#license)

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

### Agile Planning

## UI Design

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

### Key Pages

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

## 🧑‍💻 Roles and Access Control

Bookaroo implements a **role-based access control (RBAC)** system to ensure that only authorized
users can perform specific actions.  
The design emphasizes **security, usability, and maintainability**, providing distinct permissions
for each user type.

---

### 👥 User Roles Overview

| Role                                  | Description                                                                | Access Level                                                                                                               |
| ------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Anonymous User**                    | A visitor who is not logged in.                                            | Can view the landing page, browse available books, and view book details. Cannot reserve books or access restricted areas. |
| **Registered User**                   | A user with an active account created through Django Allauth registration. | Can log in, reserve and cancel books, view their profile and reservations, and edit reservation days.                      |
| **Administrator (Superuser / Staff)** | A user with administrative privileges (created via `createsuperuser`).     | Full access to Django Admin panel, can manage users, books, and authors. Has all permissions for CRUD operations.          |

---

### 🔐 Access Control Matrix

| Action                     | Anonymous | Registered User | Admin |
| -------------------------- | --------- | --------------- | ----- |
| View Landing Page          | ✅        | ✅              | ✅    |
| View Available Books       | ❌        | ✅              | ✅    |
| View Book Details          | ❌        | ✅              | ✅    |
| Register / Login / Logout  | ✅        | ✅              | ✅    |
| Create Reservation         | ❌        | ✅              | ✅    |
| Cancel Reservation         | ❌        | ✅              | ✅    |
| Edit Reservation Days      | ❌        | ✅              | ✅    |
| View Own Reservations      | ❌        | ✅              | ✅    |
| Add / Edit / Delete Book   | ❌        | ❌              | ✅    |
| Add / Edit / Delete Author | ❌        | ❌              | ✅    |
| Access Admin Dashboard     | ❌        | ❌              | ✅    |

---

### ⚙️ Implementation Details

**Authentication System**

-   Managed using **Django Allauth**, providing secure registration, login, logout, and password
    management.
-   Customized Allauth templates maintain visual consistency with Bookaroo’s branding.
-   Login and logout confirmation messages improve user experience (e.g., _“You have successfully
    logged out.”_).

**Authorization Logic**

Access control is managed through:

1. Template restrictions using {% if request.user.is_superuser %}

2. LoginRequiredMixin in views to ensure only authenticated users can access certain pages.

## Example: Template Restriction (base.html)

```html
{% if request.user.is_superuser %}
<li class="nav-item dropdown">
    <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown">
        <i class="fa fa-users me-2"></i> Books Admin
    </a>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="{% url 'book:books_list' %}">Books List</a></li>
        <li><a class="dropdown-item" href="{% url 'book:create_book' %}">Create Book</a></li>
    </ul>
</li>
{% endif %}
```

This ensures that only superusers can see and access the administrative book and author sections.

## Regular User Views

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Book

class AvailableBooksView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/books/available_books.html'
    context_object_name = 'books'
    paginate_by = 12

    def get_queryset(self):
        """Return only available books (active and in stock)."""
        return self.model.objects.filter(is_active=True, stock__gte=1)
```

![Roles_and_access_control_diagram](assets/roles.png)

**Notes:**

-   Admins see and can use the “Books Admin” and “Authors Admin” links in the UI.

-   Regular users can view available books, make reservations, edit or cancel them, and cannot see
    admin links.

-   The Django admin interface is also protected: only superusers can log in.

-   No additional view-level checks are needed for the MVP because the UI already prevents
    unauthorized access.

**Database and Model Permissions**

-   **Book** and **Author** models are registered in Django Admin for full management control.

-   **BookReservation** model connects to Django’s User model via a ForeignKey, ensuring:

    -   Users can only view and manage their own reservations.

    -   Admins can view and manage all reservations.

-   Data integrity rules (e.g., one active reservation per user/book) are enforced at model level.

**User Feedback and Messaging**

To enhance user experience, Django’s **messages framework** is used to confirm or inform users about
their actions:

Successful login / logout

Book added, edited, or deleted

Book reserved or reservation canceled

Reservation days updated

Unauthorized access attempts

Messages are custom styled for clarity and visual consistency across pages.

## Forms & Validations

Bookaroo implements robust forms with Django Forms for both user-facing and admin actions. Forms
include server-side validation, user-friendly error messages, and role-based accessibility.

### Book Form (Admins Only)

-   **Purpose: Create or edit books.**

-   **Fields:** title, author, published_date, description, stock, image, is_active

-   **Validations:**

    -   Title cannot be empty

    -   Stock must be ≥ 0

    -   At least one author must be selected

-   **Success Message:**

“Book successfully added/updated.”

-   **Error Messages:** Inline errors next to invalid fields

**Screenshot Example:**

![Book_form ](assets/screenshots_page/book_registration_form.png)

### Author Form

Used by administrators to create or edit authors.

-   **Purpose:** Create or edit authors.

-   **Fields:** first_name, last_name, country, is_active

-   **Validations:**

    -   First and last name are required

    -   Country is required

-   **Success Message:** “Author successfully added/updated.”

-   **Error Messages:** Inline errors for invalid or empty fields

**Screenshot Example:**

![Author_form ](assets/screenshots_page/author_registration_form.png)

### Book Reservation Form (Registered Users)

-   **Purpose:** Reserve books

-   **Fields:** Automatically set via the view: user, book

-   **Validations:**

    -   Book must have available stock

    -   User cannot reserve the same book twice concurrently

**Success Message:** “Book successfully reserved.”

**Error Messages:**

“No stock available for this book.”

“You already have an active reservation for this book.”

**Screenshot Examples:**

-   Reservation Success:

![Book Reserved Confirmation](assets/screenshots_page/message_confirmation_book_reserved.png)

Duplicate Reservation unavailable:

![Book Reserved Confirmation](assets/screenshots_page/book_reserved_no_duplication.png)

### Edit Days Reservation Form (Registered Users)

-   **Purpose:** Modify the number of days reserved for a book

-   **Field:** days_reserved (integer)

-   **Validations:**

    -   Must be between 1 and 15

-   **Success Message:** “Reservation days updated successfully.”

-   **Error Messages:** Inline message if outside allowed range

**Screenshot Example:**

![Days Reservation](assets/screenshots_page/messages_confirmation_edit_days.png)

#### Role-Based Form Access

| Form                    | Accessible By    | Notes                              |
| ----------------------- | ---------------- | ---------------------------------- |
| BookForm                | Admin Only       | Create/edit books                  |
| AuthorForm              | Admin Only       | Create/edit authors                |
| BookReservationForm     | Registered Users | Reserve books, manage reservations |
| EditDaysReservationForm | Registered Users | Update reservation period          |

#### Project Board

The project was organized using GitHub Projects. Tasks were tracked through columns:

-   To Do
-   In Progress
-   Review
-   Done

🔗 [Project Board]()

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

### Testing

Testing is a key component to ensure that the **Bookaroo** application works as expected and meets
business rules. The purpose of this section is to document which functionalities have been tested,
whether they work correctly, and to what extent.

The testing approach applied to this project includes:

-   **Manual testing:** Verification of main flows such as book CRUD, reservations, and
    authentication.

-   **Business-rule testing:** Checking constraints like available stock and prevention of duplicate
    reservations.

UI/UX testing: Review of accessibility, keyboard navigation, screen reader support, and responsive
design on different devices.

Documented testing: Although the project does not include a complete automated test suite, it
clearly records which functionalities have been verified and their status.

The table below shows the **User Stories**, indicating whether they were tested and whether they
work as intended:

| User Stories                                                                                                                                        | Tested     | Works as Intended |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----------------- |
| As a **product owner** I can **deploy the app to a cloud platform** so that **end users can access it securely.**                                   | ✅         | ✅                |
| As a **user** I can **sign up and log in** so that **I can reserve books.**                                                                         | ✅         | ✅                |
| As an **administrator** I can **access protected management pages** so that **only authorized roles can modify catalog and view all reservations.** | ✅         | ✅                |
| As a **visitor** I can **browse available books with their authors** so that **I can decide what to reserve.**                                      | ✅         | ✅                |
| As an **administrator** I can **create and edit authors** so that **catalog metadata stays accurate.**                                              | ✅         | ✅                |
| As an **administrator** I can **create, edit, and delete books** so that **I can maintain the reservable catalog.**                                 | ✅         | ✅                |
| As a **signed‑in user** I can **see my session state in the header (profile/logout)** so that **I can navigate confidently.**                       | ✅         | ✅                |
| As a **user** I can **view only available books** so that **I don’t attempt to reserve an unavailable item.**                                       | ✅         | ✅                |
| As a **user** I can **reserve an available book** so that **I can secure it for a short period.**                                                   | ✅         | ✅                |
| As a **user** I can **view and cancel my active reservations** so that **I can manage my bookings.**                                                | ✅         | ✅                |
| As **the system** I can **enforce at most one active reservation per book** so that **double booking is impossible.**                               | ✅         | ✅                |
| As a **user** I can **see clear validation and error messages on forms** so that **I can correct mistakes easily.**                                 | ✅         | ✅                |
| As **the system** I can **run business‑rule checks (availability and duplicate active reservation)** so that **data integrity is maintained**       | ✅         | ✅                |
| As a **keyboard user** I can **navigate with visible focus** so that **the app is operable without a mouse.**                                       | ✅         | ✅                |
| As a **screen‑reader user** I can **get correctly labeled fields, headings, and feedback** so that **I can complete tasks effectively.**            | ✅         | ✅                |
| As a **mobile user** I can **use responsive layouts** so that **pages remain usable on small screens.**                                             | ✅         | ✅                |
| As a **user** I can **receive clear notifications about data changes** so that **I stay informed.**                                                 | ✅         | ✅                |
| As a **maintainer** I can **run a test suite for key flows** so that **quality is verifiable before deployment.**                                   | ⚠️ Partial | ⚠️ Partial        |
| As a **maintainer** I can **use Git and GitHub** so that **progress is traceable and documented.**                                                  | ✅         | ✅                |
| As a **product owner** I can **deploy the app to a cloud platform** so that **end users can access it securely.**                                   | ✅         | ✅                |

## 🚀 Deployment to Heroku

Follow these steps to deploy your Django project to **Heroku**:

### 1. Create a Heroku account

-   Sign up at [Heroku](https://www.heroku.com/) if you don’t have an account.

### 2. Create a new app

-   Click **“New” → “Create new app”**.
-   Give your app a name and select the closest region to you.

### 3. Set up the database with ElephantSQL

-   Create an account at [ElephantSQL](https://www.elephantsql.com/).
-   Click **“Create instance”**.
-   Name your database, select a plan, and choose a region/data-center.
-   Copy the **DATABASE_URL** from the dashboard.

### 4. Configure environment variables

-   Paste the **DATABASE_URL** into **Heroku Config Vars** under **Settings → Config Vars**.
-   Ensure your local `env.py` file uses the same URL.
-   All environment variables should match between Heroku and your local IDE.

### 5. Create a Procfile

-   In your project root, create a file named `Procfile` with the following content:

```text
web: gunicorn project_name.wsgi
```

### 6. Add environment variables to Heroku

-   Add all variables from your `env.py` file to Heroku’s **Config Vars** under **Settings → Config
    Vars**.

### 7. Update Django settings

-   Set `DEBUG = False` in `settings.py`.
-   Add the following to `ALLOWED_HOSTS` in `settings.py`:

```python
ALLOWED_HOSTS = ['localhost', 'project_name.herokuapp.com']
```

### 8. Run migrations and create superuser(if you havent created yet)

-   Check migration status:

```bash
python3 manage.py showmigrations
```

-   Apply migrations to the database:

```bash
python3 manage.py migrate
```

Create an admin user:

```bash
python3 manage.py createsuperuser
```

### 9. Connect to GitHub and deploy

-   Link your repository to Heroku.

-Enable automatic deploys from the main branch or deploy manually.

-   Click Deploy to launch your application on Heroku.

## Acknowledgments

I would like to express my gratitude to everyone who supported and guided me throughout the
development of this project. Special thanks to:

-   **Naz**, for always being there and helping me whenever I needed assistance.
-   The Code Institute community, for inspiration and guidance.
-   All mentors, peers, and contributors who provided valuable advice and feedback.
