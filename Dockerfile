FROM python:3.10-slim
MAINTAINER rhasan.amiya@gmail.com

ENV PYTHONUNBUFFERED 1
ENV PORT 8030

WORKDIR /app
RUN mkdir src

RUN apt-get update && apt-get install build-essential curl -y && \
    pip3 install -U pip

RUN pip install poetry
ENV PATH="/root/.poetry/bin:${PATH}"

ADD poetry.lock /app

ADD pyproject.toml /app

RUN poetry config virtualenvs.create false

COPY src/ /app/src/

RUN poetry install

RUN apt-get --purge autoremove build-essential -y

EXPOSE $PORT