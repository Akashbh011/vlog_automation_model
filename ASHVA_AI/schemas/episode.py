from pydantic import BaseModel, Field
from .world_bible import WorldBible
from .appearance import AppearanceSelection
from .scene import Scene


class EpisodeScript(BaseModel):
    episode_id: str
    title: str
    raw_script: str


class Episode(BaseModel):

    episode_id: str

    script: EpisodeScript

    world_bible: WorldBible | None = None

    appearance_selection: AppearanceSelection | None = None

    scenes: list[Scene] = Field(default_factory=list)

    status: str = "created"