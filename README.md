Défi Info Neige
========

Info de déneigement en temps réel.


Cela utilise:

 - [jQuery](http://jquery.com/)
 - [Flask](http://flask.pocoo.org/)
 - [WebSockets](http://www.html5rocks.com/en/tutorials/websockets/basics/)
 - [RequireJS](http://requirejs.org/)
 - [Underscore.js](https://github.com/amdjs/underscore)
 - [Knockout.js](http://knockoutjs.com/)
 - [Bootstrap](http://twitter.github.io/bootstrap/)
 - [d3.js](http://d3js.org/)


La maquette des fichiers est inspiré de:
[discussion](http://flask.pocoo.org/docs/patterns/packages/).


Qu'est ce que ça fait?
------------

Lit l'information géoréférencé SOAP d'un serveur
Montre l'information sur une carte de Montréal

Pour executer
------------
virtualenv --no-site-packages --python=python2.7 env
source env/bin/activate
pip install -r requirements.txt
python runserver.py
google-chrome http://0.0.0.0:5000

Licence
-------

MIT
