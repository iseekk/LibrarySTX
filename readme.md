# First launch

Create a secret_key.txt file with your django secret key and add it to .gitignore file

Make sure you make a database using:
        python manage.py makemigrations
and
        python manage.py migrate

# Using LibrarySTX's API

You can perform a volumes search by sending an HTTP GET request to the following URI:

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
