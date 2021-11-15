<h1>Newsboard API | DRF + Celery + Docker </h1>
<br>
Features:
<br>
  - Show all posts: /api/read-list<br>
  - Get-Delete posts: /api/detail-news/&lt;int:pk&gt;<br>
  - Edit posts: /api/detail-news-put/&lt;int:pk&gt;<br>
  - Upvote posts: /api/upvote<br>
  - Write comment to posts: /api/comment<br>
  - Get all comments of a certain post: /api/get-comment/&lt;int:pk&gt;<br>
  - Celery task: Deletes all upvotes every 10 second <br>
  - Celery task: Deletes all upvotes every day at 10:30 am<br>
  
  <br>
  
  
  
  
  Installation using Docker:<br>
  
  ````````````
  
  git clone https://github.com/nurhesen/newsboard-docker.git
  cd newsboard-docker
  docker-compose build
  docker-compose up
  
  ````````````
  
  
  Postman file for API

``````

NewsBoard Collection.postman_collection.json

``````
  
  
  
Manual Installation Windows:<br>

Clone and install project

````````````

git clone https://github.com/nurhesen/newsboard-docker.git
cd newsboard-docker
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt

````````````

Apply migrations

````````````

python manage.py makemigrations api
python manage.py migrate

````````````

Create user with username test and password test. Important for api

````````````

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('test', 'test@test.com', 'test')" | python manage.py shell

````````````

Start the server

````````````

python manage.py runserver

````````````




Start celery worker and celery beat. This will create a task that will delete upvote counts every day at 10:30 am

``````

celery -A newsboard worker -l info
celery -A newsboard beat -l info

``````

Deployed version on heroku:<br>
https://arcane-castle-06441.herokuapp.com/api/<br><br>
(Deployed version only has the task that deletes upvotes once a day)<br><br>
Admin auth username: test<br>
Admin auth password: test<br><br>




