# СourseCatalog

СourseCatalog is a simple crud api with [Django REST framework](http://www.django-rest-framework.org/).

## Requirements
- Python 3.7.10
- Django 3.2
- Django REST Framework 3.12.4
- Django-filter 2.4.0  

## Installation
After you cloned the repository, you can create a virtual environment, so you have a clean python installation. After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html).

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single resource, `Courses`, so we will use the following URLS (endpoints):
 - `/api/courses_create` 
    - _HTTP Method - POST_
    - _CRUD Method - CREATE_
    - _Result - Create a new course_
 - `/api/courses_list`
    - _HTTP Method - GET_
    - _CRUD Method - READ_
    - _Result - Get a list of courses_
 - `/api/courses_list/<int:pk>` 
    - _HTTP Method - GET, PUT, PATCH, DELETE_
    - _CRUD Method - READ, UPDATE, DELETE_
    - _Result - Get full information about course, update course attributes(all or partial) or delete a course_

__*** Be aware! A trailing forward slash (/) should not be included in URIs_, the authoritative reference on URI is [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt), Section 3.3._

For example, `/api/courses_create` and `/api/courses_create/` would be treated as two different identifiers.

However, for this project I've added urls normalization for your convenience, so fell free to use trailing slash. 

## Use
We can test the API directly from the user-friendly Web Interface (via Django REST Framework), or we can use [Postman](https://www.postman.com/).

First, we have to start up Django's development server.
```
python manage.py runserver
```
#### Hence, the required urls are:
- Create a new course:
    - ```http://127.0.0.1:8000/api/courses_create```
- Get a list of courses:
    - ```http://127.0.0.1:8000/api/courses_list```
- Get full information about course, update course attributes(all or partial) or delete a course:
    - ```http://127.0.0.1:8000/api/courses_list/<int:pk>```

#### For each course, the following field is required:
- "title": _(name of course, text, max length: 100)_
- "start_date": _(start date of course in format YYYY-MM-DD, date)_
- "end_date": _(end date of course in format YYYY-MM-DD, date)_
- "num_of_lectures": _(numbers of lectures, integer)_
    
If you choose use Postman or API Web Interface within raw data next json examples should be useful for you.

#### JSON raw data examples

- Create a new course:
```
{"title":"BEST COURSES FROM Yalantis Python School","start_date":"2021-05-17","end_date":"2021-08-16","num_of_lectures":100}
```
- Update all course attributes:

``` 
{"title":"GIT Course","start_date":"2021-05-17","end_date":"2021-05-30","num_of_lectures":5} 
```
- Update partial course attribute:
``` 
{"title":"Flask Course"}
OR
{"title":"GIT Course","start_date":"2021-05-17"}
OR
{"end_date":"2021-05-30","num_of_lectures":5} 
  
```


### Filters
The API supports filtering/multi-filtering, you can filter by the title of a course ```title=```, or start_date ```start_date=``` and 
end_date ```end_date=```
```
http://127.0.0.1:8000/api/courses_list?title=TEST+COURSE
OR
http://127.0.0.1:8000/api/courses_list?start_date=2021-05-03
OR
http://127.0.0.1:8000/api/courses_list?end_date=2021-08-03
```

You can also combine multiples filters like so
```
http://127.0.0.1:8000/api/courses_list?title=TEST+COURSE&start_date=2021-05-03&end_date=2021-08-03
```
