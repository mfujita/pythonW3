# Django Create Project
# My First Project
# Criando um projeto chamado my_tennis_club no ambiente virtual myworld
# django-admin startproject my_tennis_world
'''
27/08/2024  23:11               421 asgi.py
27/08/2024  23:11             3.366 settings.py
27/08/2024  23:11               792 urls.py
27/08/2024  23:11               421 wsgi.py
27/08/2024  23:11                 0 __init__.py
'''

# Run the Django Project
# Vá até /my_tennis_club e execute o comando
'''
C:\github\Django\Django Tutorial\myworld\my_tennis_club>py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 27, 2024 - 23:15:10
Django version 5.1, using settings 'my_tennis_club.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
'''

# Ao digital localhost:8000 no navegador retorna no ambiente virtual:
'''
[27/Aug/2024 23:15:53] "GET / HTTP/1.1" 200 12068
Not Found: /favicon.ico
[27/Aug/2024 23:15:54] "GET /favicon.ico HTTP/1.1" 404 2216
'''

# Porém o navegador mostra que o Django foi instalado com sucesso.