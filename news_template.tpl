<!DOCTYPE html>
<html>
    <head>
            <meta charset="utf-8">
    		<title>NEWS</title>
        <style>
            body {
                width: 35em;
                margin: 1.5em;
                font-family: Tahoma, Verdana, Arial, sans-serif;
            }
            table {
            	border-collapse:collapse;
            }
            table, td, th {
            	border: 2px solid #CECECE;
            }
            td, th {
            	text-align:left;
            	padding:0.5em 0.5em;
            }
            th
            {
                background: #F0F0FF;
            }
        </style>
    </head>
    <body>
        <div class="container">
          {% block content %}{% endblock %}

          <div class="footer">
            {% block footer %}
              FOOTER
              <br>
              <br>
              <br>
            {% endblock %}
          </div>
        </div>
    </body>
</html>
