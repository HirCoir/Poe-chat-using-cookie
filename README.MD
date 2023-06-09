Este chatbot es capaz de interactuar con los bots de poe.com mediante el uso de cookies. Es capaz de enviar mensajes y recibir respuestas de los diferentes bots de poe.com.


![Interfaz de usuario del chat](https://raw.githubusercontent.com/HirCoir/Poe-chat-using-cookie/main/web.PNG)

![Respuesta del chat](https://github.com/HirCoir/Poe-chat-using-cookie/blob/main/web-respuesta.PNG)

![Procesando mensaje del chat](https://github.com/HirCoir/Poe-chat-using-cookie/blob/main/web-procesando.PNG)
![Procesando mensaje del chat](https://github.com/HirCoir/Poe-chat-using-cookie/blob/main/datos.PNG)

## Módulos PIP necesarios

- Flask
- collections
- pymysql
- html
- poe-api
- logging
- sys
- random
- concurrent.futures
```pip install Flask pymysql poe-api```

## Características

- Almacena los mensajes anteriores en una base de datos para dar una respuesta más rápida en caso de que alguien haga la misma consulta.
- Utiliza hilos para enviar y recibir mensajes del bot de poe.com.
- Si se produce un error al procesar una solicitud, muestra un mensaje de error.
- Puede ser personalizado mediante la definición del id del bot en el que se desea interactuar.
- El rol del bot puede ser personalizado mediante la definición de una variable "rol_bot".
- Respuestas del bot de poe.com se muestran en el chat junto con los mensajes anteriores.
- El botón de enviar se bloquea para evitar procesar la misma información dos veces.
- El chatbot fue creado 100% usando Chat GPT 3.5 y openassistant.io

## Cómo utilizar el chatbot

1. Asegúrate de tener instalados los módulos PIP necesarios.
2. Ejecuta el archivo Python en tu consola.
3. Accede a la página web del chatbot en tu navegador.
4. Escribe tu mensaje en el campo de texto y presiona "Enter" para enviarlo.
5. Espera a recibir la respuesta del bot de poe.com.

Nota: Este chatbot solo funciona si tienes acceso a los bots de poe.com mediante cookies.

## Cómo desplegarlo desde el repositorio original

Para desplegar este chatbot desde el repositorio original, sigue los siguientes pasos:

1. Clona el repositorio en tu servidor: `git clone https://github.com/HirCoir/Poe-chat-using-cookie.git`
2. Crea una base de datos MySQL y importa la base de datos `bot.sql` incluida en el repositorio.
3. Asegúrate de tener instalados los módulos pip Flask, pymysql, poe y concurrent.futures.
4. Ejecuta el archivo `app.py` con Python: `python app.py`
5. Abre `http://localhost:5000/` en tu navegador web para acceder al chatbot.

## Como obtener la Cookie y usarla en la app?
Para que el bot de poe funcione correctamente, es necesario extraer las cookies de su navegador después de iniciar sesión utilizando la extensión Cookie Editor en Google Chrome, puede abrirla con un click. La sesión se llama "p-b" y deberá copiar el valor del campo "value" e insertarlo en:
tokens = ["XXXXXXXXXXXXXXXXXXXXX%3D%3D"]
remplazando XXXXXXXXXXXXXXXXXXXXX%3D%3D por la cookie, igual puede insertar varias cookies ya que al enviar el mensaje al bot este elije un token random.
Ejemplo para usar varas cookies:
`tokens = [
"XXXXXXXXXXXXXXXXXXXXX%3D%3D",
"XXXXXXXXXXXXXXXXXXXXX%3D%3D",
"XXXXXXXXXXXXXXXXXXXXX%3D%3D",
"XXXXXXXXXXXXXXXXXXXXX%3D%3D",
"XXXXXXXXXXXXXXXXXXXXX%3D%3D"
]`

## Cómo crear la base de datos mediante la terminal

Para crear la base de datos MySQL necesaria para este chatbot, sigue los siguientes pasos:

1. Inicia sesión en MySQL en la terminal: `mysql -u root -p`
2. Crea la base de datos: `CREATE DATABASE bot;`
3. Selecciona la base de datos: `USE bot;`
4. Importa la estructura de la base de datos desde el archivo `bot.sql`: `SOURCE /path/to/bot.sql;` (reemplaza `/path/to/` con la ruta completa al archivo `bot.sql`)

¡Listo! Ahora puedes desplegar el chatbot desde el repositorio original siguiendo los pasos previamente mencionados.
