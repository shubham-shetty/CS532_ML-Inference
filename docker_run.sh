#!/bin/bash

IMG_NAME="sshorewala/img-class-server"
CONTAINER_NAME="densenet"

echo "\nDownloading image $IMG_NAME from DockerHub"
docker pull $IMG_NAME

echo "\nRunning a container $CONTAINER_NAME derived from image $IMG_NAME"

# check if container derived from the image is running
if [ ! "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
	if [ "$(docker ps -aq -f status=exited -f name=$CONTAINER_NAME)" ]; then
		docker rm $CONTAINER_NAME
	fi 
	docker run -p 5000:5000 --name $CONTAINER_NAME $IMG_NAME
	docker ps
fi

echo "Running classification using DenseNet"
# docker run $IMG_NAME
curl -F "query=@data/images/dog.jpeg" http://localhost:5000/v1/densenet-inference/prediction
