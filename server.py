from livereload import Server
from render_website import on_reload


server = Server()
server.watch('template.html', on_reload)
server.serve(host='127.0.0.1', port=5050)