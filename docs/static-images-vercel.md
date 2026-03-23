# Static Image Rendering on Vercel

This document explains how static images, such as the Baylor logo in the header, are rendered and served when the application is deployed on Vercel.

## 1. Django Template Usage

In the Django templates (e.g., `market_app/templates/main/base.html`), static images are referenced using the `{% static %}` template tag.

```html
{% load static %}
...
<img src="{% static 'images/baylor-logo.png' %}" alt="Baylor University Logo">
```

The `{% static %}` tag prefixes the path with the value of `STATIC_URL` defined in `main/settings.py`.

## 2. Django Configuration (`main/settings.py`)

The following settings govern how Django handles static files:

*   **`STATIC_URL = 'static/'`**: The URL prefix used when referring to static files.
*   **`STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"`**: The absolute path to the directory where `collectstatic` will collect static files for deployment.
*   **`WhiteNoiseMiddleware`**: Included in `MIDDLEWARE` to allow Django to serve its own static files, though Vercel's edge network often takes precedence based on `vercel.json` routing.

## 3. Vercel Build Process (`build.sh` & `vercel.json`)

Vercel uses a two-step build process configured in `vercel.json`:

1.  **Build Execution**: Vercel runs `build.sh` using the `@vercel/static-build` builder.
2.  **`collectstatic`**: Inside `build.sh`, the command `python manage.py collectstatic --noinput --clear` is executed.
    *   This command gathers all static assets from individual app directories (like `market_app/static/`) and places them into the `STATIC_ROOT` directory (`staticfiles_build/static`).
3.  **Deployment Directory**: The `vercel.json` file specifies `"distDir": "staticfiles_build"`. This tells Vercel that the output of the static build is located in that folder.

## 4. Serving the Images

When a user requests an image (e.g., `/static/images/baylor-logo.png`):

*   **Routing**: `vercel.json` contains a route configuration:
    ```json
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    }
    ```
*   **Edge Serving**: Vercel's edge network detects the request matches the `/static/` pattern and serves the file directly from the `static/` directory inside the deployed `distDir` (`staticfiles_build/static/`).

This ensures that static images are served efficiently by Vercel's CDN rather than being processed by the Python/Django runtime.
