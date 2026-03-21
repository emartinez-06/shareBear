# Supabase Integration

The project leverages Supabase for its backend data storage and management.

## Database (PostgreSQL)

The primary data store is a PostgreSQL database hosted by Supabase.

### Connection Logic

- Django connects to the database via the `DATABASE_URL` environment variable.
- The `dj-database-url` library is used in `shareBear/settings.py` to parse this URL into the standard Django `DATABASES` configuration.

```python
# shareBear/settings.py
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=not DEBUG
    )
}
```

### Migrations

Standard Django migrations are used to manage the schema within the Supabase database. These can be applied with `python manage.py migrate`.

## Storage (S3-Compatible)

The project includes dependencies (`django-storages`, `boto3`) to support S3-compatible storage through Supabase.

### Environment Variables

The following environment variables are used to facilitate storage:
- `SUPABASE_S3_ACCESS_KEY`: Access key for Supabase storage API.
- `SUPABASE_S3_SECRET_KEY`: Secret key for Supabase storage API.

Currently, the project uses local storage as the default, but it is configured with the necessary dependencies for easy migration to Supabase Storage if needed.
