from fastapi import APIRouter, HTTPException
from src.service.rider import RiderBase
from src.data.schemas import RiderBase
from error import Duplicate, Missing
from src.service import rider as service

router = APIRouter(prefix="/rider")

@router.get("")
@router.get("/")
def get_all() -> list[RiderBase]:
        return service.get_all()

@router.get("/{name}")
def get_one(name) -> RiderBase:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=str(exc))

@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(rider: RiderBase) -> RiderBase:
    try:
        return service.create(rider)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=str(exc))

@router.patch("/{rider_id}")
def modify(rider_id: str,rider: RiderBase) -> RiderBase:
    try:
        return service.modify(rider_id,rider)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.delete("/{rider_id}",status_code=404)
def delete(rider_id: str):
    try:
        return service.delete(rider_id )
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)