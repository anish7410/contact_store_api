FROM mysql:8.0.33
ENV MYSQL_DATABASE=pyAPI_detail
ENV MYSQL_ROOT_PASSWORD=kali
ENV MYSQL_HOST = db
ADD ./db_schema.sql /docker-entrypoint-initdb.d 