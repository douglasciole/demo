FROM python:3.10-bullseye

# set env variables
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	LC_ALL=C.UTF-8 \
	LANG=C.UTF-8 \
	TZ=America/Vancouver

WORKDIR /app

# install system packages
COPY poetry.lock pyproject.toml /app/

RUN pip install poetry \
	&& poetry config virtualenvs.create false \
	&& poetry install --no-interaction --no-ansi

RUN  adduser -u 5678 --disabled-password --gecos "" serveruser \
	&& chown -R serveruser .

USER serveruser

COPY . . 

RUN ./manage.py collectstatic --no-input

EXPOSE 8000

CMD [ "gunicorn",  "outgo.wsgi" ]