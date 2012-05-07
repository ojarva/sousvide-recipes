Sous vide recipes
=================

This is a simple recipe management tool for my sous vide cooking built 
on top of jquery-mobile and Django. As sous vide requires quite a bit 
experimenting with parameters (time and temperature), and I wanted to 
log my tries and comments, off-the-shelf software didn't quite make it. 
My installation is available [here](http://olli.jarva.fi/recipes/).

I also translated [Douglas Baldwin's excellent sous vide 
guide](http://www.douglasbaldwin.com/sous-vide.html) to Finnish, 
available at [sousvide.fi](http://www.sousvide.fi/).

Installation
------------

Install Django, configure wsgi or fastcgi (fastcgi script provided under 
*bin/* directory). Run

```
python manage.py syncdb
python manage.py collectstatic
```

to initialize database and static files. Add superuser, as that is the 
account you'll be using to log in to modify recipes.

License
-------

MIT license

Copyright (C) 2012 Olli Jarva <olli@jarva.fi>

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the 
"Software"), to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to 
the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
