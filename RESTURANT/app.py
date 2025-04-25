# 1. Basic "Hello, World!" Flask App
# A simple Flask app to display "Hello, World!" on the homepage.
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return "Hello, World! Welcome to Flask."
# if __name__ == '__main__':
#     app.run(debug=True)



# Flask App with Dynamic Routes
# This example shows how to create dynamic routes that take input from the URL.
# from flask import Flask
# app = Flask(__name__)
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f"Hello, {username}! Welcome to your profile."
# @app.route('/square/<int:number>')
# def square_number(number):
#     return f"The square of {number} is {number**2}"
# if __name__ == '__main__':
#     app.run(debug=True)

# 3. Flask App with HTML Templates (Jinja2)
# This program shows how to use Jinja2 templates to render dynamic HTML.
# Folder Structure:
# project/
# │
# ├── app.py               # Flask app file
# └── templates/
#     └── home.html        # HTML template
# HTML Template (templates/home.html):

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <title>{{ title }}</title>
# </head>
# <body>
#     <h1>Welcome to {{ title }}!</h1>
#     <p>This is a dynamic page rendered using Flask and Jinja2.</p>
# </body>
# </html>
# Python Code (app.py):
# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return render_template('home.html', title="Flask Template Example")
# if __name__ == '__main__':
#     app.run(debug=True)
#________________________________________
# #4. Flask App with Forms
# This app accepts user input through an HTML form and displays the result.
# Folder Structure:
# project/
# │
# ├── app.py               # Flask app
# └── templates/
#     └── form.html        # HTML template for the form
# HTML Form (templates/form.html):


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <title>Flask Form Example</title>
# </head>
# <body>
#     <h2>Enter your name:</h2>
#     <form action="/greet" method="post">
#         <input type="text" name="name" required>
#         <input type="submit" value="Submit">
#     </form>
# </body>
# </html>
# Python Code (app.py):
# from flask import Flask, request, render_template
# app = Flask(__name__)
# @app.route('/')
# def form():
#     return render_template('form.html')
# @app.route('/greet', methods=['POST'])
# def greet():
#     name = request.form['name']
#     return f"Hello, {name}! Welcome to Flask."
# if __name__ == '__main__':
#     app.run(debug=True)




