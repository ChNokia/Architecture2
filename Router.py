from Route import Route

class Router(object):
	def __init__(self, route_strings):
		if not route_strings:
			raise ValueError('Empty route_strings')

		self.__configs = route_strings
	
	def route_for_uri(self, uri):
		if not uri:
			raise ValueError('Empty uri')

		for route in self.__configs:
			if uri == route:#####################
				route = Route(uri)

				return route

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
