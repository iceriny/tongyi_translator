# -*- coding: utf-8 -*-
from http import HTTPStatus
import random
import logging
import dashscope
from dashscope.api_entities.dashscope_response import Message, GenerationResponse


class DashscopeAPI:
    def __init__(
        self,
        system_message: str,
        *,
        is_single_turn: bool = False,
        model: str | None = None,
        seed: int | None = None,
        top_p: float | None = None,
        result_format: str | None = None,
        enable_search: bool | None = None,
        max_tokens: int | None = None,
        temperature: float | None = None,
        repetition_penalty: float | None = None,
    ):
        self.messageList: list[Message] | None = [
            Message(role="system", content=system_message)
        ] if not is_single_turn else None
        self.prompt = None
        self.model = model
        self.seed = seed
        self.top_p = top_p
        self.result_format = result_format
        self.enable_search = enable_search
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.repetition_penalty = repetition_penalty

    def __call__(self, message: str):
        if self.messageList:
            self.messageList.append(Message(role="user", content=message))
        else:
            self.prompt = message
        return self.__send()

    def __send(self):
        response = dashscope.Generation.call(
            model=self.model if self.model else "qwen-1.8b-chat",
            messages=self.messageList if self.messageList else None, # type: ignore
            prompt=self.prompt if self.prompt else None,
            seed=self.seed if self.seed else random.randint(1, 1000000),
            top_p=self.top_p if self.top_p else 0.8,
            result_format=self.result_format if self.result_format else "message",
            enable_search=self.enable_search if self.enable_search is None else False,
            max_tokens=self.max_tokens if self.max_tokens else 1500,
            temperature=self.temperature if self.temperature else 0.85,
            repetition_penalty=(
                self.repetition_penalty if self.repetition_penalty else 1.0
            ),
        )
        if not isinstance(response, GenerationResponse):
            raise
        if response.status_code == HTTPStatus.OK:
            logging.info(response.usage)
            return response.output.choices[0].message.content
        else:
            logging.error("Request id: %s, Status code: %s, error code: %s, error message: %s"
                % (
                    response.request_id,
                    response.status_code,
                    response.code,
                    response.message,
                ))
            return "发生错误，请稍后再试"
