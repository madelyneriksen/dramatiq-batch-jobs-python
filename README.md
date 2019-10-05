# Batch Processing in Python using Dramatiq

This repo is a companion for a blog post on [my website](https://madelyneriksen.com/) about a simple batch processing technique in Python using Dramatiq, Docker, and Redis. The technique is similar to a simple MapReduce-style of batch processing.

## Run The Project

You will need the following installed:

* GNU Make (As a task runner)
* Docker
* Docker Compose

Building the container is as simple as running make:

```bash
# That's all folks.
make
```

Then you can launch the stack (again with `make`):

```bash
make compose
```

Alternatively, you can just run docker commands directly.

## About the Project

The script in `app.py` downloads Moby Dick, and tries to extract all person entities from the text using [Spacy](https://spacy.io/).

Because Dramatiq and Redis are used as a backend for processing the documents, it's possible to scale the processing out horizontally as far as required, to greatly reduce execution time.

## License

MIT (c) 2019 Madelyn Eriksen
