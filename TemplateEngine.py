from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2 import Environment

def main():
	data_file = None
	templateLoader = FileSystemLoader(searchpath = '/home/ubuntu/Desktop/devclub/Architecture2')
	templateEnv = Environment(loader = templateLoader)
	template = templateEnv.get_template('news.tpl')

	#ith open('news.tpl', 'r') as file:
	#	data_file = file.read()
	#	t = Template(data_file)

	#print(data_file)
	with open('news.html', 'w') as file:
		file.write(template.render(my_string = 'News!', my_list = [0,1,2,3,4,5]))
	
	template = templateEnv.get_template('news-sport.tpl')

	with open('news-sport.html', 'w') as file:
		file.write(template.render(my_string = 'News-Sport!', my_list = [0,1,2,3,4,5]))
	
	template = templateEnv.get_template('news-sport-football.tpl')

	with open('news-sport-football.html', 'w') as file:
		file.write(template.render(tittle_article = 'Liga Chempions!', text_article = '[0,1,2,3,4,5]'))
	


	#print(template.render(my_string = 'Wheeeee!', my_list = [0,1,2,3,4,5]))

if __name__ == '__main__':
	main()
