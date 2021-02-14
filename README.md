# Xmeme- Post Memes and Chat

This Project consist of two Parts:
- Xmeme Backend  
- Xmeme Frontend  

## Xmeme Frontend

Fontend Part of App is made with React and is being deployed to netlify, it has features of adding post, deleting post and edit the same.  


## Xmeme Backend

This is backend of Xmeme is an Api hosted on Heroku, built with Django Rest Framework, it has a database of Sqlite3. It has basically 3 feilds, name, caption, url resp. api return two formt of Data one in Json, other in API format.  
Link to Backend: <a href="https://crio-xmeme.herokuapp.com/api/">Xmeme-Backend</a>

### Frontend Dependencies

`npm install bootstrap reactstrap axios react-icons netlify `

### Running the frontend and deploying to netlify

Build Frontend: `npm run build `  
Deploy Frontend: `netlify deploy`  
Enter publish directrory as build, then check the draft url for your dummy website.

Finaly Deploy in Production Mode: `netlify deploy --prod`

### Backend Dependencies

`pip django djangorestframework django-cors-headers`

### Running the frontend and deploying to netlify

```
cd backend  
python manage.py makemigrations  
python manage.py migrate
python manage.py runserver

```
Deploy on Heroku by connecting with Github.


✅Make sure net connection is good to avoid buffering while running the app.  
✅Feel Free to add more Features to this todo, Just Raise an Issue and then create a pull request to get your pull request merged. if you like this don't forget to ⭐(star) or (frok) this repository.
