FROM python:3
LABEL maintainer="sprain@yandex.ru"
RUN mkdir -p /usr/src
COPY . /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt
EXPOSE 8180
EXPOSE 8181
VOLUME /usr/src/app/models
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
