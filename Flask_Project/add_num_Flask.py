from flask import Flask

app=Flask(__name__)

@app.route('/')
def sayhello(): 
    content = '''<html><head><title>ADD NUMBERS</title></head>
    <body><h1><center>Pass a and b (/add/ A + B) and Get sum value</center></h1></body></html>'''
    return content
   

@app.route('/add/<a>+<b>')
def add(a,b):
    return f"sum of {a}+{b}={int(a)+int(b)}"

if __name__=='__main__':
    app.debug=True
    app.run()
