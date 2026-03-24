# Project Overview

**SHARE Bear** is a Django-based application built to manage a waitlist for students at Baylor University. The project focuses on providing a simple, user-friendly interface for students interested in buying, selling, or both, as they navigate their university experience.

## Technology Stack

The project uses the following modern technology stack:

### Backend
- **Framework:** [Django 6.0+](https://www.djangoproject.com/) — A high-level Python web framework.
- **Database:** [PostgreSQL](https://www.postgresql.org/) (hosted on [Supabase](https://supabase.com/)).
- **Database Connector:** `dj-database-url` and `psycopg2-binary` for connecting to PostgreSQL.
- **Media Storage:** Integrated with Supabase via S3-compatible storage.
- **Environment Management:** `python-dotenv` for local environment variable management.

### Frontend
- **Templating:** Django Templates with a `base.html` structure.
- **Styling:** Vanilla CSS for simplicity and ease of modification.
- **Interactivity:** Minimal JavaScript used for handling the modal UI on the homepage.

### Infrastructure & Deployment
- **Hosting:** [Vercel](https://vercel.com/) — Fast, serverless deployment for Python/Django.
- **WSGI:** Standard WSGI interface for production.
- **Static Assets:** [WhiteNoise](http://whitenoise.evans.io/en/stable/) for serving static files efficiently from Django.
