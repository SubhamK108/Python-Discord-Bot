FROM python:buster
WORKDIR /app

RUN python3 -m pip install -U discord.py requests

COPY . .
CMD [ "python3", "Program.py" ]