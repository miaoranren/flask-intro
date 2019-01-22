"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """
        <!doctype html>
        <html>Hi! This is the home page.
        <a href= "/hello">hello</a></html>
        """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person">
          <input type="radio" name="compliment" value="awesome">Awesome
            <input type="radio" name="compliment" value="terrific">Terrific
            <input type="radio" name="compliment" value="fantastic">Fantastic
            <input type="radio" name="compliment" value="neato">Neato
            <input type="radio" name="compliment" value="fantabulous">Fantabulous

          <input type="submit" value="Submit">  
        </form>
        <form action ="/diss" method="GET">
            Who needs a warning?<input type="text" name="person">
            Select a diss:
            <select name="diss_list">
                <option value= "smelly">Smelly</option>
                <option value= "mean">Mean</option>
                <option value= "selfish">Selfish</option>
                <option value= "rude">Rude</option>
            </select>
            <input type="submit" value="Submit">

        </form>
       

      </body>
    </html>
    """

@app.route("/diss",methods=['GET'])
def diss_person():

    diss = request.args.get("diss_list")

    player = request.args.get("person")

    return """
     <!doctype html>
    <html>
      <head>
        <title>A Warning</title>
      </head>
      <body>
        Hi, {}! Don't be {}!
      </body>
    </html>
    """.format(player, diss)





@app.route("/greet",methods=['GET'])
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    # y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
