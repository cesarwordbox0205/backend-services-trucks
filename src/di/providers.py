import os

from bp import TruckService
from data import TruckRepository, truck_schema
from fastapi import Depends
from neo4j import GraphDatabase
from neo4j import Neo4jDriver

URI_KEY = "NEO4J_URI"
USER_KEY = "NEO4J_USER"
PASSWORD_KEY = "NEO4J_PASS"

def neo4j_driver_module() -> Neo4jDriver:
    uri_db = os.environ.get(URI_KEY)
    user_db = os.environ.get(USER_KEY)
    password_db = os.environ.get(PASSWORD_KEY)
    return GraphDatabase.driver(uri_db, auth=(user_db, password_db))

def truck_repository_module(
    driver: Neo4jDriver = Depends(neo4j_driver_module),
) -> TruckRepository:
    return TruckRepository(driver, truck_schema)

def truck_service_module(
    truck_repository: TruckRepository = Depends(
        truck_repository_module
    )
) -> TruckService:
    return TruckService(truck_repository)
