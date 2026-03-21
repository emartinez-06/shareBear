# Deployment and Configuration

The project is designed to be easily deployed to [Vercel](https://vercel.com/) with a few configurations.

## Local Setup

To set up the project locally:

1.  **Clone the Repository.**
2.  **Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment Variables:**
    - Copy `.env.example` to `.env`.
    - Fill in the required variables (`SECRET_KEY`, `DATABASE_URL`, etc.).
5.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```

## Vercel Deployment

The project is pre-configured for Vercel using the `vercel.json` file.

### Environment Variables on Vercel

Ensure the following environment variables are set in your Vercel project dashboard:
- `SECRET_KEY`
- `DATABASE_URL` (your Supabase PostgreSQL connection string)
- `DEBUG` (set to `False` for production)
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`

### Static Files

Vercel serves static files using [WhiteNoise](http://whitenoise.evans.io/). No extra configuration is needed for static assets to be served during production.
