# PetClinic Load Test

This tool simulates the creation of new owner data for the PetClinic Java application - https://hub.docker.com/repository/docker/grdnr/spring-petclinic

### Parameters
* `[host]` - The hostname (and port if applicable) where the application is exposed. (Required)
* `[number of clients]` - The nuber of concurrent end users to simulate. (Optional: Default is 2)
* `[number of requests]` - The total number of requests to run before terminating the tests. (Optional: Default is 10)

## Running in Docker Container
* Build `docker build -t load-test .`
* Run `docker run load-test -h [host] -c [number of clients] -r [number of requests]`

## Running in Kubernetes
