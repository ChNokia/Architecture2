{% extends 'news_template.tpl' %}
{% block content %}
    <h3> This is the start of my child template</h3>
    <br>
    <h3>List Sport NEWS: {{my_string}}</h3>
    <ul>
        {% for n in my_list %}
            <li>{{n}}</li>
        {% endfor %}
    </ul>
    <h3> This is the end of my child template</h3>
{% endblock %}