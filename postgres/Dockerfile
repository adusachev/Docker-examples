FROM postgres

ENV POSTGRES_PASSWORD pass
ENV POSTGRES_DB mydb
ENV POSTGRES_USER aleksei

COPY create_db.sql /docker-entrypoint-initdb.d/
# COPY ./backup/mydb.sql /docker-entrypoint-initdb.d/
