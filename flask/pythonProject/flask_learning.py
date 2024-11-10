from flask import Flask
app=Flask(__name__)

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def make_italic(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def make_underline(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return "Bye!"

if __name__=="__main__":
    app.run(debug=True)