from typing import Optional

from ninja import Schema
from pydantic import Field

from lineups import constants


class LineupIn(Schema):
    title: str = Field(
        description="Lineup title",
        min_length=constants.MIN_FIELD_LENGTH,
        max_length=constants.MAX_FIELD_LENGTH,
    )
    author: Optional[str] = Field(
        description="Author name",
        min_length=constants.MIN_FIELD_LENGTH,
        max_length=constants.MAX_FIELD_LENGTH,
        default=constants.DEFAULT_AUTHOR_VALUE,
    )
    map: constants.Maps = Field(
        default=constants.Maps.MIRAGE,
    )
    grenade_type: constants.GrenadesType = Field(default=constants.GrenadesType.SMOKE)


class LineupOut(LineupIn):
    id: int
    video: Optional[str]
