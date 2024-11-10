from flask import Flask
app=Flask(__name__)
import random
@app.route('/')
def number_guess():
    out= f'<h1>Guess the number between 0 to 9</h1>\n<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'
    return out
rand= random.randint(0,9)
@app.route('/<num>')
def result(num):

    if int(num)<rand:
        out = f'<h1 style="color:red;">Too Low</h1>\n<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
    elif int(num)>rand:
        out = f'<h1 style="color:blue;">Too High</h1>\n<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    else:
        out = f'<h1 style="color:green;">You Found Me</h1>\n<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    return out

if __name__=="__main__":
    app.run(debug=True)