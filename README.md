# PelikulaDB Backend

The backend of **PelikulaDB** is built using **Django REST Framework (DRF)**. It provides a robust API for managing movies, users, reviews, and payments. The backend integrates with **Stripe** for secure payment processing and uses **PostgreSQL** as the database.

---

## Features

- **User Authentication**: Secure registration and login using Django's authentication system.
- **Movie Management**: CRUD operations for movies (user-specific and admin-approved).
- **Review and Rating System**: Users can write reviews and rate movies.
- **Payment Integration**: Process payments using Stripe.
- **Admin Dashboard**: Manage movies, users, reviews, and payments.
- **Advanced Search**: Filter movies by title, genre, year, etc.

---

## Tech Stack

- **Django REST Framework (DRF)**: For building RESTful APIs.
- **PostgreSQL**: Relational database for storing data.
- **Stripe**: For payment processing.
- **Docker**: For containerization (optional).

---

## Getting Started

### Prerequisites
- Python 3.x
- PostgreSQL
- Stripe API keys

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/PelikulaDB.git
   cd PelikulaDB/backend
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root of the `backend` directory with the following:
     ```
     SECRET_KEY=your-django-secret-key
     DATABASE_URL=your-postgres-db-url
     STRIPE_SECRET_KEY=your-stripe-secret-key
     STRIPE_PUBLIC_KEY=your-stripe-public-key
     ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the API:**
   - Visit `http://localhost:8000` in your browser or use tools like Postman.

---

## API Endpoints

### Movies
- `GET /api/movies/`: List all movies.
- `POST /api/movies/`: Add a new movie (user/admin only).
- `GET /api/movies/{id}/`: Retrieve a specific movie.
- `PUT /api/movies/{id}/`: Update a movie (user/admin only).
- `DELETE /api/movies/{id}/`: Delete a movie (user/admin only).

### Reviews
- `GET /api/reviews/`: List all reviews.
- `POST /api/reviews/`: Add a new review.
- `GET /api/reviews/{id}/`: Retrieve a specific review.
- `PUT /api/reviews/{id}/`: Update a review.
- `DELETE /api/reviews/{id}/`: Delete a review.

### Payments
- `POST /api/payments/`: Process a payment via Stripe.

---

## Folder Structure

```
backend/
├── pelikula/          # Django project settings
├── api/               # DRF app (movies, reviews, payments)
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
└── .env               # Environment variables
```

---

## Available Commands

- `python manage.py runserver`: Start the development server.
- `python manage.py migrate`: Apply database migrations.
- `python manage.py createsuperuser`: Create an admin user.

---

## Deployment

### Using Docker
1. Build the Docker image:
   ```bash
   docker-compose build
   ```
2. Run the Docker container:
   ```bash
   docker-compose up
   ```

### Using Render/Heroku
- Follow the platform-specific guides for deploying Django applications.

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
