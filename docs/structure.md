# Project Structure

The project follows a standard Django project layout with some specific customizations for Vercel and Supabase.

## Directory and File Breakdown

- **`.github/`**: Configuration for GitHub actions (e.g., CI/CD).
- **`.venv/`**: Python virtual environment containing the project's dependencies.
- **`assets/`**: Project assets such as logos and brand images.
- **`docs/`**: Documentation files for the project.
- **`shareBear/`**: The SHARE Bear project configuration folder.
  - `settings.py`: SHARE Bear project settings, including Supabase database and storage configuration.
  - `urls.py`: Main URL routing for the project.
  - `wsgi.py` / `asgi.py`: Entry points for web server interfaces.
- **`templates/`**: Global templates used by the project.
  - `base.html`: Base template providing the layout for other pages.
  - `home.html`: Homepage template featuring the waitlist join modal.
- **`waitlist/`**: A Django app dedicated to managing the waitlist entries.
  - `models.py`: Defines the `WaitlistEntry` model.
  - `views.py`: Logic for the homepage and waitlist form submission.
  - `forms.py`: Django form for validating and processing waitlist entries.
  - `urls.py`: URL routing specific to the waitlist app.
- **`manage.py`**: Django management command-line utility.
- **`.env.example`**: Template for environment variables needed for development and production.
- **`requirements.txt`**: List of all Python dependencies.
- **`vercel.json`**: Configuration for deploying the project to Vercel.
- **`.tool-versions`**: Specifies tool versions for local development (e.g., via `asdf`).
