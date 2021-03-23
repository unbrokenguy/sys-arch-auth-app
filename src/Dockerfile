FROM python:3.7.9

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIPENV_VERBOSITY -1

RUN apt update
RUN apt install netcat -y
RUN apt install -y gettext libgettextpo-dev

RUN pip install --upgrade pip
RUN pip install poetry==1.0.10
COPY pyproject.toml /usr/src/app/pyproject.toml
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/.
RUN chmod 777 /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
 
