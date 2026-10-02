from pydantic import BaseModel, Field


class AppearanceOption(BaseModel):
    option_id: str

    name: str

    description: str

    ashva_appearance: str

    environment_style: str

    lighting_style: str

    color_language: str

    summoning_style: str

    emotional_feel: str

    cinematic_style: str

    reference_requirements: list[str] = Field(default_factory=list)


class AppearanceSelection(BaseModel):
    selected_option_id: str
    reason: str