from typing import Literal
from pydantic import BaseModel, Field


class ValidationIssue(BaseModel):

    category: str

    severity: Literal["low", "medium", "high", "critical"]

    description: str

    suggested_fix: str


class ValidationResult(BaseModel):

    passed: bool

    score: float = Field(ge=0, le=100)

    issues: list[ValidationIssue] = Field(default_factory=list)

    validated_components: list[str] = Field(default_factory=list)

    failed_components: list[str] = Field(default_factory=list)

    regeneration_required: bool = False

    regeneration_scope: str | None = None