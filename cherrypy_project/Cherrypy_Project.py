import cherrypy


class root(object):
    @cherrypy.expose
    def index(self):
        return '''<!DOCTYPE html>
<html lang="en">

<head>
    <title>Cherrypy Project</title>
</head>

<body>
    <form method="get" action="add">
        <input type="tex" name="x" />
        <input type="tex" name="y" />
        <button type="submit">Addition</button>
    </form>
    <form method="get" action="sub">
        <input type="tex" name="x" />
        <input type="tex" name="y" />
        <button type="submit">Subtraction</button>
    </form>
</body>

</html>'''

    @cherrypy.expose
    def add(self, x, y):
        return f'The SUM value is {int(x)+int(y)}'

    @cherrypy.expose
    def sub(self, x, y):
        return f'The SUB value is {int(x)-int(y)}'


# if __name__ == 'main__':
cherrypy.quickstart(root(), '')
