FROM mysql

EXPOSE 3306
ADD init.sql /docker-entrypoint-initdb.d
