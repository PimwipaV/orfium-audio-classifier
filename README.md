# orfium-audio-classifier

Since the service has to be reachable by users through endpoints that will receive requests and provide responses, I have to deploy the service somewhere on the cloud.

After some research, I decided to host my audio classifier service on **Heroku** because;

1. it’s the cheapest option to host a service ($0.01/hour max$7/month, available 24/7) compared to other similar services e.g. AWS Fargate or EC2 where my 12-month free tier has expired.

The audio classifier service is now available at https://orfium-audio-classifier-457d57532354.herokuapp.com/
**edit 07/12/23 I have turned off the server. please let me know if I should turn it on again**

2. Heroku provides **monitoring tool e.g. New Relic** as an add-on for free that can measure throughput (requests per second), response time, and memory usage without further configuration. Here’s a screenshot.

![new_relic_screenshot](https://github.com/PimwipaV/orfium-audio-classifier/assets/36345485/dcef9a28-f2ba-49bc-8d19-5342fa9f5f6b)



3. With its Procfile that I can specify numbers of workers (4 as of now), I can approximately calculate number of requests it can handle to be between **2-8 requests per second** depends on the response time of the ML component (500ms to 2 seconds). With this multi-process capability, I hope that it qualifies for ‘relatively high’ number of requests it can handle.




## Instructions to set up and run the service 
1. set up an account with Heroku. Payment information is required to create an app.

Note: I’m not subscribing to Eco Dyno plan but just use Dyno basic hour since I intend to have the service available only for the duration of this assignment. I can turn the server on or off with a toggle on resources tab on the dashboard page.

2. heroku container: login

3. git clone https://github.com/PimwipaV/orfium-audio-classifier.git

4. heroku create orfium-audio-classifier, then git add ., git commit,and git push heroku master. Basically, following the instructions from here https://devcenter.heroku.com/articles/container-registry-and-runtime

5. go to https://orfium-audio-classifier-457d57532354.herokuapp.com/ and see the app I made. If there is an error, I can do heroku logs --tail to see what happens.


## Architecture of my solution
![components_interactions](https://github.com/PimwipaV/orfium-audio-classifier/assets/36345485/769f4872-c7ee-4058-9d65-c3c1dbcd794c)
There are 4 main components in my system;
1. **Flask app** (app.py) written in Python, handling routes, application logic, and requests, with the ML component abstracted away
2. **Docker container** (Dockerfile) that packages the app and its dependencies to be able to run the app across different environments
3. **Gunicorn server** that runs my app with standardized interface (WSGI) between Python app and web servers
4. **Heroku hosting platform** where I deployed my containerized app with Procfile as its configuration

I haven’t included API Gateway at this point because now there is only 1 module and relatively high number of requests. If there are more components added to the system or the app grows in popularity, we can consider adding an API Gateway in front of the app.

Regarding error handling, there are parts in the app.py code that does the job e.g. checking if the uploading file is of allowed extension, checking if the file is present. It has also been tested for the sending of the requests to the endpoints using curl and using requests library.

So,there goes my audio classifier service.

I had fun implementing the service and looking forward to more!
