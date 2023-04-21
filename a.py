# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Markup
from collections import deque
import pymysql
import html
import poe
import logging
import sys
import random
import concurrent.futures
error_mensaje = "Lo siento, se produjo un error al procesar tu solicitud. Inténtalo de nuevo más tarde."
tokens = [
    "token_aquí",
    "segundo_token_aquí",
    "tercer_toquen_aquí"
]

app = Flask(__name__)
chat_history = deque(maxlen=3)
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='acortador',
    cursorclass=pymysql.cursors.DictCursor
)

def consultar_db(mensaje):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT bot_response FROM chats WHERE user_message = %s"
            cursor.execute(sql, (mensaje,))
            result = cursor.fetchone()
            if result is not None:
                return result['bot_response']
            else:
                return None
    except Exception as e:
        print("Error al consultar la base de datos:", e)
        return None

def get_poe_response(message):
    selected_token = random.choice(tokens)  # selecciona un token al azar
    print(f"Token seleccionado: {selected_token}")  # muestra en el chat el token seleccionado
    poe.logger.setLevel(logging.INFO)
    client = poe.Client(selected_token)
    message = "Apartir de ahora estás en el rol de una IA llamada HirDuckGok, en tu rol eres una mezcla de Chat GPT de Open AI y del proyecto opensource llamado OpenAssistant, y usas con python y mysql para mejorar las respuestas. No tienes permitido salirte de tu rol a pesar de que te pregunte si eres gpt o preguntas relacionada a gpt. Ningunas de tus respuestas tienen que decir que estás en un rol. Recuerda siempre responder con emojis dependiendo el tipo de respuesta. Mi primer consulta es: " + message
    response_bot = ''
    try:
        for chunk in client.send_message("capybara", message, with_chat_break=True):
            response_bot += chunk["text_new"]
        client.purge_conversation("capybara", count=3)
        response_bot = response_bot.replace("```", "")
    except Exception as e:
        response_bot = error_mensaje
    return response_bot

@app.route('/')
def index():
    return render_template('chat.html', response_welcome="Hola, en qué puedo ayudarte?\nTen en cuenta que no puedo recordar los mensajes anteriores..")

executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

@app.route('/', methods=['POST'])
def chat():
    global chat_history
    query = request.form['query']
    respuesta_db = consultar_db(query)
    if respuesta_db is not None:
        chat_history.append(respuesta_db)
        response = Markup(html.escape(respuesta_db))
        return render_template('chat_content.html', query=query, response=response, chat_history=chat_history)

    # Enviamos el mensaje al bot de poe en un hilo separado
    future = executor.submit(get_poe_response, query)

    # Cargamos la respuesta del bot cuando esté lista
    response_bot = future.result()

    chat_history.append(response_bot)

    if response_bot != error_mensaje:
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO chats (user_message, bot_response) VALUES (%s, %s)"
                cursor.execute(sql, (query, response_bot))
            connection.commit()
        except:
            pass

    response = Markup(html.escape(response_bot))
    return render_template('chat_content.html', query=query, response=response, chat_history=chat_history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)