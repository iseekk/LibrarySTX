from books.models import Book
import urllib
import json
import re


def download_book_data(keyword, idx):
    url = f"https://www.googleapis.com/books/v1/volumes?q={keyword}&startIndex={idx}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    search_results = []
    for book in data["items"]:
        date = book["volumeInfo"]["publishedDate"] \
            if "publishedDate" in book["volumeInfo"].keys() else ""
        if re.compile(r"^\d{4}\-(0[1-9]|1[012])$").match(date) is not None:
            date = f"{date}-01"
        elif re.compile(r"^\d{4}$").match(date) is not None:
            date = f"{date}-01-01"

        if "industryIdentifiers" in book["volumeInfo"]:
            for i in book["volumeInfo"]["industryIdentifiers"]:
                if "ISBN_13" in i.values():
                    isbn = i["identifier"]
                    break
                elif "ISBN_10" in i.values():
                    isbn = i["identifier"]
                else:
                    isbn = ""
        else:
            isbn = ""

        result = {
            "title": book["volumeInfo"]["title"]
            if "title" in book["volumeInfo"].keys() else "",

            "authors": ", ".join(
                [str(a) for a in book["volumeInfo"]["authors"]]
            )[::-1].replace(",", "i ", 1)[::-1]
            if "authors" in book["volumeInfo"].keys() else "",

            "publishedDate": date,

            "isbn": isbn,

            "pageCount": str(book["volumeInfo"]["pageCount"])
            if "pageCount" in book["volumeInfo"].keys() else "",

            "thumbnail": book["volumeInfo"]["imageLinks"]["thumbnail"]
            if "imageLinks" in book["volumeInfo"] else "",

            "language": book["volumeInfo"]["language"].upper()
            if "language" in book["volumeInfo"].keys() else "",

            "exists": True if isbn and Book.objects.filter(isbn__exact=isbn)
                           else False,
        }

        search_results.append(result)

        total_items = data["totalItems"] if data["totalItems"] else None

    return search_results, total_items
