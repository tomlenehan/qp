#!/usr/bin/env bash

# get this script's directory path
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# source docker-compose environment variables
. "$DIR/../.env"

# build docker image
alias qp-build="docker build -t qp ."

