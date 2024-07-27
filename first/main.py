import asyncio
import signal
import random
import time

def get_cencelation_signal():
    kill_now = False
    def exit_gracefully(_0, _1):
        nonlocal kill_now
        kill_now = True
    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGTERM, exit_gracefully)
    return lambda: kill_now

async def producer(queue):
    is_canceled = get_cencelation_signal()
    while not is_canceled():
        i = random.randint(1, 100)
        await queue.put(i)
        await asyncio.sleep(i / 500)

async def create_worker(queue, number):
    while True:
        item = await queue.get()
        await asyncio.sleep(item / 100)
        print(f'Message processed by worker {number}: {item}')
        queue.task_done()

async def main():
    queue = asyncio.Queue()    

    workers = [asyncio.create_task(producer(queue))]
    for i in range(5):
       workers.append(asyncio.create_task(create_worker(queue, i)))

    await asyncio.sleep(1)
    await queue.join()

    for worker in workers:
        worker.cancel()

asyncio.run(main())