from typing import List

from ninja import File, Router, UploadedFile
from ninja.pagination import paginate

from api import crud
from lineups import constants
from lineups.models import Lineup
from lineups.schemas import LineupIn, LineupOut

router = Router(tags=["lineups"])
LINEUP_CRUD = crud.DatabaseCrud(Lineup)


@router.get("/{lineup_id}", response=LineupOut)
async def get_object(request, lineup_id: int):
    instance = await LINEUP_CRUD.get(lineup_id)
    return instance


@router.get("", response=List[LineupOut])
@paginate
async def get_list(
    request, grenade_type=constants.GrenadesType.SMOKE, maps=constants.Maps.MIRAGE
):
    queryset = await LINEUP_CRUD.list(grenade_type=grenade_type, map=maps)
    return list(queryset)


@router.post("", response=LineupOut)
async def post(request, payload: LineupIn, video: File[UploadedFile]):
    instance = await LINEUP_CRUD.create(**payload.dict(), video=video)
    return instance
