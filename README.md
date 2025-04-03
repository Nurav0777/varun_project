Tech Stack

Python (Flask framework)

Flask-SQLAlchemy (Database ORM)

SQLite (Default database, can be replaced with PostgreSQL/MySQL)

Flask-JWT-Extended (Authentication)

Flask-Bcrypt (Password hashing)

🔧 Setup Instructions

1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Initialize the Database

python app.py

3️⃣ Run the Server

python app.py

The server will start at http://127.0.0.1:5000/

🚀 API Endpoints

🧑 User Authentication

Method

Endpoint

Description

POST

/register

Register a new user

POST

/login

Login and get JWT token

🛒 Product Management

Method

Endpoint

Description

GET

/products

Fetch all products

POST

/products

Add a new product

🛍 Shopping Cart

Method

Endpoint

Description

POST

/cart/add

Add product to cart

POST

/cart/remove

Remove product from cart

✅ Order Checkout

Method

Endpoint

Description

POST

/checkout

Mock checkout process

🔐 Security Features

JWT Authentication using Flask-JWT-Extended

Password Hashing using Flask-Bcrypt

Authentication Decorators for secured endpoints

📌 Key Concepts Implemented

OOP Principles (Encapsulation, Abstraction, etc.)

Abstraction (Separated services and controllers)

Decorators (Used for authentication handling)

Exception Handling (Handled API errors gracefully)