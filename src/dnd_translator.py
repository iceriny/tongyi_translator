from cgitb import text
import re
from base_plugin import BasePlugin
import xml.etree.ElementTree as ET
import html
import logging
from tqdm import tqdm


class DndTranslator(BasePlugin):
    def __init__(self):
        super().__init__("龙与地下城电子游戏")

    def load_data(self):
        super().load_data()
        self.original_xmls: dict[str, ET.Element] = {}
        for name, xml_content in self.original_contents.items():
            logging.debug("解析:%s", name)
            tree = ET.fromstring(xml_content)
            logging.debug("Done!")
            self.original_xmls[name] = tree
        logging.info("加载数据完成。")

    def get_results(self):
        logging.info("开始翻译。")
        for name, xml_content in tqdm(self.original_xmls.items()):
            logging.debug("翻译: %s", name)
            contents = self.__get_content(xml_content)
            self.__trans_single_xml_files(contents)
            string = ET.tostring(xml_content, encoding="unicode")
            self.results[name] = string

    def __get_content(self, xml_content: ET.Element):
        return xml_content.findall("content")

    def __trans_single_xml_files(self, elements: list[ET.Element]):
        for content in tqdm(elements):
            if content.text is None:
                continue
            text = content.text
            # match = re.match(r" 2e$", text)
            # if match:
            #     text = text.replace(" 2e", "")
            trans = self.translate(html.unescape(text))
            # if match:
            #     trans += "*2e"
            logging.debug("原文:%s译文:%s", content.text, trans)
            if isinstance(trans, str):
                content.text = html.escape(trans)
