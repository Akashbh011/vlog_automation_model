from pydantic import BaseModel, Field


class EnvironmentSpecification(BaseModel):
    location: str
    time_of_day: str
    weather: str
    season: str
    terrain: str
    road_description: str
    visibility: str
    atmosphere: str
    lighting: str


class CinematographySpecification(BaseModel):
    camera_style: str
    viewpoint: str
    lens_characteristics: str
    camera_movement: str
    motion_behavior: str
    depth_of_field: str


class AshvaWorldSpecification(BaseModel):
    appearance_variant: str
    physical_description: str
    aura: str
    energy_behavior: str
    personality: str
    emotional_state: str
    summoning_concept: str


class WorldBible(BaseModel):
    episode_id: str

    story_theme: str
    narrative_tone: str
    emotional_arc: str

    environment: EnvironmentSpecification

    cinematography: CinematographySpecification

    ashva: AshvaWorldSpecification

    visual_language: list[str] = Field(default_factory=list)

    continuity_rules: list[str] = Field(default_factory=list)

    prohibited_elements: list[str] = Field(default_factory=list)