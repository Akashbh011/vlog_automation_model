from abc import ABC, abstractmethod
from typing import Type, TypeVar
from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


class LLMProvider(ABC):

    @abstractmethod
    def generate_structured(
        self,
        prompt: str,
        response_schema: Type[T],
        model: str | None = None,
    ) -> T:
        """
        Generate structured output matching the supplied Pydantic schema.
        """
        raise NotImplementedError