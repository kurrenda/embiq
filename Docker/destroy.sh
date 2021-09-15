#!/bin/bash
docker-compose -f docker-compose.yml stop
rm -rf ./app/requirements.txt
docker-compose -f docker-compose.yml rm -f
