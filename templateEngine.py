# -*- coding: utf-8 -*- 

import router

from jinja2 import Template, FileSystemLoader, Environment

news_list = ['Sport', 'Politic', 'Live', 'World', 'Economics']
sport_list = ['Football', 'Tenis', 'Hoky', 'Basketball', 'Cars']
dict_article = {'tittle_article': 'Финал Лиги Чемпионов 2015/16 пройдет в Милане',
				'text': '''Стадион "Сан-Сиро" в Милане примет финал Лиги Чемпионов в сезоне-2015/16. Как отмечает итальянская пресса, о подобном развитии событий сообщалось и ранее, а сегодня на пресс-конференции в штаб-квартире УЕФА в Ньоне место проведения финала в 2016 году было подтверждено официально.

Отметим, что "Сан-Сиро", на котором домашние матчи проводят "Милан" и "Интер", в четвёртый раз будет проводить финал Лиги Чемпионов. Стадион принимал финальные матчи турнира в 1965-м, 1970-м и 2001 годах. Отметим, что решающий матч главного еврокубкового турнира в девятый раз пройдёт в Италии.
'''}



class TemplateEngine(object):
	def __init__(self, searchpath = '/'):
		template_loader = FileSystemLoader(searchpath)
		self.__template_enviroment = Environment(loader = template_loader)

	def get_template(self, template_name):
		return self.__template_enviroment.get_template(template_name)

def main():
	data_file = None
	template_loader = TemplateEngine(searchpath = '/home/ubuntu/Desktop/devclub/Architecture2')
	route_strings = []

	with open('routes.conf', 'r') as file:
		for line in file:
			route_strings.append(line[:-1])

	my_router = router.Router(route_strings)
	route = my_router.route_for_uri('/news/')
	template = None

	if route:
		template = template_loader.get_template(route.uri + route.template)

	with open('news.html', 'w') as file:
		file.write(template.render(my_string = 'News!', my_list = news_list))
	
	route = my_router.route_for_uri('/news/sport/')

	if route:
		template = template_loader.get_template(route.uri + route.template)

	with open('news-sport.html', 'w') as file:
		file.write(template.render(my_string = 'News-Sport!', my_list = sport_list))
	
	route = my_router.route_for_uri('/news/sport/football/')

	if route:
		template = template_loader.get_template(route.uri + route.template)


	with open('news-sport-football.html', 'w') as file:
		file.write(template.render(data_article = dict_article))

	#print(template.render(my_string = 'Wheeeee!', my_list = [0,1,2,3,4,5]))

if __name__ == '__main__':
	main()
