from project.app import db

# create the database and the db table
# HELLO!s
db.create_all()
# commit the changes
db.session.commit()
