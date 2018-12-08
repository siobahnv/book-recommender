"""Woo backend coding!"""

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify, url_for)

from model import User, Rating, Movie, connect_to_db, db

app = Flask(__name__)

@app.route("/")
def index():
    """Show homepage"""

    return """
      <html>
        <body>
          <h1>I am the landing page</h1>
        </body>
      </html>
      """


if __name__ == "__main__":
    
    connect_to_db(app)

    app.run(port=5000, host='0.0.0.0')