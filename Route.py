from urllib.parse import urlparse

class Route(object):
	def __init__(self, route_str):
		if not route_str:
			raise ValueError('Empty route_str')

		self.__uri = route_str
		folder_list = self.__uri.split('/')
		self.__template = '-'.join([folder for folder in folder_list if folder]) + '.tpl'

	def matches_uri(self, uri): # return bool
		return self.__uri == uri

	@property
	def uri(self):
		return self.__uri

	@property
	def template(self):
		return self.__template
