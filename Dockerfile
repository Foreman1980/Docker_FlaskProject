FROM python:3
LABEL maintainer="sprain@yandex.ru"
COPY . /usr
WORKDIR /usr
RUN pip install -r requirements.txt
EXPOSE 8180
EXPOSE 8181
VOLUME /usr/app/models
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
