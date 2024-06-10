# POKE

A playground to try different technologies through implementing a REST API service.

Each service should implement the same API and being wrapped into a docker container. Then a set of integration tests will verify the implementation.

## How to add an implementation

1. Create a new folder in the root of the repo.
2. Implement the application and provide a Dockerfile.
3. Add a dedicated `docker-compose-<service-name>.yml` file to run the service.

## How to run

```shell
./run-tests.sh [service-name] [[--only-integrational] | [--only-unit]]
```
