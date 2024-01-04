from db_models import Author, Quote
from mongoengine.errors import NotUniqueError

import json


def seed_authors(filename: str):
    with open(filename, "r", encoding="utf-8") as fd:
        data = json.load(fd)
        for el in data:
            try:
                author = Author(
                    fullname=el.get("fullname"),
                    born_date=el.get("born_date"),
                    born_location=el.get("born_location"),
                    description=el.get("description"),
                )
                author.save()
            except NotUniqueError:
                print(f'Author "{el.get("fullname")}" already exists')


def seed_quotes(filename: str):
    with open(filename, "r", encoding="utf-8") as fd:
        data = json.load(fd)
        for el in data:
            author = Author.objects(fullname=el.get("author")).first()
            if not author:
                print(f'Author "{el.get("author")}" not found')
                continue
            try:
                quote = Quote(
                    author=author,
                    tags=el.get("tags"),
                    quote=el.get("quote"),
                )
                quote.save()
            except NotUniqueError:
                print(f'Quote "{el.get("quote")}" already exists')


if __name__ == "__main__":
    seed_authors("authors.json")
    seed_quotes("quotes.json")
