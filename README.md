# Backend-Services-Trucks
Service to retrieve information regarding trucks status

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

docker-compose up -d

```

* You can then make local API calls to the following endpoints using POSTMAN or any other REST client.

### Make API calls.


* In order to get the trucks based on the longitude and latitude we can call the GET endpoint `apis/get_trucks_by_get_trucks_by_longitude_and_latitude` with the longitude and latitude parameters set. Eg.

```

http://localhost:80/apis/get_trucks_by_longitude_and_latitude/1.0.0?latitude=37.79092150726921&longitude=-122.4001004237385

```

* In order to get the trucks based on an arbitrary number of parameters that the application support then call the POST endpoint `apis/get_trucks_by_params/1.0.0` along with a json body containing the parameters we want to call the service with.

```

http://localhost:80/apis/get_trucks_by_params/1.0.0

```

```JSON

{"params":{"latitude": 37.79092150726921, "longitude": -122.4001004237385}}

```
