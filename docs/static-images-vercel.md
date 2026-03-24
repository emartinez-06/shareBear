# Static Image Rendering on Vercel

This document explains how static images, such as the Baylor logo in the header, are rendered and served when the application is deployed on Vercel using WhiteNoise.

## 1. Django Template Usage

In the Django templates (e.g., `templates/base.html`), static images are referenced using the `{% static %}` template tag.

```html
{% load static %}
...
<img src="{% static 'images/bearLogo.png' %}" alt="SHARE Bear Logo">
```

The `{% static %}` tag prefixes the path with the value of `STATIC_URL` defined in `shareBear/settings.py`.

## 2. Django Configuration (`shareBear/settings.py`)

The following settings govern how Django and WhiteNoise handle static files to ensure they work reliably in Vercel's serverless environment:

*   **`STATIC_URL = '/static/'`**: The URL prefix used when referring to static files.
*   **`STATIC_ROOT = BASE_DIR / 'staticfiles_build'`**: The directory where `collectstatic` gathers files. We use `staticfiles_build` because it is NOT ignored by `.gitignore` (unlike `staticfiles/`), ensuring Vercel includes it in the deployment.
*   **`WhiteNoiseMiddleware`**: Added to `MIDDLEWARE` to serve static files directly from the Python/Django runtime.
*   **`WHITENOISE_USE_FINDERS = True`**: A robust fallback that allows WhiteNoise to search source directories (like `static/`) if a file is missing from `STATIC_ROOT`.
*   **`WHITENOISE_MANIFEST_STRICT = False`**: Ensures the app doesn't crash with a 500 error if a static file or manifest entry is missing; it will gracefully fall back to the unhashed file.
*   **Storage Backend**: We use `whitenoise.storage.CompressedStaticFilesStorage`. This provides compression without the strict manifest requirements of the `Manifest` version, preventing "Missing manifest entry" errors.

## 3. Vercel Build Process (`build_files.sh` & `vercel.json`)

Vercel uses a build process configured in `vercel.json`:

1.  **Build Execution**: Vercel runs `build_files.sh`.
2.  **`collectstatic`**: Inside `build_files.sh`, the command `python manage.py collectstatic --noinput --clear` is executed to gather and compress all assets.

## 4. Serving the Images

Unlike traditional deployments that might use Nginx or Vercel's edge routing for `/static/`, we let **WhiteNoise** handle all static file requests through the Django application.

*   **Routing**: `vercel.json` is simplified to route all requests to the WSGI application:
    ```json
    "routes": [
      {
        "src": "/(.*)",
        "dest": "shareBear/wsgi.py"
      }
    ]
    ```
*   **Reliability**: This approach is more reliable on Vercel because it doesn't depend on the edge network correctly mapping the transient `STATIC_ROOT` directory. WhiteNoise effectively "bundles" the static files with the application code.

This setup ensures that static images render correctly on both localhost and Vercel without triggering 500 errors.
