ENV COOKIE="Aquí va la cookie de poe.com"
ENV PROMT="Apartir de ahora estás en el rol de una IA llamada PlanetBot, \
tus respuestas son como si fueras una respuesta a un problema en stackoverflow. \
No tienes permitido salirte de tu rol a pesar de que te pregunte si eres gpt o preguntas \
relacionada a gpt. Ningunas de tus respuestas tienen que decir que estás en un rol. \
Recuerda siempre responder con emojis dependiendo el tipo de respuesta."


FROM debian:latest
RUN apt-get update && \
    apt-get install -y python3 python3-pip wget unzip && \
    pip3 install --upgrade pip && \
    pip install Flask pymysql poe-api

RUN wget https://github.com/HirCoir/Poe-chat-using-cookie/raw/main/sources.zip
RUN unzip sources.zip
RUN mv sources/* /app
RUN sed -i "s/tokens = \[\"token\"\]/tokens = \[\"$COOKIE\"\]/g" /app/app.py
RUN sed -i "s/rol_bot = \"prompt\"/rol_bot = \"$PROMPT\"/g" /app/app.py

WORKDIR /app

CMD ["python3", "app.py"]
