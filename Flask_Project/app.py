from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def sayhello():
    content = '''<html><head><title>First Page</title></head>
    <body><marquee>Welcome to New Flask Page(Scrolls from left to right)</marquee></body></html>'''
    return content

@app.route('/coures')
def corse():
    return render_template('coures.html')

@app.route('/details')
def details():
    return render_template('details.html')

if __name__=='__main__':
    app.debug=True
    app.run()
