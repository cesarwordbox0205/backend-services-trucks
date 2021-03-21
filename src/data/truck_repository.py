from .domain import Truck
import math

class TruckRepository():
    def __init__(self, driver, schema):
        self.driver = driver
        self.schema = schema
        self.set_save_query()
 
    def set_save_query(self):
        self.save_query = ["MERGE (c:Truck{objectid: $objectid})"]
        for key, value in self.schema.items():
            if(key != "objectid"):
                self.save_query.append(f"\nSET c.{value} = ${value}")
            
        self.save_query = "".join(self.save_query)
        
    def get_trucks_by_longitude_and_latitude(self, longitude, latitude):
        truck_list = []
        with self.driver.session() as session:
            for record in session.read_transaction(self._get_trucks_by_longitude_and_latitude, longitude, latitude):
                db_object = {}
                for key in self.schema.values():
                    value = record["t"][key]
                    if type(value) == int or type(value) == float:
                        db_object[key] =  value if math.isnan(value) == False else None
                    else:
                        db_object[key] = value
                truck_list.append(Truck(**db_object))
            return truck_list
        
    def get_trucks_by_params(self, params):
        truck_list = []
        with self.driver.session() as session:
            for record in session.read_transaction(self._get_trucks_by_params, params):
                db_object = {}
                for key in self.schema.values():
                    value = record["t"][key]
                    if type(value) == int or type(value) == float:
                        db_object[key] =  value if math.isnan(value) == False else None
                    else:
                        db_object[key] = value
                truck_list.append(Truck(**db_object))
            return truck_list
            
    def _get_trucks_by_longitude_and_latitude(self, tx, longitude: float, latitude: float):
            
        query = """
            MATCH (t:Truck{longitude:$longitude, latitude:$latitude})
            RETURN t
            """
        print("To query:::", longitude, latitude, type(longitude), type(latitude))
        return list(tx.run(query, longitude = longitude, latitude = latitude))
        
    def _get_trucks_by_params(self, tx, search_params):
        
        query_params = []
        params = {}
        for key, value in search_params.items():
            db_attribute = self.schema[key]
            query_params.append(f"t.{db_attribute}=${key}")
            params[key] = value
            
        query_params = " AND ".join(query_params)
            
        query = f"""
            MATCH (t:Truck)
            WHERE {query_params}
            RETURN t
            """
        return list(tx.run(query, **params))
    
    def save(self, record):
        with self.driver.session() as session:
            session.write_transaction(self.save_record, record)
                
    def save_record(self, tx, record):      

        db_data = {}
        for key, value in self.schema.items():
            if(key != "objectid"):
                db_data[value] = record[key]
                
        tx.run(self.save_query, objectid = record["objectid"], **db_data)
