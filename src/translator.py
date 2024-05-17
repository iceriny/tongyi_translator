from api import DashscopeAPI


class Translator:
    def __init__(self, context:str):
        self.api = DashscopeAPI(
            f"你是一个翻译者，从事一个{context}的翻译工作，用户将发送你一段英文，你将回复并只回复对应的中文翻译。",
            model="qwen-turbo",
            is_single_turn=False,
        )

    def get(self, string: str):
        return self.api(string)
