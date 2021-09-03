# autonomous-car

Rest APIs to detect whether an autonomous car will be able to complete its route.
All of the code has been written and tested with python 3.8.

To run this code (Windows): 
`pip install -r requirements.txt`

This will install all the required libraries

Then run:
`python manage.py runserver` to execute the django application.

A postman collection is present in the repository. We can simply import it to postman to test all the available APIs

We have also integrated swagger to the application. To use swagger, simply run the application and navigate to: http://127.0.0.1:8000 and test the APIs accordingly.


To manually test the APIs (using postman etc.):

base url = http://127.0.0.1:8000/api/v1/autonomous-car/routes/[route]

where route can be:

* empty-route: To retrieve a route with empty track & travelLog arrays.

* success-no-obstacles: To retrieve a successful track with no obstacles.

* success-with-obstacles: To retrieve a successful track with obstacles.

* failure-out-of-bounds: To retrieve a route that should result in failure due to running out of bounds.

* failure-hits-obstacle: To retrieve a route that should result in failure due to running into an obstacle.

* random: To retrieve a random route including the empty route.
 
