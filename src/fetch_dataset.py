import google.cloud.logging
from dotenv import load_dotenv
from di import providers

load_dotenv()

client = google.cloud.logging.Client()
client.setup_logging()


if __name__ == "__main__":
    
    neo4j_driver = providers.neo4j_driver_module()
    truck_repository = providers.truck_repository_module(neo4j_driver)
    fetch_service = providers.fetch_service_module(truck_repository)

    fetch_service.process_data()