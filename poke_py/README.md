# Poke service

## How to run

```shell
docker compose up poke
```

after that, you can query the serivice like this:

```shell
http http://127.0.0.1:8080/pokemon/mewtwo
```

or 

```shell
http http://127.0.0.1:8080/pokemon/translated/mewtwo
```

To run tests:

```shell
docker compose up poke-test
```


## Rel-life Production notes

#### Deployment

In the production environment, the application service would usually be run behind a reverse proxy server like Nginx. This will take care of SSL, static file serving, buffering etc. Assuming the application will be deployed in the cloud (e.g. AWS ECS) it will also be behind a load balancer to ensure high availability and scalability.

#### Monitoring

In production, I would use a monitoring tool like Prometheus to monitor the application. I would monitor the number of requests, response times, error rates, etc. I would also monitor the underlying infrastructure like CPU, memory, disk usage, etc. I would set up alerts to notify me if something goes wrong.

#### Logging / error tracking

I would be adding structured logging to the application. I would log the request/response data with the minimum required information such as TIME - METHOD - PATH - RESPONSE CODE, RESPONSE TIME. I would also log errors with a stack trace. I would use a service like Sentry to track errors and exceptions in the application. This would help me to identify and fix issues quickly.

#### Caching

For GET requests to the Pokeapi service, I used a simple in-memory LRU cache - the data is unlikely to change frequently and using caching would improve the performance significantly. However, this specific implementation of the cache has 2 issues:

* it doesn't support TTL i.e. it will be in memory until the process killed
* it's not shared between processes/containers i.e. each of them would have its own copy

For production, however, I would use a distributed cache like Redis. It would solve both of the issues mentioned above.

#### Errors handling

Not implemented i.e. if one of the third-party services returns an error or there is a networking error happens our API would return 500. In production implementation, I would, for example, attempt to automatically retry networking errors. Also, I would add more verbose error messages to my end-users with different error codes to make it clear what's happened.

#### Testing

I only implemented unit tests. In production, depending on the importance of this logic, I may consider adding integrational tests. I would have a simple web server that would emulate third-party APIs behaviour for specific request-response and my test code would do requests against it. This way I would be able to test how different pieces of my application work together.
