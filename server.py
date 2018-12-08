"""Woo backend coding!"""

from model import User, Book, BookList, connect_to_db, db

from secrets import *

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