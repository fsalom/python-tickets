FROM rudodeveloper/python:3.12.0

RUN pip install poetry
RUN mkdir /code
WORKDIR /code
RUN ls -la .
COPY ../ /code/
RUN ls -la /code
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
EXPOSE 8000
CMD ["gunicorn", "infrastructure.django.wsgi:application", "-b", "0.0.0.0:8000", "--workers=3", "--log-level=debug"]
