set -e
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

if [ -z $1 ]; then
    echo "${RED}You need to specify a language code of the service for which you want to run tests e.g. py${NC}"
    exit 1
fi

fname="docker-compose-"$1".yml"

if [[ ! -f $fname ]]; then
    echo "${RED}File "$fname" does not exist you need to create one for your implementation.${NC}"
    exit 1
fi

run_integrational=1
run_unit=1

if [[ $2 == "--only-integrational" ]]; then
    run_integrational=1
    run_unit=0
elif [[ $2 == "--only-unit" ]]; then
    run_integrational=0
    run_unit=1
elif [[ ! -z $2 ]]; then
    echo "${RED}Unknow parameter: $2 ${NC}"
    exit 1
fi

cmd="docker compose -f docker-compose-base.yml -f "$fname

if [[ $run_unit == 1 ]]; then
    echo "\n\n${GREEN}Running unit tests${NC}\n\n"
    $cmd run --rm poke-unit
fi


if [[ $run_integrational == 1 ]]; then
    echo "\n\n${GREEN}Running integrational tests${NC}\n\n"
    $cmd run --rm int-tests
fi

$cmd stop

echo "${GREEN}Done${NC}"
