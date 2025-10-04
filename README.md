# trino-docker-demo

Minimal demo: Dockerised Python script that queries Trino and a CI workflow that runs tests on PRs.

How to run locally:
1. Build image: docker build -t trino-demo .
2. Run (requires Trino accessible at TRINO_HOST/TRINO_PORT env): 
   docker run --rm -e TRINO_HOST=host -e TRINO_PORT=8080 trino-demo

Run tests locally:
pip install -r requirements.txt
pytest