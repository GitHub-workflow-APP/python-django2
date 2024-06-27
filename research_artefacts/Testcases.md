# Simpleapp
Class inheriting TemplateView, and passing just template_name, gives entire request object access to corresponding templates

```
msheth-mbp:django2-simpleapp msheth$ curl 'http://localhost:8000/class_based_view/about/?name=<script>alert(123)</script>'
<h1>Simple Class Based View - Abount Us</h1>
request.META.QUERY_STRING : name=<script>alert(123)</script> 
msheth-mbp:django2-simpleapp msheth$ 

```



# Polling App

# Try Django 2 App - non-basic views
- created superuser msheth/msheth using
``` python manage.py createsuperuser ```

blog app - uses CreateView, ListView, DetailView, UpdateView, DeleteView:

- http://localhost:8000/admin, created another user mansi/adminadmin
- Create blog entries : http://localhost:8000/blog/create
- View particular blog entry: http://localhost:8000/blog/<1>
- Update blog entry: http://localhost:8000/blog/1/update/
- Delete blog entry: http://localhost:8000/blog/1/update/


course app - Custom mixin, Views

- Create course entries : http://localhost:8000/courses/create
- View particular course entry: http://localhost:8000/courses/<1>
- Update course entry: http://localhost:8000/courses/1/update/
- Delete course entry: http://localhost:8000/courses/1/update/

product app - uses function views

- Create products entries : http://localhost:8000/products/create
- View particular products entry: http://localhost:8000/products/<1>
- Update products entry: http://localhost:8000/products/1/update/
- Delete products entry: http://localhost:8000/products/1/update/

pages - function based views

# Educa App
Created superuser to login to app.

```
python manage.py createsuperuser
Username (leave blank to use 'msheth'): admin
Email address: admin@admin.com
Password: 
Password (again): 
The password is too similar to the email address.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```