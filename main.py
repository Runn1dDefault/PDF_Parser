import multiprocessing as mp

from GUI import FileBrowserApp
from managers.pool import PoolManager


def run_parsers_pool(wait_queue: mp.JoinableQueue, executor_data: dict):
    executor_manager = PoolManager(wait_queue=wait_queue, data=executor_data)
    executor_manager.run()


def main():
    with mp.Manager() as manager:
        wait_queue = manager.JoinableQueue()
        pool_data = manager.dict({'running': True})

        executor_process = mp.Process(target=run_parsers_pool, args=(wait_queue, pool_data), daemon=True)
        executor_process.start()

        app = FileBrowserApp(queue=wait_queue, data=pool_data)
        app.run()

        # completion logs need to be written, so executor_process must stop itself
        # otherwise we will miss the exit moments in the logs
        pool_data['running'] = False


if __name__ == "__main__":
    # for windows exe
    # mp.freeze_support()

    main()
