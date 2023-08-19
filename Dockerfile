FROM ubuntu

WORKDIR /app

RUN DEBIAN_FRONTEND="noninteractive" apt update && \
    DEBIAN_FRONTEND="noninteractive" apt upgrade -y && \
    apt install -y python3-setuptools python3-pip python3 python3-dev cron
RUN pip install flask flask-markdown pandas
RUN echo "*/30 * * * * /usr/bin/python3 /app/collate.py 1>/logs 2>/logerrors" >> crontab && \
    crontab crontab

COPY . .
RUN chmod +x startup.sh

ENV FLASK_APP=app.py

CMD ["./startup.sh"]
# CMD ["bash"]
