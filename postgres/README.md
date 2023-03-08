Simple database with two tables

**Usage**
```
docker-compose up
```

```
docker exec -it [container_name] bash
```

```
psql -U [user] -d [database_name]
```

List of all databases: `\l`

Connect to database database_name: `\c <database_name>`

List of tables in database: `\dt` 

List of all users: `\du`

**Create database dump**

```
pg_dump [parameters] [database_name] > [dump_filename]
```


Restore dump file:
```
psql [database_name] < [dump_filename]
```
