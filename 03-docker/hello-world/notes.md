# Dockerfile — заметки

## Что посмотрел
- Docker для новичков #2 (Dockerfile)
- Docker для новичков #4 (слои и кэш)

## Главный инсайт про слои
1. Что редко меняется ставим выше, что часто меняется ставим ниже

## docker history моего образа
IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT
e511b2b48aa7   29 seconds ago   CMD ["python3" "app.py"]                        0B        buildkit.dockerfile.v0
<missing>      29 seconds ago   RUN /bin/sh -c echo "Building image..." # bu…   4.1kB     buildkit.dockerfile.v0
<missing>      29 seconds ago   EXPOSE [8000/tcp]                               0B        buildkit.dockerfile.v0
<missing>      29 seconds ago   ENV PORT=8000                                   0B        buildkit.dockerfile.v0
<missing>      29 seconds ago   COPY app.py . # buildkit                        12.3kB    buildkit.dockerfile.v0
<missing>      29 seconds ago   RUN /bin/sh -c pip install --upgrade pip # b…   21.3MB    buildkit.dockerfile.v0
<missing>      42 hours ago     WORKDIR /app                                    8.19kB    buildkit.dockerfile.v0
<missing>      3 days ago       CMD ["python3"]                                 0B        buildkit.dockerfile.v0
<missing>      3 days ago       RUN /bin/sh -c set -eux;  for src in idle3 p…   16.4kB    buildkit.dockerfile.v0
<missing>      3 days ago       RUN /bin/sh -c set -eux;   savedAptMark="$(a…   48.4MB    buildkit.dockerfile.v0
<missing>      3 days ago       ENV PYTHON_SHA256=272179ddd9a2e41a0fc8e42e33…   0B        buildkit.dockerfile.v0
<missing>      3 days ago       ENV PYTHON_VERSION=3.11.15                      0B        buildkit.dockerfile.v0
<missing>      3 days ago       ENV GPG_KEY=A035C8C19219BA821ECEA86B64E628F8…   0B        buildkit.dockerfile.v0
<missing>      3 days ago       RUN /bin/sh -c set -eux;  apt-get update;  a…   4.94MB    buildkit.dockerfile.v0
<missing>      3 days ago       ENV LANG=C.UTF-8                                0B        buildkit.dockerfile.v0
<missing>      3 days ago       ENV PATH=/usr/local/bin:/usr/local/sbin:/usr…   0B        buildkit.dockerfile.v0
<missing>      4 days ago       # debian.sh --arch 'amd64' out/ 'trixie' '@1…   87.4MB    debuerreotype 0.17


