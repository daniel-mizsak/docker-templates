#!/bin/bash

docker pull pytorch/pytorch:latest
docker build \
	--no-cache \
	--rm \
	--tag pytorch-image \
	.