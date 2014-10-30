from urllib.parse import urlparse

class Route(object):
	def __init__(self, route_str):
		self.__uri_path = self.__path_uri(route_str)
		self.__template = 'index.tpl'

		if len(self.__uri_path) > 0:
			self.__template = '-'.join([folder for folder in self.__uri_path]) + '.tpl'

	def __path_uri(self, uri_str):
		uri_path = []
		uri = uri_str.strip('/')

		if uri:
			uri_path = uri.split('/')

		return uri_path

	def matches_uri(self, uri): # return bool
		uri_path = self.__path_uri(uri)

		if len(uri_path) != len(self.__uri_path):
			return False

		for i in range(len(uri_path)):
			if self.__uri_path[i][0] != '[':
				if uri_path[i] != self.__uri_path[i]:
					return False

		return True

	@property
	def template(self):
		return self.__template

class Router(object):
	def __init__(self, route_strings):
		if not route_strings:
			raise ValueError('Empty route_strings')

		self.__routes = []

		for route_string in route_strings:
			self.__routes.append(Route(route_string))

	def route_for_uri(self, uri):
		for route in self.__routes:
			if route.matches_uri(uri):
				return Route(uri)

		raise ValueError('NotFoundError')

def main():
	route_strings = []

	with open('routes.conf', 'r') as file:
		for line in file:
			route_strings.append(line[:-1])

	print(route_strings)

	router = Router(route_strings)
	route = router.route_for_uri('/news/sport/football/')

	if route:
		print(route.template)

if __name__ == '__main__':
	main()
