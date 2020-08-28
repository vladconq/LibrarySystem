# LibrarySystem

The development of this system is part of the test task.

```
cd backend
pip install -r requirements.txt
python manage.py runserver
cd ..
cd frontend
index.html
```

The system consists of back-end and front-end parts.

The backend handles the following requests:
```
api/authors/ - get list of authors
api/shelves/ - get list of shelves
api/authors/<str:author_name>/books/ - get list of books for specific author
api/shelves/<str:shelf_name>/shelves/ - get list of books for specific shelf
```
