FROM rudodeveloper/python:3.12.0

RUN apt-get update && apt-get install -y supervisor
RUN pip install poetry
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
RUN chmod +x /code/start.sh
EXPOSE 8000 8001

CMD ["/code/start.sh"]
