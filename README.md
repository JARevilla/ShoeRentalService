# Bowling Shoes Rental Service for Kode Across Technical Examination

Description: This is a backend service for bowling shoes rental. It has the following
features as listed below.

- `Customer Management` - Add and retrieve customer records.
- `Shoe Rental Management` - Manage shoe rentals, including recording rental dates and fees.
- `Discount Calculation` - Calculate and apply discounts using an LLM model.
- `Database` - Managed and stored with Supabase.
- `Containerization` - Docker setup for easy deployment.

## Instructions

1. Cloning the repository:
    ```sh
    git clone <repository_url>
    cd bowling_shoes_rental_service
    ```
2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up environment variables:
    ```sh
    export SUPABASE_URL=<your_supabase_url>
   export SUPABASE_API_KEY = <your_supabase_API_KEY>
    export OPENAI_API_KEY=<your_openai_api_key>
    ```
5. Initialize the database:
    ```sh
    python -m app.database
    ```
6. Run the application:
    ```sh
    uvicorn app.main:app --reload
    ```
   
## API Endpoints

- `POST /customers/` - Create a new customer
- `GET /customers/` - List all customers
- `POST /rentals/` - Create a new rental and calculate the discount
- `GET /rentals/` - List all rentals

## Design Choices

- **FastAPI** for building a modern, fast (high-performance) web framework.
- **SQLAlchemy** for ORM and managing database interactions.
- **Supabase** as the database service.
- **OpenAI** for integrating a language model to determine discounts.
- **Docker** for containerizing the application.

## Containerization

1. Build and run the Docker container:
    ```sh
    docker-compose up --build
    ```

## Notes

- Ensure that your environment variables are set correctly for Supabase and OpenAI.
