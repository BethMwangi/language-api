
# Langauge API

A web service that returns the langauge code of a sentence passed to it

## Table of Contents

1. [Getting Started](#getting-started-docker)

### Getting Started Docker

To get started you need to have docker installed on Windows or Mac please follow this [link](https://www.docker.com/products/docker-desktop) 
for Ubuntu use this [link](https://docs.docker.com/install/linux/docker-ce/ubuntu/). 
Once downloaded clone the repository and `cd` into the repository and run the following command
```docker
docker-compose up --build
```
The command will download all the required containers and start the application to access the application
go to the browser on the url [http://localhost:5000](http://localhost:500)

To Test the application run the below requests;

```
curl -i  -X POST -H "Content-Type: application/json" -d '{"input": "My cat ate a mouse"}' http://localhost:5000/

```

```
curl -i  -X POST -H "Content-Type: application/json" -d '{"input": "Startrek is a ship"}' http://localhost:5000/

```



