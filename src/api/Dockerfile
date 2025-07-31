FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONBUFFERED = 1

WORKDIR ./app
COPY ../requirements/prod.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt --no-cache-dir

COPY /src/api/ .

EXPOSE 8000
