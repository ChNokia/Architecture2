{% extends './././news_template.tpl' %}
{% block content %}
    <br>
    <h3>NEWS > Sport {{my_string}}</h3>
    <ul>
        {% for n in my_list %}
            <li>{{n}}</li>
        {% endfor %}
    </ul>
{% endblock %}