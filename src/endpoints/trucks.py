import logging

from bp import TruckService
from di import providers
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from pydantic import BaseModel
from typing_extensions import Final
from typing import Dict
import logging

router = APIRouter()
STATUS: Final = "status"

CODE = "code"
MESSAGE = "message"
ITEMS = "items"
PAGE = "page"

class Data(BaseModel):
    params: Dict

@router.get("/apis/get_trucks_by_longitude_and_latitude/1.0.0", tags=["trucks"])
async def get_trucks_by_longitude_and_latitude(
    longitude: float,
    latitude: float,
    response: Response,
    truck_service: TruckService = Depends(
        providers.truck_service_module
    )
):
    try:
        logging.info("Longitude {} and latitude {} received".format(longitude, latitude))
        truck_list = truck_service.get_trucks_by_longitude_and_latitude(
                longitude, latitude
            )

        return {
            ITEMS: [truck.to_json() for truck in truck_list]
        }

    except Exception as e:
        logging.error("Fatal error in get_trucks_by_longitude_and_latitude", exc_info=True)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {CODE: 500, MESSAGE: str(e)}


@router.post("/apis/get_trucks_by_params/1.0.0", tags=["trucks"])
async def get_trucks_by_params(
    data: Data,
    response: Response,
    truck_service: TruckService = Depends(
        providers.truck_service_module
    )
):
    logging.info("Params received {}".format(data.params))
    try:
        truck_list = truck_service.get_trucks_by_params(
                data.params
            )
        return {
            ITEMS: [truck.to_json() for truck in truck_list]
        }
    except Exception as e:
        logging.error("Fatal error in get_trucks_by_params", exc_info=True)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {CODE: 500, MESSAGE: str(e)}