class OpenAIProvider:
    """
    Placeholder for optional OpenAI API integration.

    This provider should implement the same interface
    as GeminiProvider once enabled.
    """

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    def generate_structured(
        self,
        prompt,
        response_schema,
        model=None,
    ):
        raise NotImplementedError(
            "OpenAI provider is not enabled yet."
        )