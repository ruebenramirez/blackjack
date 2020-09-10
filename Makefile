SHELL := /bin/bash

pull-base-container:
	docker pull alpine:3.12

container_build: pull-base-container
	docker build \
		-t ruebenramirez/blackjack:latest .

test: container_build
	docker run -ti --rm \
		--name ruebenramirez-blackjack-test \
		ruebenramirez/blackjack:latest \
		sh -c '/usr/bin/python -m pytest tests/*'

play: container_build
	docker run -ti --rm \
		ruebenramirez/blackjack:latest \
		python blackjack.py

install-python-deps:
	virtualenv .venv && \
	source .venv/bin/activate && \
		pip install -r requirements.txt
