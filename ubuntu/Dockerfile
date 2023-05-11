FROM ubuntu:latest

WORKDIR /workdir

RUN apt-get update -qqy && apt-get install -qqy \
	sudo \
	curl \
	openssh-server \
	git \
	nano \
	python3 \
	python3-pip && \
	apt-get clean -qq && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /tmp/*