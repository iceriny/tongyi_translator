import logging
import os
from src.dnd_translator import DndTranslator

if __name__ == "__main__":
    ISDEV = os.environ.get("ISDEV", "true")
    if ISDEV == "true":
        logging_level = logging.DEBUG
    else:
        logging_level = logging.INFO
    print("logging_level: ", logging_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging_level)
    file_handler = logging.FileHandler('run.log', mode="w", encoding="utf-8")  # 设置写入模式（'w' 表示覆盖写入，'a' 表示追加写入）
    file_handler.setLevel(logging_level)

    # 创建一个格式器并将其添加到处理器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)


    # 配置基本的日志记录设置
    logging.basicConfig(
        level=logging_level,  # 设置日志级别
        handlers=[file_handler, ],# console_handler,],
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # 设置日志格式
        datefmt="%Y-%m-%d %H:%M:%S",  # 设置日期格式
    )

    translator = DndTranslator()
    translator.load_data()
    translator.get_results()
    translator.save_data()
