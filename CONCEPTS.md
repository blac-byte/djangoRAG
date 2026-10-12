## Docker

- You use `docker-compose.yaml` to orchestrate multi-container setups.
- Image: a snapshot of the filesystem(I suppose it is all the code from the codebase)
- Container: a working/running instance of the image, so a VM inside your computer.
- Volume: persistent storage of the container separate from the container. It  survive everything except `docker compose down -v` or `docker volume rm`.
- Docker compose: a composer


```
docker compose up -d          # start everything in background
docker compose ps             # see status (look for "healthy")
docker compose logs -f db     # tail logs of the db service
docker compose logs -f redis
docker compose down           # stop + remove containers, KEEP volumes
docker compose down -v        # stop + remove containers AND volumes (wipes DB)
docker compose restart db     # restart just one service
docker compose exec db psql -U raguser -d ragdb   # shell into Postgres
```


## Dev knowledge
1. You split your settings in mysite to base, dev, prod to vary the settings in production, development
2. settings
    |-base.py
    |-dev.py
    |-prod.py


# 2026-10-11 — settings split
# BASE_DIR needs 3 parents when file is in config/settings/
# manage.py/wsgi.py/asgi.py each set DJANGO_SETTINGS_MODULE
# use django-environ, NOT environ (Py2 package, same import name)