# db_create.py


from datetime import date

from project import db
from project.models import Task, User


# create the database and the db table
db.create_all()

# instert data
# db.session.add(
#     User("admin", "ad@min", "admin", "admin")
# )
# db.session.add(
#     Task("Finish this tutorial", date(2015, 3, 13), 10, date(2015, 2, 13), 1, 1)
# )

# commit the changes
db.session.commit()