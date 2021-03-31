FROM python:buster
WORKDIR /app

RUN python3 -m pip install -U discord.py

COPY . .
CMD [ "python3", "Program.py" ]