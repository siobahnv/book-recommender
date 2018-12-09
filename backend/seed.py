from sqlalchemy import func
from model import User, Book, BookList

from model import connect_to_db, db
from server import app

def load_data():
    """Load sample users into database."""

    print("Deleting tables")

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()
    BookList.query.delete()
    Book.query.delete()

    testuser1 = User(email='test@test.com', password='test')
    testuser2 = User(email='gmail.com', password='password')
    testuser3 = User(email='@yahoo.com', password='blank')

    db.session.add(testuser1)
    db.session.add(testuser2)
    db.session.add(testuser3)
    db.session.commit()

    booklist1 = BookList(user_id=testuser1.user_id)
    booklist2 = BookList(user_id=testuser2.user_id)
    booklist3 = BookList(user_id=testuser3.user_id)

    db.session.add(booklist1)
    db.session.add(booklist2)
    db.session.add(booklist3)
    db.session.commit()

    book1 = Book(booklist_id=booklist1.booklist_id, title="fake book 1")
    book2 = Book(booklist_id=booklist1.booklist_id, title="fake book 2")
    book3 = Book(booklist_id=booklist1.booklist_id, title="fake book 3")

    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()

def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_data()
    set_val_user_id()