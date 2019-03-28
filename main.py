from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>



<html>

    <head>

        <style>

            form {{

                background-color: #eee;

                padding: 20px;

                margin: 0 auto;

                width: 540px;

                font: 16px sans-serif;

                border-radius: 10px;

            }}

            textarea {{

                margin: 10px 0;

                width: 540px;

                height: 120px;

            }}

        </style>

    </head>

    <body>

      <!-- create your form here -->
        <form action="/" method="post">
          <label for="rotate">Rotate by: </label>
          <input id="rotate" type="text" name="rot" />
      <br><br>
          <input type="text" name="text" />
      <br>
          <input type="Submit" />
        </form>
    </body>

</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rots = int(request.form['rot'])
    texts = request.form['text']
    
    return form.format(rotate_string(texts,rots))

app.run()