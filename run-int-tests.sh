set -e

if [ -z $1 ]; then
    echo "You need to specify name of the service to run tests against."
    exit 1
fi

docker compose stop
now=$(date +%Y-%m-%dT%H:%M:%SZ)
sleep 1  # give it a break

services=("mock-server" $1)
search_strings=("Starting" "Press CTRL+C to quit")
docker compose up -d mock-server
POKEAPI_BASE_URL=http://mock-server:5000 docker compose up -d $1

MAX_WAIT=5  # seconds

for ((i = 0; i < ${#services[@]}; i++))
do
    service=${services[$i]}
    search_string=${search_strings[$i]}

    x=0
    ready=0
    while [[ $x < $MAX_WAIT && $ready == 0 ]]
    do
        echo "boom"
        found=$(docker compose logs --since=$now $service | grep "$search_string" || echo "0")

        if [[ $found == "0" ]]; then
            let remain=$MAX_WAIT-$i
            echo "Service "$service" is not ready yet. Waiting for "$remain" seconds"
            sleep 1
            let x=$x+1
            continue
        else
            ready=1
            echo "Service "$service" is ready"
        fi
    done

    if [ $ready -ne 1 ]; then
        echo "Service "$service" couldn't get started. Exiting."
        exit 1
    fi
done

docker compose run --rm -e SERVICE_HOST=$1:8080 int-tests
docker compose stop

echo "Done"
