# docker

We have an ever-increasing selection of docker images and containers. This repo contains all our dockerfiles and a tool for automatically building them

```
./build.sh DOCKERFILE_NAME
```

We use these containers in various permutations. Each of them needs their unique IP address, port bindings, and sometimes a USB address. To ensure no overlaps I made this tidy little tool that automatically creates the `docker-compose.yaml` with no clashes and correct volume mapping.

Just run

```
$ python orchestrate.py container1 container2 container3

```
