FROM python:2.7.10-slim
ENV buildDeps "build-essential libpq-dev"
RUN apt-get update && apt-get install -y $buildDeps libpq5
ADD . /app/
WORKDIR /app
RUN pip install -e .
RUN pip install -r test-requirements.txt
RUN pip install -r dev-requirements.txt
RUN apt-get purge -y --auto-remove $buildDeps && rm -rf /var/lib/apt/lists/*
