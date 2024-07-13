# ci-cd

This repo is for working and understanding CI-CD on our infra. 


Application : 
The Flask microservice will be accessible at http://localhost:5000/data, and it will return a JSON array containing the data items when a GET request is made.


Docker commands 
docker build -t flask-microservice .
docker run -p 5000:5000 flask-microservice
