"""Batch processing with MapReduce, implemented with Dramatiq."""
import itertools

import dramatiq
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend
from dramatiq.brokers.redis import RedisBroker

import requests
import spacy


# Dramatiq Setup
result_backend = RedisBackend(host="redis", port=6379)
redis_broker = RedisBroker(host="redis", port=6379)
redis_broker.add_middleware(Results(backend=result_backend))

dramatiq.set_broker(redis_broker)

# Using Spacy for entity extraction.
nlp = spacy.load("en_core_web_sm")


@dramatiq.actor(store_results=True)
def extract_ents(paragraph: str):
    """Extract entities from the paragraph."""
    doc = nlp(paragraph)
    ents = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            ents.append(ent.text)
    return ents


if __name__ == "__main__":
    # Moby Dick - Split into paragraphs.
    data = requests.get("https://www.gutenberg.org/files/2701/2701-0.txt").content.decode('utf-8')
    paragraphs = data.split("\r\n\r\n")

    print("Staring Jobs")
    group = dramatiq.group([extract_ents.message(x) for x in paragraphs]).run()
    results = itertools.chain(*[x for x in group.get_results(block=True, timeout=100_000)])

    print(set(results))
