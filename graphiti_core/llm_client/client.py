"""
Copyright 2024, Zep Software, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import typing
from abc import ABC, abstractmethod

from ..prompts.models import Message
from .config import LLMConfig


class LLMClient(ABC):
    @abstractmethod
    def __init__(self, config: LLMConfig | None):
        pass

    @abstractmethod
    def get_embedder(self) -> typing.Any:
        pass

    @abstractmethod
    async def generate_response(self, messages: list[Message]) -> dict[str, typing.Any]:
        pass