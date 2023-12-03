from typing import List
from zipfile import ZipFile


class ZipExtractor:
    def __init__(self, filepath: str):
        self.filepath = filepath

    @property
    def zipfile(self):
        return ZipFile(self.filepath)

    def get_files_by_format(self, file_format: str = 'pdf') -> List[str]:
        return [file.filename for file in self.zipfile.infolist() if file.filename.endswith(f'.{file_format}')]

    def extract_file(self, filename: str):
        return self.zipfile.open(filename)
