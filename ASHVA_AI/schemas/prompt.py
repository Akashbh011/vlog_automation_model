from pydantic import BaseModel, Field


class VeoPrompt(BaseModel):

    scene_id: int

    prompt: str

    negative_constraints: list[str] = Field(default_factory=list)

    reference_images: list[str] = Field(default_factory=list)

    first_frame: str | None = None

    last_frame: str | None = None

    continuity_constraints: list[str] = Field(default_factory=list)

    expected_duration_seconds: int = 8

    aspect_ratio: str = "9:16"