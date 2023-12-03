import os
from datetime import datetime
from logging import getLogger
from multiprocessing import JoinableQueue
from typing import List, Iterable, Tuple, Dict

from tkinter import filedialog, messagebox, Tk, Text, Button, END, CENTER

from config import DESKTOP_PATH


class FileBrowserApp:
    def __init__(self, queue: JoinableQueue = None, data: dict = None):
        self.file_spliter = '/'
        self.window = Tk()
        self.queue = queue
        self.data = data
        self.running = True
        self._create_open_file = False
        self.info_bar = Text(self.window, height=10, width=100)
        self.button_explore = Button(self.window, text="Select Files", command=self.browse_files)

        self.logger = getLogger(self.__class__.__name__)

    def setup_window(self):
        self.logger.info('Setting up...')

        self.window.title('PDF Parser')
        self.window.geometry("500x500")
        self.window.config(background="white")
        self.info_bar.pack()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.logger.info('Setting up over!')

    def run(self):
        self.logger.info('Start...')
        self.setup_window()
        self.positions_setup()

        while self.running:
            if self.data and self.data.get('ui_log'):
                log_msg = self.data.pop('ui_log')
                self.add_message_info_bar(log_msg)

            self.window.update()

        # self.window.mainloop()
        self.logger.info('Over!')

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.running = False
            self.window.destroy()

    def browse_files(self):
        self.logger.info('FileBrowser open...')
        filenames = filedialog.askopenfilenames(
            initialdir=DESKTOP_PATH,
            title="Load File Selection Dialog",
            filetypes=(("Pdf files", "*.pdf"), ("zip files", "*.zip"))
        )
        self.logger.info('FileBrowser close...')

        validated, not_valid = self._validate_files(filenames)

        if validated:
            msg = "\n\nFile parsing started: \n \t" + '\n \t'.join(validated)

            if self.queue:
                self.logger.debug('send to queue: {}'.format(validated))
                self.queue.put(validated)
                filename = os.path.basename(DESKTOP_PATH)
                msg += f'\n\nThe output xlsx file will be created in: ' \
                       f'\n\t {filename} \n\twith a name containing {datetime.now().date()}.'

            self.add_message_info_bar(msg)

        if not_valid:
            message = self._errors_files_complete_to_message(not_valid)
            messagebox.showinfo(title='Found invalid files', message=message)

    def add_message_info_bar(self, msg: str):
        self.info_bar.insert(END, msg)

    def positions_setup(self):
        self.button_explore.place(relx=0.5, rely=0.5, anchor=CENTER)

    def _validate_files(self, files: Iterable[str]) -> Tuple[List[str], Dict[str, List[str]]]:
        validated = []
        not_valid = {}

        for file in files:
            if not isinstance(file, str):
                reason = 'Invalid file'

                if not not_valid.get(reason):
                    not_valid[reason] = []

                not_valid[reason].append(file)
                self.logger.error(f'{file} is not string! Type: {type(file)}')
                continue

            if file.endswith('.zip') or file.endswith('.pdf'):
                validated.append(file)
            else:
                reason = 'Is not zip and not pdf file'

                if not not_valid.get(reason):
                    not_valid[reason] = []

                not_valid[reason].append(file)
                self.logger.error(f'{file} is not zip and not pdf file!')

        return validated, not_valid

    @staticmethod
    def _errors_files_complete_to_message(error_files: Dict[str, List[str]]) -> str:
        errors = []

        for reason, files in error_files.items():
            files = ' \n \t '.join(files)
            msg = f'{reason}: \n \t {files}'
            errors.append(msg)

        return '\n\n'.join(errors)
