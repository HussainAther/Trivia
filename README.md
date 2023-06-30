# Trivia RESTful API

Glitch link: https://glitch.com/edit/#!/foil-universal-revolve?path=README.md%3A1%3A0

This project is a full-featured CRUD RESTful Web API for Trivia information. It allows users to register, log in, and manage collections of trivia questions and answers. The API is built using Flask and PostgreSQL as the database.

## Installation and Setup

1. Clone the repository to your local machine:
   ```
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```
   cd trivia-api
   ```

3. Create a virtual environment named `trivia-env`:
   - For Windows:
     ```
     python -m venv trivia-env
     trivia-env\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     python3 -m venv trivia-env
     source trivia-env/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up the PostgreSQL database:
   - Install PostgreSQL on your machine if you haven't already.
   - Create a new PostgreSQL database for the project.
   - Update the `SQLALCHEMY_DATABASE_URI` in the `app.py` file with your database connection details.

6. Run the database migrations:
   ```
   flask db upgrade
   ```

## Usage

1. Activate the virtual environment:
   - For Windows:
     ```
     trivia-env\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source trivia-env/bin/activate
     ```

2. Start the Flask development server:
   ```
   flask run
   ```

3. The API will be accessible at `http://localhost:5000`.

4. Use a tool like Postman or cURL to interact with the API endpoints.

## API Documentation

The API has the following endpoints:

- `/register` - Register a new user.
- `/login` - Log in an existing user.
- `/logout` - Log out the current user.
- `/trivia` - Get all trivia collections for the logged-in user.
- `/trivia/<trivia_id>` - Get details of a specific trivia collection.
- `/trivia` - Create a new trivia collection.
- `/trivia/<trivia_id>` - Update a trivia collection.
- `/trivia/<trivia_id>` - Delete a trivia collection.

Please refer to the API documentation for detailed information on request/response formats and authentication.

## License

This project is licensed under the [MIT License](LICENSE).
