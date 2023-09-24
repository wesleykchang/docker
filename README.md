# docker

We have an ever-increasing selection of docker images and containers. This repo contains all our dockerfiles and a tool for automatically building (and pushing) images

```
./build.sh DOCKERFILE_NAME
```

We use these containers in various permutations. Each of them needs their unique IP address, port bindings, and sometimes a USB address. To ensure no overlaps I the repo includes a little tool that automatically creates the `docker-compose.yaml` with no clashes and correct volume mapping.

Just run

```
$ python orchestrate.py container1 container2 container3

```

_Why not use Docker Desktop?_

Now, Docker Desktop is nice but kind of incompatible with deployment at Club Steingart because most of our deployment is done remotely on lightweight-ish machines (rpi and $200 linux boxes). Having a CLI tool massively reduces all an any stress, and makes switching between machines a breeze.

### TODOs

[ ] Way too many images have `ubuntu:latest` as the base, where they should be using alpine. Will get around to fixing it
