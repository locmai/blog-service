install:
	@poetry install

start-dev:
	@poetry run uvicorn blog_service.main:app --reload

test:
	@poetry run pytest

build:
	DOCKER_BUILDKIT=1 docker build -t locmai/blog-service:${TAG} .

deploy:
	az webapp update --name={app_name}