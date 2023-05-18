# Web stack Debugging PART 4

In this debugging episode, we are testing how well our web server setup featuring Nginx is doing under pressure. Turns out it's NOT doing well: we are getting a hug amount of failed requests.

We are using **ApacheBench** which is quite popular tool in the industry.
  * It allows you to simulate HTTP requests to a web server.
In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!