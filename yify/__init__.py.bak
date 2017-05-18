import asyncio

from yify.api import get_all


NUM_COROUTINES = 30


def latest(from_page=1, to_page=1):
    '''Show latest movies.'''
    # create a semaphore to limit coroutine numbers
    sem = asyncio.Semaphore(NUM_COROUTINES)

    # create an event loop
    loop = asyncio.get_event_loop()

    futures = []
    # create a new future for each page
    for page in range(from_page, to_page + 1):
        # use future to wrap a an asynchronous execution
        future = asyncio.Future()
        asyncio.async(get_all('latest', page, None, future, sem))
        futures.append(future)

    # wait for all futures to complete
    loop.run_until_complete(asyncio.wait(futures))

    results = []
    # iterate through each future, then get results and append to results
    for f in futures:
        results += f.result()
    return results


def popular(from_page=1, to_page=1):
    '''Show popular movies.'''
    # create a semaphore to limit coroutine numbers
    sem = asyncio.Semaphore(NUM_COROUTINES)

    # create an event loop
    loop = asyncio.get_event_loop()

    futures = []
    # create a new future for each page
    for page in range(from_page, to_page + 1):
        # use future to wrap a an asynchronous execution
        future = asyncio.Future()
        asyncio.async(get_all('popular', page, None, future, sem))
        futures.append(future)

    # wait for all futures to complete
    loop.run_until_complete(asyncio.wait(futures))

    results = []
    # iterate through each future, then get results and append to results
    for f in futures:
        results += f.result()
    return results


def search(keyword, from_page=1, to_page=1):
    '''Search movies.'''
    # replace space with %20
    keyword = keyword.replace(' ', '%20')

    # create a semaphore to limit coroutine numbers
    sem = asyncio.Semaphore(NUM_COROUTINES)

    # create an event loop
    loop = asyncio.get_event_loop()

    futures = []
    # create a new future for each page
    for page in range(from_page, to_page + 1):
        # use future to wrap a an asynchronous execution
        future = asyncio.Future()
        asyncio.async(get_all('search', page, keyword, future, sem))
        futures.append(future)

    # wait for all futures to complete
    loop.run_until_complete(asyncio.wait(futures))

    results = []
    # iterate through each future, then get results and append to results
    for f in futures:
        results += f.result()
    return results


def main():
    movies = latest(1, 3)
    for m in movies:
        print('{}: {}'.format(m['title'], m['rating']))

if __name__ == '__main__':
    main()
