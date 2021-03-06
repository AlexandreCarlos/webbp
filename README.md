#Flask Foundation
[![Build Status](https://travis-ci.org/JackStouffer/Flask-Foundation.png)](https://travis-ci.org/JackStouffer/Flask-Foundation)

Documentation is located at [https://jackstouffer.github.io/Flask-Foundation/](https://jackstouffer.github.io/Flask-Foundation/)

Flask Foundation is a solid foundation for flask applications, built with best practices, that you can easily construct your website/webapp off of. Flask Foundation is different from most Flask frameworks as it does not assume anything about your development or production environments. Flask Foundation is platform agnostic in this respect.

Built off of the [bootstrapy project](https://github.com/kirang89/bootstrapy)

Best practices were learned from:
* [Creating Websites With Flask](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/)
* [Getting Bigger With Flask](http://maximebf.com/blog/2012/11/getting-bigger-with-flask/)
* [Larger Applications With Flask](http://flask.pocoo.org/docs/patterns/packages/).


## DB init and migration

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    python manage.py server


## License

Flask-Foundation is licensed under the BSD license. For more info see LICENSE.md

# Want to learn more about Flask?

I also wrote a book on Flask! You can order it [here](https://www.packtpub.com/web-development/mastering-flask).

[Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)
