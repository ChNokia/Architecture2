# -*- coding: utf-8 -*- 

import os
import sys

from jinja2 import (
	Environment,
	FileSystemLoader,
	Template
	)

import router
import templateEngine

news_list = ['Sport', 'Politic', 'Live', 'World', 'Economics']
sport_list = ['Football', 'Tenis', 'Hoky', 'Basketball', 'Cars']

route_strings = []
with open('routes.conf', 'r') as file:
		for line in file:
			route_strings.append(line[:-1])

template_loader = templateEngine.TemplateEngine(searchpath = '/usr/share/uwsgi/www/mySite/get')
my_router = router.Router(route_strings)

def do_GET(environ, environ_values):
	template = None
	url = (environ_values['PATH_INFO'])
	route = my_router.route_for_uri(url)

	if route:
		template = template_loader.get_template(route.uri + route.template)

	response_body = template.render(my_string = 'News!', my_list = news_list)

	return response_body.encode('utf-8')

def application(environ, start_response):
	status_code = '200 OK'
	environ_values = dict(environ.items())
	response_body = ''
	response_headers = []

	print('PATH_INFO = ', environ_values['PATH_INFO'])
	print('QUERY_STRING = ', environ_values['QUERY_STRING'])
	
	if environ_values['REQUEST_METHOD'] == 'GET':
		try:
			response_body = do_GET(environ, environ_values)
		except ValueError:
			response_body = 'Page not found'
			status_code = '404'
	
	response_headers.append(('Content-Type', 'text/html'))
	response_headers.append(('Content-Length', str(len(response_body))))

	start_response(status_code, response_headers)

	return response_body
	