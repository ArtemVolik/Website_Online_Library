import json
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked
from dotenv import load_dotenv
from livereload import Server
import glob


def get_list_from_json(json_path):
    with open(json_path, "r") as my_file:
        books_json = my_file.read()
    return json.loads(books_json)


def write_page(rendered_page, page_number, folder):
    page_path = os.path.join(folder, f'index{page_number}.html')
    with open(page_path, 'w', encoding="utf8") as file:
        file.write(rendered_page)
    return page_path


def make_page_content(quantity_on_page: int, books: list, template, directory):
    rendered_pages_pathes = set()
    books_on_pages = list(chunked(books, quantity_on_page))
    columns_quantity = 2
    for page, books_on_page in enumerate(books_on_pages, 1):
        books_separated_to_columns = list(chunked(books_on_page, columns_quantity))
        rendered_page = template.render(books=books_separated_to_columns,
                                        current_page=page,
                                        pages_quantity=len(books_on_pages))
        rendered_pages_pathes.add(write_page(rendered_page, page, directory))
    return rendered_pages_pathes


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    load_dotenv()
    source = os.getenv('SOURCE_JSON', default='books_info.json')
    directory = 'pages'
    template = env.get_template('template.html')
    books = get_list_from_json(source)
    os.makedirs(directory, exist_ok=True)
    quantity_on_page = 26
    old_pages = set(glob.glob('*/index*.*'))
    new_pages = make_page_content(quantity_on_page, books, template, directory)
    pages_to_delete = old_pages - new_pages
    for page in pages_to_delete:
        os.remove(page)


if __name__ == "__main__":
    on_reload()
    server = Server()
    server.watch('template.html', on_reload)
    server.serve(host='127.0.0.1', port=5050)
