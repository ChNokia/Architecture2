# -*- coding: utf-8 -*- 

class Route(object):
	def __init__(self, route_str):
		self.__uri = route_str
		self.__uri_path = self.__create_path_uri(route_str)
		self.__date_uri = {}
		self.__template = '-'.join(
									[
										folder.strip('[').strip(']')
										if folder else 'index'
										for folder in self.__uri_path
									]
									) + '.tpl'

		#if self.__uri_path[0]:
		#	self.__template = '-'.join([folder.strip('[').strip(']') for folder in self.__uri_path]) + '.tpl'

	def __create_path_uri(self, uri_str = ''):
		uri_path = uri_str.strip('/').split('/')

		return uri_path

	def matches_uri(self, uri): # return bool
		uri_path = self.__create_path_uri(uri)

		if len(uri_path) != len(self.__uri_path):
			return False

		num_part_uri = 0;

		for left, right in zip(self.__uri_path, uri_path):
			if not '[' in left:
				if left != right:
					self.__date_uri = {}

					return False

			self.__date_uri[num_part_uri] = {left.strip('[').strip(']'): right}
			num_part_uri += 1

		return True

	@property
	def uri(self):
		return self.__uri

	@property
	def template(self):
		return self.__template

	@property
	def date_uri(self):
		return self.__date_uri

class Router(object):
	def __init__(self, route_strings):
		if not route_strings:
			raise ValueError('Empty route_strings')

		self.__routes = [Route(route_string) for route_string in route_strings]

	def route_for_uri(self, uri):
		for route in self.__routes:
			if route.matches_uri(uri):
				return route

		raise ValueError('NotFoundError')

def main():
	route_strings = []

	with open('routes.conf', 'r') as file:
		for line in file:
			route_strings.append(line[:-1])

	print(route_strings)

	router = Router(route_strings)
	route = router.route_for_uri('/news/')

	if route:
		print(route.template)
		print(route.date_uri)

	route = router.route_for_uri('/news/sport/')

	if route:
		print(route.template)
		print(route.date_uri)

	route = router.route_for_uri('/news/subject/')

	if route:
		print(route.template)
		print(route.date_uri)

if __name__ == '__main__':
	main()
