# Waitlist Application

The `waitlist` app is the central component of the shareBear project, responsible for collecting student interest.

## Features

- **User Interest Form:** Captures student email, name, intent (Buy, Sell, or Both), and academic year.
- **Email Validation:** Restricts registration to `@baylor.edu` email addresses.
- **Duplication Prevention:** Ensures unique emails on the waitlist.
- **User Interface:** Features a responsive modal form on the homepage.

## Core Components

### `WaitlistEntry` Model

The `WaitlistEntry` model stores all the captured user information.

- `email`: Unique email address.
- `first_name`: User's first name.
- `last_name`: User's last name.
- `intent`: One of `BUY`, `SELL`, or `BOTH`.
- `year`: The user's academic year (Freshman through Graduate).

### `WaitlistEntryForm`

A Django `ModelForm` that handles data validation and sanitization.

- Normalizes email addresses to lowercase.
- Custom validation ensures all emails end with `@baylor.edu`.

### `home` View

The view logic handles both displaying the homepage and processing form submissions.

- Validates and saves waitlist entries.
- Displays success or error messages to the user using Django's `messages` framework.
