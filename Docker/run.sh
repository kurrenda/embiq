#!/bin/bash
cp ../requirements.txt ./app
docker-compose -f docker-compose.yml up -d