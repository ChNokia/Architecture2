{% extends 'news_template.tpl' %}
{% block content %}
    <h3> This is the start of my child template</h3>
    <br>
    <h3>Football article NEWS: {{tittle_article}}</h3>
    <p>{{text_article}}</p>
    <h3> This is the end of my child template</h3>
{% endblock %}