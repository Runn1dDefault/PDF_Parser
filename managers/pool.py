import ntpath
import multiprocessing as mp
from logging import getLogger

from managers.parsers_manager import ParserManager


class PoolManager:
    def __init__(self, wait_queue: mp.Queue, data: dict):
        self.logger = getLogger(self.__class__.__name__)
        self.wait_queue = wait_queue
        self.data = data

    def run(self):
        self.logger.info('Start pool manager work...')

        while bool(self.data.get('running', False)):
            if self.wait_queue.empty():
                continue

            self._new_task_process()

        self.logger.info('Over pool manager work!')
        # return an empty string so as not to violate the principle of inheritance
        return ''

    def _new_task_process(self) -> None:
        self.logger.info('Found new task for parsing...')
        selected_files = self.wait_queue.get()

        if not isinstance(selected_files, list):
            self.logger.error(
                f'Passed future process, because object must been instance of list with filepaths inside!'
                f' Not {type(selected_files)}'
            )
            return

        parser = ParserManager(files=selected_files)

        self.logger.debug(f'Task: {parser.task_id} started...')
        parser.run()
        self.logger.debug(f'Task: {parser.task_id} completed!')

        self.data['ui_log'] = f'\n\nCreated file with name: {ntpath.basename(parser.out_xls_path)}\n\n'
        self.logger.debug('Last Created File is ' + parser.out_xls_path)
