# Changelog

## 2026-03-09: Initial Setup of Custom User Model

**Summary:** 
Created a custom `User` model to replace the default Django `User` model in preparation for the application's unique user requirements (intent tracking, classification, and a referral program).

**Changes Made:**
1.  **New App Creation (`users`):**
    *   Created a new Django app named `users` using `python manage.py startapp users` to maintain a clean separation of concerns.
2.  **Custom `User` Model (`users/models.py`):**
    *   Inherited from `django.contrib.auth.models.AbstractUser`.
    *   Set `USERNAME_FIELD = 'email'` (and added `username` to `REQUIRED_FIELDS`) so that users log in with their email address, while retaining the `username` for display purposes.
    *   **New Fields Added:**
        *   `email`: Enforced as unique.
        *   `intent`: A choice field (`BUY`, `SELL`, `BOTH`) for analytics tracking.
        *   `classification`: A choice field (`FRESHMAN`, `SOPHOMORE`, `JUNIOR`, `SENIOR`) representing the student's academic standing.
        *   `referral_code`: An automatically generated, unique 8-character string for users to share.
        *   `referred_by`: A self-referential foreign key allowing a user to be linked to the person who invited them.
    *   **Properties Added:**
        *   `referral_count`: A property that dynamically counts how many users this user has directly referred (`user.referrals.count()`).
3.  **Project Configuration (`shareBear/settings.py`):**
    *   Added the `users` app to `INSTALLED_APPS`.
    *   Set `AUTH_USER_MODEL = 'users.User'` to tell Django to use our custom user model globally.
4.  **Admin Integration (`users/admin.py`):**
    *   Subclassed `django.contrib.auth.admin.UserAdmin`.
    *   Exposed the custom fields (`intent`, `classification`, `referral_code`, `referred_by`, `referral_count`) in the Django admin interface for easy management and visibility.

**Action Required (Database Reset):**
Because the standard `auth.User` model had already been migrated (Django defaults), switching `AUTH_USER_MODEL` midway requires the database to be flushed or recreated. Since you are using Supabase, you must drop the existing tables or flush the database entirely before applying the newly generated migrations for the `users` app.
