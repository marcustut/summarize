deps:
	pip install -r requirements.txt

server-dev:
	uvicorn main:app --reload --app-dir server

server-prod:
	uvicorn main:app --app-dir server --host 0.0.0.0 --port 8080

client-deps:
	cd client && pnpm i

client-dev:
	cd client && pnpm dev

summarize-install:
	pip install .
