## Project «API for Yatube»

Yatube - social network project. «API for Yatube» extends features of the social network. The new functionality allows users to publish their posts and manage subscriptions through a programmatic interaction interface.

### Implemented features

- Getting, creating, updating, deleting posts.
- Getting, creating, updating, deleting post comments.
- View groups and detailed information about them.
- Tracking subscriptions to authors, as well as the ability to subscribe to the author of the post of interest.
- Getting, updating and checking JWT authorization.

### Technologies

- [Python](https://www.python.org/) - programming language.
- [Django](https://www.djangoproject.com/) - a free framework for web applications in Python.
- [Django REST Framework](https://www.django-rest-framework.org/) - a powerful and flexible set of tools for creating web APIs.
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - JSON Web Token Authentication Plugin for Django REST Framework.

### How to deploy the project:

Clone the repository and go to it on the command line:

`git clone https://github.com/DanikKravets/api_final_yatube.git`

`cd api_final_yatube`


Create and activate a virtual environment:

+ `python3 -m venv env`
+ `source env/bin/activate`
+ `python3 -m pip install --upgrade pip`

Install dependencies from a file requirements.txt:
`pip install -r requirements.txt`

Perform migrations:
`python3 manage.py migrate`


Run the project:
`python3 manage.py runserver`
#### After the project is launched, the documentation will be available at:
`http://localhost:port/redoc/`

#### Request examples:

POST-request with token, adding new post to the post collection.

`POST http://localhost:port/api/v1/posts/`

```
{
  "text": "Test text 1",
  "group": 1
}
```

Response:

```
{
    "id": 9,
    "author": "your_username",
    "text": "Test text 1",
    "pub_date": "2023-03-16T18:11:48.247905Z",
    "image": null,
    "group": 1
}
```


GET-request, getting information about group id=2.

`GET http://localhost:port/api/v1/groups/2/`

Response:

```
{
    "id": 2,
    "title": "group2",
    "slug": "group2",
    "description": "group2"
}
```

POST-request, subscription of an authorized user `user=root` on whose behalf a request was made for the author of the publication of interest `following=admin`.

`POST http://localhost:port/api/v1/follow/`

```
{
  "following": "admin"
}
```

Response:

```
{
    "id": 6,
    "user": "your_username",
    "following": "admin"
}
```