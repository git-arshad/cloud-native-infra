#!/bin/bash

echo"Starting deployment..."

cd ~/cloud-native-infra

echo "Pulling latest code..."
git pull

echo "Stopping old containers..."
docker-compose down

echo "Starting new containers..."
docker-compose up -d --build

echo "Deployment complete!"
