from project.app import db
# hmmm
# create the database and the db table
db.create_all()
# commit the changes
db.session.commit()
