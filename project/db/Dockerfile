# pull official image base of postgres
FROM postgres:13-alpine

# RUN create.sql on init to create databases for dev and test
ADD create.sql /docker-entrypoint-initdb.d