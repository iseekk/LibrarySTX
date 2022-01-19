# First launch

Create **secret_key.txt** file with your django secret key and add it to **.gitignore** file.

Make sure you create a database using:

        python manage.py makemigrations

and

        python manage.py migrate

# Deploying LibrarySTX to production

In **LibrarySTX/settings.py** set **DEBUG** to **False**, uncomment **STATIC_ROOT** and enter your domain as string to **ALLOWED_HOSTS**. Then run:

        python manage.py collectstatic

# Using LibrarySTX's API

You can perform a volumes search by sending an HTTP GET request to the following URL:

        http://127.0.0.1:8000/api/books

The request may have the following parameters:

        title
        authors
        language
        initial_date
        final_date

Examples:

        http://127.0.0.1:8000/api/books?title=hobbit
        http://127.0.0.1:8000/api/books?initial_date=2010-01-01
