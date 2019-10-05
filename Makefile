build:
	docker build -t simple-batch-container .

compose: build
	docker-compose up
