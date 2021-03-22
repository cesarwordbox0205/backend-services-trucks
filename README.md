# Backend-Services-Trucks
Service to retrieve information regarding trucks status

The application is divided in two services:

* A backend service that fetches the truck dataset at regular intervals (3 min) using
  a python script that is launched by a cron job.
    * It downloads the dataset in a csv file.
    * Checks whether the file has changed its content since the last time it was downloaded using a md5 file checksum.
    * Cleans and processes the data in a pandas dataframe.
    * Saves the data in the db.
    * Saves the last generated md5 checksum.

* A web service to retrieve truck information. It has two endpoints,
  one to get a truck list by latitude and longitude and another to get a truck list by an
  arbitrary number of parameters.

The database is mounted in an external service in the cloud for scalability purposes. It uses
neo4j that is a nonsql database.

This project can be lauched locally using the docker-compose file or in the cloud by setting a CD/CI job. Specifically Google Cloud Build is a tool similar to Jenkins that builds images (CI) and lauches virtual machines (CD) via a configuration file.

When lauching the web application there is a prestart.sh script that is excecuted before the worker nodes are initialized. The script starts a the cron job responsible of executing the dataset fetcher application.

## Quick Start

### Build your Image

* Clone the latest stable version of the `backend-services-trucks` repository.

```
git clone https://github.com/cesarwordbox0205/backend-services-trucks.git
```

* Navigate to the `backend-services-trucks` directory and enter in it.
* Build the docker image:

```bash

docker-compose build

```

### Launch the application

* Launch the application with:

```bash

docker-compose up

```

* You can then make local API calls to the following endpoints using POSTMAN or any other REST client.

### Make API calls.


* In order to get the truck list based on the longitude and latitude we call the GET endpoint `apis/get_trucks_by_get_trucks_by_longitude_and_latitude` with the longitude and latitude parameters. Eg.

```

http://localhost:80/apis/get_trucks_by_longitude_and_latitude/1.0.0?latitude=37.79092150726921&longitude=-122.4001004237385

```

* In order to get a truck list based on an arbitrary number of parameters then call the POST endpoint `apis/get_trucks_by_params/1.0.0` along with a json body containing the parameters to perform the search.

```

http://localhost:80/apis/get_trucks_by_params/1.0.0

```

```JSON

{"params":{"latitude": 37.79092150726921, "longitude": -122.4001004237385}}

```

### Check backend dataset service logs.


* To check the logs created by the backend service we need to get into the container.

```

docker exec -it backend-services-trucks_truck_service_1 /bin/bash

```

* The logs are stored in the file dataset_fetch.log. Then to retrieve the last 50
lines use the tail command.

```

tail -n 50 dataset_fetch.log

```


