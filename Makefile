deps:
	pip install -r requirements.txt --use-feature=in-tree-build

server-dev:
	uvicorn main:app --reload --app-dir server

client-deps:
	cd client && pnpm i

client-dev:
	cd client && pnpm dev

summarize-install:
	pip install . --use-feature=in-tree-build