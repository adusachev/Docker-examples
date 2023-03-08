FROM postgres

ENV POSTGRES_DB mydb
ENV POSTGRES_USER aleksei
ENV POSTGRES_PASSWORD pass

COPY create_db.sql /docker-entrypoint-initdb.d/
