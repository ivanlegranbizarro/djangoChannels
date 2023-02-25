# Chat en tiempo real con Django Channels

Este proyecto es un chat en tiempo real hecho con Django y django-channels utilizando sockets. Los usuarios pueden registrarse, loguearse, crear diferentes canales y chatear en tiempo real. Las rutas están protegidas para los usuarios logueados y, además, los distintos usuarios cuentan con coloreado distinto en el username para que sea más fácil distinguir sus mensajes de otros usuarios en el chat.


## Características

- Registro y autenticación de usuarios
- Creación de diferentes canales para chatear
- Protección de rutas para usuarios logueados
- Coloreado distinto de usernames para distinguir mensajes de distintos usuarios
- Envió de mensajes en tiempo real con sockets

## Tecnologías utilizadas

- Django
- Django-channels
- JavaScript
- TailwindCSS

## Instalación

1. Clonar el repositorio

`git clone https://github.com/ivanlegranbizarro/djangoChannels.git`


2. Instalar dependencias

`cd djangoChannels`
`pip install -r requirements.txt`


3. Ejecutar migraciones de Django

`python manage.py migrate`


4. Ejecutar servidor de Django

`python manage.py runserver`


## Créditos

Este chat fue construido como variación de un tutorial de internet, [aquí](https://www.youtube.com/watch?v=SF1k_Twr9cg&t=1710s) se encuentra el enlace del tutorial original.

