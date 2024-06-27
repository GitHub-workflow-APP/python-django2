## django.http.HttpRequest arguments for tainted source

```
Arguments: (['COOKIES', // Tainted SOURCE
				'FILES', // Tainted SOURCE
				'GET', // Tainted SOURCE
				'META', // Tainted SOURCE
				'POST', // Tainted SOURCE
				'body', // Tainted SOURCE
				'build_absolute_uri', // Test, not a TAINTED SOURCE, outputs encoded
				'close', 
				'content_params', // Tested, not a TAINTED SOURCE
				'content_type', 
				'encoding', // Tainted SOURCE
				'environ', 
				'get_full_path', // Tainted SOURCE
				'get_full_path_info', // Test, not a TAINTED SOURCE, outputs encoded
				'get_host', 
				'get_port', 
				'get_raw_uri', // Tested, not a TAINTED SOURCE, outputs encoded
				'get_signed_cookie', 
				'is_ajax', 
				'is_secure', 
				'method', 
				'parse_file_upload', 
				'path', // Tainted SOURCE
				'path_info', // Tainted SOURCE
				'read', // Tainted SOURCE
				'readline', // Tainted SOURCE
				'readlines', // Tainted SOURCE
				'resolver_match', 
				'scheme', 
				'session', 
				'upload_handlers', 
				'user', 
				'xreadlines'// Tainted SOURCE
				],)
```

## django.http for Tainted SINKS

```
(testcases) msheth-mbp:class_hierarchy msheth$ python tree_generator.py django.http
		C: django.http.multipartparser.BoundaryIter [ django.http.multipartparser.BoundaryIter , builtins.object]
		C: django.http.multipartparser.ChunkIter [ django.http.multipartparser.ChunkIter , builtins.object]
		C: django.http.multipartparser.InputStreamExhausted [ django.http.multipartparser.InputStreamExhausted , builtins.Exception , builtins.BaseException , builtins.object]
			P: args <attribute 'args' of 'BaseException' objects>
		C: django.http.multipartparser.InterBoundaryIter [ django.http.multipartparser.InterBoundaryIter , builtins.object]
		C: django.http.multipartparser.LazyStream [ django.http.multipartparser.LazyStream , builtins.object]
			F: close(self)
			F: read(self,size)
			F: tell(self)
			F: unget(self,bytes)
		C: django.http.multipartparser.MultiPartParser [ django.http.multipartparser.MultiPartParser , builtins.object]
			F: IE_sanitize(self,filename)
			F: handle_file_complete(self,old_field_name,counters)
			F: parse(self)
		C: django.http.multipartparser.MultiPartParserError [ django.http.multipartparser.MultiPartParserError , builtins.Exception , builtins.BaseException , builtins.object]
			P: args <attribute 'args' of 'BaseException' objects>
		C: django.http.multipartparser.Parser [ django.http.multipartparser.Parser , builtins.object]
		C: django.http.request.HttpRequest [ django.http.request.HttpRequest , builtins.object]
			P: body <property object at 0x10d7b6f48>
			P: encoding <property object at 0x10d7d85e8>
			P: scheme <property object at 0x10d547ef8>
			P: upload_handlers <property object at 0x10d7d8638>
			F: build_absolute_uri(self,location)
			F: close(self)
			F: get_full_path(self,force_append_slash)
			F: get_full_path_info(self,force_append_slash)
			F: get_host(self)
			F: get_port(self)
			F: get_raw_uri(self)
			F: get_signed_cookie(self,key,default,salt,max_age)
			F: is_ajax(self)
			F: is_secure(self)
			F: parse_file_upload(self,META,post_data)
			F: read(self,args,kwargs)
			F: readline(self,args,kwargs)
			F: readlines(self)
			F: xreadlines(self)
		C: django.http.request.QueryDict [ django.http.request.QueryDict , django.utils.datastructures.MultiValueDict , builtins.dict , builtins.object]
			P: encoding <property object at 0x10d7d8728>
			M: fromkeys(iterable,value,mutable,encoding)
			F: appendlist(self,key,value)
			F: clear(self)
			F: copy(self)
			F: dict(self)
			F: get(self,key,default)
			F: getlist(self,key,default)
			F: items(self)
			F: lists(self)
			F: pop(self,key,args)
			F: popitem(self)
			F: setdefault(self,key,default)
			F: setlist(self,key,list_)
			F: setlistdefault(self,key,default_list)
			F: update(self,args,kwargs)
			F: urlencode(self,safe)
			F: values(self)
		C: django.http.request.RawPostDataException [ django.http.request.RawPostDataException , builtins.Exception , builtins.BaseException , builtins.object]
			P: args <attribute 'args' of 'BaseException' objects>
		C: django.http.request.UnreadablePostError [ django.http.request.UnreadablePostError , builtins.OSError , builtins.Exception , builtins.BaseException , builtins.object]
			P: args <attribute 'args' of 'BaseException' objects>
			P: characters_written <attribute 'characters_written' of 'OSError' objects>
			P: errno <member 'errno' of 'OSError' objects>
			P: filename <member 'filename' of 'OSError' objects>
			P: filename2 <member 'filename2' of 'OSError' objects>
			P: strerror <member 'strerror' of 'OSError' objects>
		C: django.http.response.BadHeaderError [ django.http.response.BadHeaderError , builtins.ValueError , builtins.Exception , builtins.BaseException , builtins.object]
			P: args <attribute 'args' of 'BaseException' objects>
		C: django.http.response.FileResponse [ django.http.response.FileResponse , django.http.response.StreamingHttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: block_size 4096
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc1908>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 200
			P: streaming True
			P: streaming_content <property object at 0x10dcc19a8>
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_headers(self,filelike)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.Http404 [ django.http.response.Http404 , builtins.Exception , builtins.BaseException , builtins.object]
			P: args <attribute 'args' of 'BaseException' objects>
		C: django.http.response.HttpResponse [ django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 200
			P: streaming False
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseBadRequest [ django.http.response.HttpResponseBadRequest , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 400
			P: streaming False
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseBase [ django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 200
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseForbidden [ django.http.response.HttpResponseForbidden , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 403
			P: streaming False
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseGone [ django.http.response.HttpResponseGone , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 410
			P: streaming False
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseNotAllowed [ django.http.response.HttpResponseNotAllowed , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 405
			P: streaming False
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseNotFound [ django.http.response.HttpResponseNotFound , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 404
			P: streaming False
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseNotModified [ django.http.response.HttpResponseNotModified , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc1c28>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 304
			P: streaming False
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponsePermanentRedirect [ django.http.response.HttpResponsePermanentRedirect , django.http.response.HttpResponseRedirectBase , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: allowed_schemes ['http', 'https', 'ftp']
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 301
			P: streaming False
			P: url <property object at 0x10dcc1a48>
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseRedirect [ django.http.response.HttpResponseRedirect , django.http.response.HttpResponseRedirectBase , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: allowed_schemes ['http', 'https', 'ftp']
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 302
			P: streaming False
			P: url <property object at 0x10dcc1a48>
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseRedirectBase [ django.http.response.HttpResponseRedirectBase , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: allowed_schemes ['http', 'https', 'ftp']
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 200
			P: streaming False
			P: url <property object at 0x10dcc1a48>
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.HttpResponseServerError [ django.http.response.HttpResponseServerError , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 500
			P: streaming False
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.JsonResponse [ django.http.response.JsonResponse , django.http.response.HttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc18b8>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 200
			P: streaming False
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)
		C: django.http.response.StreamingHttpResponse [ django.http.response.StreamingHttpResponse , django.http.response.HttpResponseBase , builtins.object]
			P: charset <property object at 0x10dcc17c8>
			P: content <property object at 0x10dcc1908>
			P: reason_phrase <property object at 0x10dcc1778>
			P: status_code 200
			P: streaming True
			P: streaming_content <property object at 0x10dcc19a8>
			F: close(self)
			F: delete_cookie(self,key,path,domain)
			F: flush(self)
			F: get(self,header,alternate)
			F: getvalue(self)
			F: has_header(self,header)
			F: items(self)
			F: make_bytes(self,value)
			F: readable(self)
			F: seekable(self)
			F: serialize_headers(self)
			F: set_cookie(self,key,value,max_age,expires,path,domain,secure,httponly,samesite)
			F: set_signed_cookie(self,key,value,salt,kwargs)
			F: setdefault(self,key,value)
			F: tell(self)
			F: writable(self)
			F: write(self,content)
			F: writelines(self,lines)

```

```
		C: django.views.generic.base.RedirectView [ django.views.generic.base.RedirectView , django.views.generic.base.View , builtins.object]
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: pattern_name None
			P: permanent False
			P: query_string False
			P: url None
			M: as_view(initkwargs)
			F: delete(self,request,args,kwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_redirect_url(self,args,kwargs)
			F: head(self,request,args,kwargs)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: patch(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
			F: put(self,request,args,kwargs)
		C: django.views.generic.base.TemplateView [ django.views.generic.base.TemplateView , django.views.generic.base.TemplateResponseMixin , django.views.generic.base.ContextMixin , django.views.generic.base.View , builtins.object]
			P: content_type None
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_template_names(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.base.View [ django.views.generic.base.View , builtins.object]
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
		
		C: django.views.generic.detail.BaseDetailView [ django.views.generic.detail.BaseDetailView , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.base.View , builtins.object]
			P: context_object_name None
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: pk_url_kwarg pk
			P: query_pk_and_slug False
			P: queryset None
			P: slug_field slug
			P: slug_url_kwarg slug
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_object(self,queryset)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
		C: django.views.generic.detail.DetailView [ django.views.generic.detail.DetailView , django.views.generic.detail.SingleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.detail.BaseDetailView , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.base.View , builtins.object]
			P: content_type None
			P: context_object_name None
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: pk_url_kwarg pk
			P: query_pk_and_slug False
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: slug_field slug
			P: slug_url_kwarg slug
			P: template_engine None
			P: template_name None
			P: template_name_field None
			P: template_name_suffix _detail
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_object(self,queryset)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_template_names(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.edit.BaseCreateView [ django.views.generic.edit.BaseCreateView , django.views.generic.edit.ModelFormMixin , django.views.generic.edit.FormMixin , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.edit.ProcessFormView , django.views.generic.base.View , builtins.object]
			P: context_object_name None
			P: extra_context None
			P: fields None
			P: form_class None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: initial {}
			P: model None
			P: pk_url_kwarg pk
			P: prefix None
			P: query_pk_and_slug False
			P: queryset None
			P: slug_field slug
			P: slug_url_kwarg slug
			P: success_url None
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: form_invalid(self,form)
			F: form_valid(self,form)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_form(self,form_class)
			F: get_form_class(self)
			F: get_form_kwargs(self)
			F: get_initial(self)
			F: get_object(self,queryset)
			F: get_prefix(self)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_success_url(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
			F: put(self,args,kwargs)
		C: django.views.generic.edit.BaseDeleteView [ django.views.generic.edit.BaseDeleteView , django.views.generic.edit.DeletionMixin , django.views.generic.detail.BaseDetailView , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.base.View , builtins.object]
			P: context_object_name None
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: pk_url_kwarg pk
			P: query_pk_and_slug False
			P: queryset None
			P: slug_field slug
			P: slug_url_kwarg slug
			P: success_url None
			M: as_view(initkwargs)
			F: delete(self,request,args,kwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_object(self,queryset)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_success_url(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
		C: django.views.generic.edit.BaseFormView [ django.views.generic.edit.BaseFormView , django.views.generic.edit.FormMixin , django.views.generic.base.ContextMixin , django.views.generic.edit.ProcessFormView , django.views.generic.base.View , builtins.object]
			P: extra_context None
			P: form_class None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: initial {}
			P: prefix None
			P: success_url None
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: form_invalid(self,form)
			F: form_valid(self,form)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_form(self,form_class)
			F: get_form_class(self)
			F: get_form_kwargs(self)
			F: get_initial(self)
			F: get_prefix(self)
			F: get_success_url(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
			F: put(self,args,kwargs)
		C: django.views.generic.edit.BaseUpdateView [ django.views.generic.edit.BaseUpdateView , django.views.generic.edit.ModelFormMixin , django.views.generic.edit.FormMixin , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.edit.ProcessFormView , django.views.generic.base.View , builtins.object]
			P: context_object_name None
			P: extra_context None
			P: fields None
			P: form_class None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: initial {}
			P: model None
			P: pk_url_kwarg pk
			P: prefix None
			P: query_pk_and_slug False
			P: queryset None
			P: slug_field slug
			P: slug_url_kwarg slug
			P: success_url None
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: form_invalid(self,form)
			F: form_valid(self,form)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_form(self,form_class)
			F: get_form_class(self)
			F: get_form_kwargs(self)
			F: get_initial(self)
			F: get_object(self,queryset)
			F: get_prefix(self)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_success_url(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
			F: put(self,args,kwargs)
		C: django.views.generic.edit.CreateView [ django.views.generic.edit.CreateView , django.views.generic.detail.SingleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.edit.BaseCreateView , django.views.generic.edit.ModelFormMixin , django.views.generic.edit.FormMixin , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.edit.ProcessFormView , django.views.generic.base.View , builtins.object]
			P: content_type None
			P: context_object_name None
			P: extra_context None
			P: fields None
			P: form_class None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: initial {}
			P: model None
			P: pk_url_kwarg pk
			P: prefix None
			P: query_pk_and_slug False
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: slug_field slug
			P: slug_url_kwarg slug
			P: success_url None
			P: template_engine None
			P: template_name None
			P: template_name_field None
			P: template_name_suffix _form
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: form_invalid(self,form)
			F: form_valid(self,form)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_form(self,form_class)
			F: get_form_class(self)
			F: get_form_kwargs(self)
			F: get_initial(self)
			F: get_object(self,queryset)
			F: get_prefix(self)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_success_url(self)
			F: get_template_names(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
			F: put(self,args,kwargs)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.edit.DeleteView [ django.views.generic.edit.DeleteView , django.views.generic.detail.SingleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.edit.BaseDeleteView , django.views.generic.edit.DeletionMixin , django.views.generic.detail.BaseDetailView , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.base.View , builtins.object]
			P: content_type None
			P: context_object_name None
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: pk_url_kwarg pk
			P: query_pk_and_slug False
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: slug_field slug
			P: slug_url_kwarg slug
			P: success_url None
			P: template_engine None
			P: template_name None
			P: template_name_field None
			P: template_name_suffix _confirm_delete
			M: as_view(initkwargs)
			F: delete(self,request,args,kwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_object(self,queryset)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_success_url(self)
			F: get_template_names(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
			F: render_to_response(self,context,response_kwargs)
		
		C: django.views.generic.edit.FormView [ django.views.generic.edit.FormView , django.views.generic.base.TemplateResponseMixin , django.views.generic.edit.BaseFormView , django.views.generic.edit.FormMixin , django.views.generic.base.ContextMixin , django.views.generic.edit.ProcessFormView , django.views.generic.base.View , builtins.object]
			P: content_type None
			P: extra_context None
			P: form_class None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: initial {}
			P: prefix None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: success_url None
			P: template_engine None
			P: template_name None
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: form_invalid(self,form)
			F: form_valid(self,form)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_form(self,form_class)
			F: get_form_class(self)
			F: get_form_kwargs(self)
			F: get_initial(self)
			F: get_prefix(self)
			F: get_success_url(self)
			F: get_template_names(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
			F: put(self,args,kwargs)
			F: render_to_response(self,context,response_kwargs)
		
		C: django.views.generic.edit.ProcessFormView [ django.views.generic.edit.ProcessFormView , django.views.generic.base.View , builtins.object]
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
			F: put(self,args,kwargs)
		C: django.views.generic.edit.UpdateView [ django.views.generic.edit.UpdateView , django.views.generic.detail.SingleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.edit.BaseUpdateView , django.views.generic.edit.ModelFormMixin , django.views.generic.edit.FormMixin , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.edit.ProcessFormView , django.views.generic.base.View , builtins.object]
			P: content_type None
			P: context_object_name None
			P: extra_context None
			P: fields None
			P: form_class None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: initial {}
			P: model None
			P: pk_url_kwarg pk
			P: prefix None
			P: query_pk_and_slug False
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: slug_field slug
			P: slug_url_kwarg slug
			P: success_url None
			P: template_engine None
			P: template_name None
			P: template_name_field None
			P: template_name_suffix _form
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: form_invalid(self,form)
			F: form_valid(self,form)
			F: get(self,request,args,kwargs)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_form(self,form_class)
			F: get_form_class(self)
			F: get_form_kwargs(self)
			F: get_initial(self)
			F: get_object(self,queryset)
			F: get_prefix(self)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_success_url(self)
			F: get_template_names(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: post(self,request,args,kwargs)
			F: put(self,args,kwargs)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.list.BaseListView [ django.views.generic.list.BaseListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty True
			P: context_object_name None
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_queryset(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
		C: django.views.generic.list.ListView [ django.views.generic.list.ListView , django.views.generic.list.MultipleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.list.BaseListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty True
			P: content_type None
			P: context_object_name None
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			P: template_name_suffix _list
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_queryset(self)
			F: get_template_names(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
			F: render_to_response(self,context,response_kwargs)
			
			C: django.views.generic.dates.ArchiveIndexView [ django.views.generic.dates.ArchiveIndexView , django.views.generic.list.MultipleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.dates.BaseArchiveIndexView , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: content_type None
			P: context_object_name latest
			P: date_field None
			P: date_list_period year
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			P: template_name_suffix _archive
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_queryset(self)
			F: get_template_names(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.dates.BaseArchiveIndexView [ django.views.generic.dates.BaseArchiveIndexView , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: context_object_name latest
			P: date_field None
			P: date_list_period year
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_queryset(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
		C: django.views.generic.dates.BaseDateDetailView [ django.views.generic.dates.BaseDateDetailView , django.views.generic.dates.YearMixin , django.views.generic.dates.MonthMixin , django.views.generic.dates.DayMixin , django.views.generic.dates.DateMixin , django.views.generic.detail.BaseDetailView , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.base.View , builtins.object]
			P: allow_future False
			P: context_object_name None
			P: date_field None
			P: day None
			P: day_format %d
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: month None
			P: month_format %b
			P: pk_url_kwarg pk
			P: query_pk_and_slug False
			P: queryset None
			P: slug_field slug
			P: slug_url_kwarg slug
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_future(self)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_date_field(self)
			F: get_day(self)
			F: get_day_format(self)
			F: get_month(self)
			F: get_month_format(self)
			F: get_next_day(self,date)
			F: get_next_month(self,date)
			F: get_next_year(self,date)
			F: get_object(self,queryset)
			F: get_previous_day(self,date)
			F: get_previous_month(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
		C: django.views.generic.dates.BaseDateListView [ django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: context_object_name None
			P: date_field None
			P: date_list_period year
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_queryset(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
		C: django.views.generic.dates.BaseDayArchiveView [ django.views.generic.dates.BaseDayArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.MonthMixin , django.views.generic.dates.DayMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: context_object_name None
			P: date_field None
			P: date_list_period year
			P: day None
			P: day_format %d
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: month None
			P: month_format %b
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_day(self)
			F: get_day_format(self)
			F: get_month(self)
			F: get_month_format(self)
			F: get_next_day(self,date)
			F: get_next_month(self,date)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_day(self,date)
			F: get_previous_month(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
		C: django.views.generic.dates.BaseMonthArchiveView [ django.views.generic.dates.BaseMonthArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.MonthMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: context_object_name None
			P: date_field None
			P: date_list_period day
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: month None
			P: month_format %b
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_month(self)
			F: get_month_format(self)
			F: get_next_month(self,date)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_month(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
		C: django.views.generic.dates.BaseTodayArchiveView [ django.views.generic.dates.BaseTodayArchiveView , django.views.generic.dates.BaseDayArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.MonthMixin , django.views.generic.dates.DayMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: context_object_name None
			P: date_field None
			P: date_list_period year
			P: day None
			P: day_format %d
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: month None
			P: month_format %b
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_day(self)
			F: get_day_format(self)
			F: get_month(self)
			F: get_month_format(self)
			F: get_next_day(self,date)
			F: get_next_month(self,date)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_day(self,date)
			F: get_previous_month(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
		C: django.views.generic.dates.BaseWeekArchiveView [ django.views.generic.dates.BaseWeekArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.WeekMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: context_object_name None
			P: date_field None
			P: date_list_period year
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: week None
			P: week_format %U
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_next_week(self,date)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_week(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_week(self)
			F: get_week_format(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
		C: django.views.generic.dates.BaseYearArchiveView [ django.views.generic.dates.BaseYearArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: context_object_name None
			P: date_field None
			P: date_list_period month
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: make_object_list False
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_make_object_list(self)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
		C: django.views.generic.dates.DateDetailView [ django.views.generic.dates.DateDetailView , django.views.generic.detail.SingleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.dates.BaseDateDetailView , django.views.generic.dates.YearMixin , django.views.generic.dates.MonthMixin , django.views.generic.dates.DayMixin , django.views.generic.dates.DateMixin , django.views.generic.detail.BaseDetailView , django.views.generic.detail.SingleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.base.View , builtins.object]
			P: allow_future False
			P: content_type None
			P: context_object_name None
			P: date_field None
			P: day None
			P: day_format %d
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: month None
			P: month_format %b
			P: pk_url_kwarg pk
			P: query_pk_and_slug False
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: slug_field slug
			P: slug_url_kwarg slug
			P: template_engine None
			P: template_name None
			P: template_name_field None
			P: template_name_suffix _detail
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_future(self)
			F: get_context_data(self,kwargs)
			F: get_context_object_name(self,obj)
			F: get_date_field(self)
			F: get_day(self)
			F: get_day_format(self)
			F: get_month(self)
			F: get_month_format(self)
			F: get_next_day(self,date)
			F: get_next_month(self,date)
			F: get_next_year(self,date)
			F: get_object(self,queryset)
			F: get_previous_day(self,date)
			F: get_previous_month(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_slug_field(self)
			F: get_template_names(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.dates.DayArchiveView [ django.views.generic.dates.DayArchiveView , django.views.generic.list.MultipleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.dates.BaseDayArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.MonthMixin , django.views.generic.dates.DayMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: content_type None
			P: context_object_name None
			P: date_field None
			P: date_list_period year
			P: day None
			P: day_format %d
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: month None
			P: month_format %b
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			P: template_name_suffix _archive_day
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_day(self)
			F: get_day_format(self)
			F: get_month(self)
			F: get_month_format(self)
			F: get_next_day(self,date)
			F: get_next_month(self,date)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_day(self,date)
			F: get_previous_month(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_template_names(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.dates.MonthArchiveView [ django.views.generic.dates.MonthArchiveView , django.views.generic.list.MultipleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.dates.BaseMonthArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.MonthMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: content_type None
			P: context_object_name None
			P: date_field None
			P: date_list_period day
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: month None
			P: month_format %b
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			P: template_name_suffix _archive_month
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_month(self)
			F: get_month_format(self)
			F: get_next_month(self,date)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_month(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_template_names(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.dates.TodayArchiveView [ django.views.generic.dates.TodayArchiveView , django.views.generic.list.MultipleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.dates.BaseTodayArchiveView , django.views.generic.dates.BaseDayArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.MonthMixin , django.views.generic.dates.DayMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: content_type None
			P: context_object_name None
			P: date_field None
			P: date_list_period year
			P: day None
			P: day_format %d
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: month None
			P: month_format %b
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			P: template_name_suffix _archive_day
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_day(self)
			F: get_day_format(self)
			F: get_month(self)
			F: get_month_format(self)
			F: get_next_day(self,date)
			F: get_next_month(self,date)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_day(self,date)
			F: get_previous_month(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_template_names(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.dates.WeekArchiveView [ django.views.generic.dates.WeekArchiveView , django.views.generic.list.MultipleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.dates.BaseWeekArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.WeekMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: content_type None
			P: context_object_name None
			P: date_field None
			P: date_list_period year
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			P: template_name_suffix _archive_week
			P: week None
			P: week_format %U
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_next_week(self,date)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_week(self,date)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_template_names(self)
			F: get_week(self)
			F: get_week_format(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
			F: render_to_response(self,context,response_kwargs)
		C: django.views.generic.dates.WeekMixin [ django.views.generic.dates.WeekMixin , builtins.object]
			P: week None
			P: week_format %U
			F: get_next_week(self,date)
			F: get_previous_week(self,date)
			F: get_week(self)
			F: get_week_format(self)
		C: django.views.generic.dates.YearArchiveView [ django.views.generic.dates.YearArchiveView , django.views.generic.list.MultipleObjectTemplateResponseMixin , django.views.generic.base.TemplateResponseMixin , django.views.generic.dates.BaseYearArchiveView , django.views.generic.dates.YearMixin , django.views.generic.dates.BaseDateListView , django.views.generic.list.MultipleObjectMixin , django.views.generic.base.ContextMixin , django.views.generic.dates.DateMixin , django.views.generic.base.View , builtins.object]
			P: allow_empty False
			P: allow_future False
			P: content_type None
			P: context_object_name None
			P: date_field None
			P: date_list_period month
			P: extra_context None
			P: http_method_names ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			P: make_object_list False
			P: model None
			P: ordering None
			P: page_kwarg page
			P: paginate_by None
			P: paginate_orphans 0
			P: paginator_class <class 'django.core.paginator.Paginator'>
			P: queryset None
			P: response_class <class 'django.template.response.TemplateResponse'>
			P: template_engine None
			P: template_name None
			P: template_name_suffix _archive_year
			P: year None
			P: year_format %Y
			M: as_view(initkwargs)
			F: dispatch(self,request,args,kwargs)
			F: get(self,request,args,kwargs)
			F: get_allow_empty(self)
			F: get_allow_future(self)
			F: get_context_data(self,object_list,kwargs)
			F: get_context_object_name(self,object_list)
			F: get_date_field(self)
			F: get_date_list(self,queryset,date_type,ordering)
			F: get_date_list_period(self)
			F: get_dated_items(self)
			F: get_dated_queryset(self,lookup)
			F: get_make_object_list(self)
			F: get_next_year(self,date)
			F: get_ordering(self)
			F: get_paginate_by(self,queryset)
			F: get_paginate_orphans(self)
			F: get_paginator(self,queryset,per_page,orphans,allow_empty_first_page,kwargs)
			F: get_previous_year(self,date)
			F: get_queryset(self)
			F: get_template_names(self)
			F: get_year(self)
			F: get_year_format(self)
			F: http_method_not_allowed(self,request,args,kwargs)
			F: options(self,request,args,kwargs)
			F: paginate_queryset(self,queryset,page_size)
			F: render_to_response(self,context,response_kwargs)
		
```