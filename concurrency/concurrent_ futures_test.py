from concurrent import futures

import requests

from utils.execution_time import execution_time

MAX_WORKERS = 32

things_to_download = [
    'http://news.ycombinator.com/rss',
    'http://www.reddit.com/r/Python/.rss',
]


def get_thing(thing):
    return requests.get(thing).text


@execution_time(loops=10, verbose=True)
def download_all_things(things):
    workers = min(MAX_WORKERS, len(things))
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        response = executor.map(get_thing, things)
    return response


@execution_time(loops=10, verbose=True)
def download_all_things_sequential(things):
    for thing in things:
        get_thing(thing)


if __name__ == "__main__":
    download_all_things(things_to_download)
    download_all_things_sequential(things_to_download)