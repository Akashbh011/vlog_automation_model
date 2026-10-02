from typing import Optional
from pydantic import BaseModel, Field


class Position(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    description: str


class CameraState(BaseModel):
    viewpoint: str
    height_description: str
    orientation: str
    movement: str
    lens_description: Optional[str] = None


class MotorcycleState(BaseModel):
    model: str
    color: str
    position: str
    orientation: str
    movement: str
    speed_description: Optional[str] = None


class RiderState(BaseModel):
    position: str
    body_orientation: str
    hand_positions: str
    head_orientation: str
    action: str


class AshvaState(BaseModel):
    visibility: str
    position: str
    orientation: Optional[str] = None
    movement: Optional[str] = None
    emotional_state: Optional[str] = None
    appearance_description: Optional[str] = None


class EnvironmentState(BaseModel):
    location: str
    time_of_day: str
    weather: str
    lighting: str
    road_or_terrain: str
    atmosphere: str


class FrameState(BaseModel):
    camera: CameraState
    motorcycle: MotorcycleState
    rider: RiderState
    ashva: AshvaState
    environment: EnvironmentState
    important_visual_details: list[str] = Field(default_factory=list)