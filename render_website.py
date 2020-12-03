import json
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked
from dotenv import load_dotenv




def get_list_from_json(json_path):
    with open(json_path, "r") as my_file:
        books_json = my_file.read()
    return json.loads(books_json)


def write_page(rendered_page, page_number, folder):
    page_path = os.path.join(folder, f'index{page_number}.html')
    with open(page_path, 'w', encoding="utf8") as file:
        file.write(rendered_page)


def make_page_content(quantity_on_page: int, books: list, template, directory):
    books_on_pages = list(chunked(books, quantity_on_page))
    for page, books_on_page in enumerate(books_on_pages, 1):
        books_separated_to_columns = list(chunked(books_on_page, 2))
        rendered_page = template.render(books=books_separated_to_columns, current_page=page, pages_quantity=len(books_on_pages))
        write_page(rendered_page, page, directory)


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    load_dotenv()
    os.getenv('SOURCE_JSON', default='SOURCE_JSON')
    directory = 'pages'
    template = env.get_template('template.html')
    books = get_list_from_json(source)
    os.makedirs(directory, exist_ok=True)
    make_page_content(20, books, template, directory)


if __name__ == "__main__":
    on_reload()

