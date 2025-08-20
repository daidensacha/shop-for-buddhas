🪷 Shop for Buddhas
===================

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Django](https://img.shields.io/badge/Django-3.2-092E20?logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/Postgres-13-4169E1?logo=postgressql&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-Payments-008CDD?logo=stripe&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS-S3-FF9900?logo=stripe&logoColor=white)

<https://www.djangoproject.com/> <https://www.python.org/> [LICENSE](LICENSE)

An **e-commerce web app** built with **Django**.
Originally deployed with **Heroku + AWS S3 + Stripe**, now simplified to run **locally with SQLite**.

✨ Features: - Browse products (fixtures included 🛍️) - Product categories & images - User accounts (login/register) - Cart & checkout flow (Stripe removed in this version) - Blog & testimonials

📸 Screenshots
--------------

🚀 Getting Started
------------------

Clone the repo and set up your environment:
> ⚠️ Make sure to use the same Python version that this project was developed with (Python 3.9).
> Newer versions (e.g., 3.12, 3.13) may cause dependency errors with some packages.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ bash
git clone https://github.com/daidensacha/shop-for-buddhas.git
cd shop-for-buddhas

# Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate   # (Mac/Linux)
venv\Scripts\activate      # (Windows)

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

⚙️ Configuration
---------------

Create an `env.py` file in the project root:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ python
import os

os.environ["SECRET_KEY"] = "your-secret-key"
os.environ["DEBUG"] = "True"
os.environ["DEVELOPMENT"] = "True"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

⚠️ No AWS/Stripe/Heroku configuration is required --- this setup uses **SQLite** for simplicity.

📂 Database Setup
-----------------

Run migrations and load fixtures:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ bash
python manage.py makemigrations
python manage.py migrate

# Create a superuser for admin login
python manage.py createsuperuser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load categories & products:
# Order is important!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ bash
python manage.py loaddata products/fixtures/categories.json
python manage.py loaddata products/fixtures/products.json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

▶️ Run the Server
----------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ bash
python manage.py runserver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visit <http://127.0.0.1:8000>.

🧰 Tech Stack
-------------

-   **Backend**: Django 3.2.8

-   **Database**: SQLite (local)

-   **Frontend**: Django templates + Bootstrap

-   **Auth**: Django Allauth

-   **Other**: Crispy Forms, Taggit

📜 License
----------

This project is licensed under the [MIT License](LICENSE).

🙏 Acknowledgements
-------------------

-   Built during my **Diploma of Software Development course (2021)**

![License](https://img.shields.io/github/license/daidensacha/shop-for-buddhas)
![Last Commit](https://img.shields.io/github/last-commit/daidensacha/shop-for-buddhas)
![Open Issues](https://img.shields.io/github/issues/daidensacha/shop-for-buddhas)
![Tech](https://img.shields.io/badge/stack-Python%20%7C%20Django%20%7C%20Postgres-blue)

-   Refreshed in 2025 with simplified local setup
