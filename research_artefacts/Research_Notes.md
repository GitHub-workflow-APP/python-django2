## ToDo:
- Exception handling. 
	-	Does normal out of box, has any sinks ?
	-  Overiding, adds sinks, may be in template files.
- Captured parameters
	- path('<username>/blog/', include('foo.urls.blog')),  # username is tainted.
- included urls
- When urls are not only in urls.py files.
- When views are not just in views.py files.
- url template tag possible sinks
- reverse() and get_absolute_url() functions. Possible sinks 
- How dangerous is having an admin/ module enabled by default ? 
- Flag for Debug = False
- Allowed_Host is overly inclusive
- CSRF Protection is disabled globally ?
- SECURE_SSL_REDIRECT = False
- CSRF_COOKIE_SECURE = False
	
## Other Django Frameworks/Projects more commonly seen.
- django rest framework
- django braces

- from documentation, common use cases:
	- authentication usecase
	- logging
	
## Ask Static:

- Past/Present/Future of our python support, and django framework and Django template
- Point me to some saf code, to refer our exact modeling details.
- Any simple way to run python scanner on laptop, rather than going thru analysiscenter each time?
- General risk of python sinks
- What is the deal with RT files of templates ?
- Do we support filters (safe == XSS)?
- How well do we look for view methods... Everything from Django1 research pages?
- Once, view methods are identified, how well do we map it to corresponding templates ?


1/16:
- How do we handle inheritance ? HttpResponse and all its subclasses should be treated as sinks

## Testcases:
- Single project, containing multiple apps.
- 	add include() to include sub-apps, urls into parent project
- single app, added on multiple projects, via PYTHON_PATH 
- Work on a File Upload example, ass request.FILES Tainted SOURCE to it.


# Nice to add support for:
- re_path, regular expressions... groups etc. "Each captured argument is sent to the view as a string, regardless of what sort of match the regular expression makes."

# Dig Deeper:
- Couldn't find a way, where positional arguments could be passed to non-regular expression based configs.

# Won't Support:
- Regular expression in URLConf. 
- ```*args``` is not considered tainted, in view class entry points, since its used in conjuction with re_path. There would be no way to know, args is being matched to a clean data, or not. 