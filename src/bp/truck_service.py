from typing import Dict
from data import TruckRepository

class TruckService:

    def __init__(self, truck_repository):
        self.truck_repository = truck_repository

    def get_trucks_by_longitude_and_latitude(self, longitude: float, latitude: float):
        return self.truck_repository.get_trucks_by_longitude_and_latitude(longitude = longitude, 
                                                                            latitude = latitude)

    def get_trucks_by_params(self, params: Dict):
        return self.truck_repository.get_trucks_by_params(params)
        

