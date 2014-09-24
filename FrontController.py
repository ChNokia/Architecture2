# -*- coding: utf-8 -*- 

import TemplateEngine
import Router
import Route

import sys
import os
import time, Cookie
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2 import Environment

news_list = ['Sport', 'Politic', 'Live', 'World', 'Economics']
sport_list = ['Football', 'Tenis', 'Hoky', 'Basketball', 'Cars']

route_strings = []

def do_GET(environ, environ_values):
	template_loader = TemplateEngine.TemplateEngine(searchpath = '/usr/share/uwsgi/www/mySite/get')
	template = None
	url = (environ_values['PATH_INFO'])#create_url((environ_values['PATH_INFO'])[1:])
	router = Router.Router(route_strings)
	route = router.route_for_uri(url)

	if route:
		template = template_loader.get_template(route.uri + route.template)
 
	response_body = template.render(my_string = 'News!', my_list = news_list)

	return response_body.encode('utf-8')

def application(environ, start_response):
	HEADER_ANSWER = '200 OK'
	environ_values = dict(environ.items())
	response_body = ''
	response_headers = []

	with open('routes.conf', 'r') as file:
		for line in file:
			route_strings.append(line[:-1])

	print('PATH_INFO = ', environ_values['PATH_INFO'])
	print('QUERY_STRING = ', environ_values['QUERY_STRING'])
	
	if environ_values['REQUEST_METHOD'] == 'GET':
		try:
			response_body = do_GET(environ, environ_values)
		except ValueError:
			response_body = 'Page not found'
			HEADER_ANSWER = '404 Not Found'
	
	response_headers.append(('Content-Type', 'text/html'))
	response_headers.append(('Content-Length', str(len(response_body))))

	start_response(HEADER_ANSWER, response_headers)

	return response_body
	