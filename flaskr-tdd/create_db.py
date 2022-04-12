from project.app import db

# create the database and the db table
# create it 
db.create_all()
# commit the changes
db.session.commit()
