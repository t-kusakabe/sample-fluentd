from bottle import template, route, run, request
import urllib

@route('/')
def login():
    print("test")
    return template('text_login')

@route('/text_check', method='post')
def check():
    username = request.forms.get('username')
    email = request.forms.get('email')

    return template('test_check.html', username=username, email=email)

run(host='0.0.0.0', port=8080, debug=True)
