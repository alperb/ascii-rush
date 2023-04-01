FROM python:3.10.10-slim-bullseye

WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .
RUN rm .env
EXPOSE 3000
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/run/sshd /var/log/supervisor

ENTRYPOINT supervisord -c supervisor.conf