from abc import ABC, abstractmethod
import os
import logging

from translator import Translator

class BasePlugin(ABC):
    def __init__(self, context: str):
        self.context = context
        self.input_path = "./input"
        all_entries = os.listdir(self.input_path)
        self.input_files = [
            os.path.basename(f)
            for f in all_entries
            if os.path.isfile(os.path.join(self.input_path, f))
        ]
        self.output_path = "./output"
        if len(self.input_files) == 0:
            logging.error("No input files found in input folder")
            self.file_type = None
            return
        self.file_type = self.input_files[0].split(".")[-1]
        self.results = {}

    @abstractmethod
    def get_results(self):
        pass

    def load_data(self):
        logging.info("开始加载数据...")
        self.original_contents = {}
        for file in self.input_files:
            with open(self.input_path + "/" + file, "r", encoding="utf-8") as f:
                self.original_contents[file] = f.read()

    def save_data(self):
        logging.info("开始保存数据...")
        if not self.file_type:
            return
        for file_name, content in self.results.items():
            with open(self.output_path + "/" + file_name, "w", encoding="utf-8") as f:
                f.write(content)

    def translate(self, string: str):
        translator = Translator(self.context)
        return translator.get(string)
