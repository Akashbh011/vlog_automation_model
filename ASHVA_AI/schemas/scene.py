from pydantic import BaseModel, Field
from .frame_state import FrameState


class SceneAudio(BaseModel):
    ambient_sound: list[str] = Field(default_factory=list)
    motorcycle_sound: list[str] = Field(default_factory=list)
    sound_effects: list[str] = Field(default_factory=list)
    dialogue: str | None = None


class Scene(BaseModel):

    scene_id: int

    duration_seconds: int = 8

    title: str

    narrative_purpose: str

    action_description: str

    environment_description: str

    camera_description: str

    lighting_description: str

    ashva_description: str

    summoning_description: str | None = None

    audio: SceneAudio

    start_state: FrameState

    end_state: FrameState

    reference_assets: list[str] = Field(default_factory=list)

    continuity_requirements: list[str] = Field(default_factory=list)

    transition_to_next_scene: str