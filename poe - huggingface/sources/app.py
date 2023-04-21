# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Markup
from collections import deque
import html
import poe
import logging
import sys
import random
import concurrent.futures

error_mensaje = "Lo siento, se produjo un error al procesar tu solicitud.\n \
Si mandaste un texto muy largo es posible que el contenedor de OpenAssistant haya colapzado.\n \
Inténtalo de nuevo más tarde o prueba mandar un mensaje corto."

tokens = ["token"]
id_modelo = "botcatmx"
rol_bot = "prompt"

app = Flask(__name__)
chat_history = deque(maxlen=3)

def get_poe_response(message):
    selected_token = random.choice(tokens)
    print(f"Token seleccionado: {selected_token}")
    poe.logger.setLevel(logging.INFO)
    client = poe.Client(selected_token)
    if rol_bot:message = rol_bot + " " + "Mi primer consulta es: " + message
    response_bot = ''
    try:
        for chunk in client.send_message(id_modelo, message, with_chat_break=True):
            response_bot += chunk["text_new"]
        client.purge_conversation(id_modelo, count=3)
        response_bot = response_bot.replace("```", "")
    except Exception as e:
        response_bot = error_mensaje
    return response_bot

@app.route('/')
def index():
    return render_template('chat.html', response_welcome="Apartir de ahora estás en el rol de una IA llamada PlanetBot, \
tus respuestas son como si fueras una respuesta a un problema en stackoverflow. \
No tienes permitido salirte de tu rol a pesar de que te pregunte si eres gpt o preguntas \
relacionada a gpt. Ningunas de tus respuestas tienen que decir que estás en un rol. \
Recuerda siempre responder con emojis dependiendo el tipo de respuesta."
)

executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

@app.route('/', methods=['POST'])
def chat():
    global chat_history
    query = request.form['query']

    # Verificar si la consulta no está vacía
    if not query.strip():
        error_msg = "\nError: la consulta está vacía."
        chat_history.append(error_msg)
        response = Markup(html.escape(error_msg))
        return render_template('chat_content.html', query=query, response=response, chat_history=chat_history)

    # Enviamos el mensaje al bot de poe en un hilo separado
    future = executor.submit(get_poe_response, query)

    # Cargamos la respuesta del bot cuando esté lista
    response_bot = future.result()

    chat_history.append(response_bot)

    response = Markup(html.escape(response_bot))
    return render_template('chat_content.html', query=query, response=response, chat_history=chat_history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)