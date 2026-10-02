class ImageProvider:
    """
    Abstraction for future image-generation/reference-frame
    workflows.
    """

    def generate_image(self, prompt: str, **kwargs):
        raise NotImplementedError(
            "Image generation provider is not enabled yet."
        )