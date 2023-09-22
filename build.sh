#!/bin/bash

# Get the name of the Dockerfile from the first argument
name=$1

docker build -t steingartlab/easi:$name -f dockerfiles/$name .
