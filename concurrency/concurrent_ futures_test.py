import requests
from concurrent import futures
from utils.execution_time import execution_time

MAX_WORKERS = 32
VERBOSE = False
TEST_LOOPS = 10

things_to_download = [
    'http://news.ycombinator.com/rss',
    'http://www.reddit.com/r/Python/.rss',
]


def get_thing(thing):
    return requests.get(thing).text


@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def download_all_things_map(things):
    workers = min(MAX_WORKERS, len(things))
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        response = executor.map(get_thing, things)
    return response


@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def download_all_things_submit(things):
    workers = min(MAX_WORKERS, len(things))

    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        to_do = []
        for thing in things:
            future = executor.submit(get_thing, thing)
            to_do.append(future)
            # print("Scheduled for {}:{}".format(thing, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            # print("{} result {!r}".format(future, res))
            results.append(res)
    return len(results)


@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def download_all_things_sequential(things):
    for thing in things:
        get_thing(thing)


if __name__ == "__main__":
    download_all_things_map(things_to_download)
    download_all_things_submit(things_to_download)
    download_all_things_sequential(things_to_download)

    ""
    [download_all_things_map] exec time: 1.1174753980000787 s, loops: 10
    [download_all_things_submit] exec time: 0.7971122307001679 s, loops: 10
    [download_all_things_sequential] exec time: 1.1475031709001087 s,loops: 10

    ""
