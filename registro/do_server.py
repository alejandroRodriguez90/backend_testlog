import json
import http.server
from models.user import cursor, insert_user
from registro.register import get_user


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = json.loads(post_data)  # Convertir los datos del cuerpo a JSON
        print(params)

        if 'name' in params and 'email' in params:
            name = params['name']
            email = params['email']

            if get_user(email):
                response_message = "El correo ya existe"
            else:
                insert_user(name, email)
                response_message = "Usuario creado correctamente"
        else:
            response_message = "Falta el nombre o el correo electrónico en la solicitud"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_message.encode('utf-8'))


def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()


run()
