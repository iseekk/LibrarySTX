# Using LibrarySTX's API

You can perform a volumes search by sending an HTTP GET request to the following URI:

        http://127.0.0.1:8000/api/

The request may have the following parameters:

        title
        authors
        language
        initial_date
        final_date

Examples:

        http://127.0.0.1:8000/api/?title=hobbit
        http://127.0.0.1:8000/api/?initial_date=2010-01-01
