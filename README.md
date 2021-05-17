# Team 7

* Team Members:
	* Dhruv Agarwal (dagarwal@umass.edu)
	* Shantam Shorewala (sshorewala@umass.edu)
	* Shubham Shetty (shubhamshett@umass.edu)


## Test Script

The below command pulls the docker image from DockerHub, starts a container, and sends a classification request for `data/dog.jpeg`: 
````
sh docker_run.sh 
````

## Step-wise Instructions
* To download the pre-built image from DockerHub:
````
docker pull sshorewala/img-class-server
````
* To start a container from the pulled image:
````
docker run -p 5000:5000 sshorewala/img-class-server --name mlinf-team-7
````
* To run inference against the provided test image, execute (from project root):
```
curl -F "query=@data/images/zeppelin.jpg" http://localhost:5000/v1/densenet-inference/prediction
```
* To build the docker image locally:
````
docker build -t img-class-server .  
````
