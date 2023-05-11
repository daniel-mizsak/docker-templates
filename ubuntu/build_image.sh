#!/bin/bash

docker pull ubuntu:22.10
docker build \
	--no-cache \
	--rm \
	--tag ubuntu-image \
	.