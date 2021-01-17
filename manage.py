import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import db, create_app


def make_shell_context():
    return dict(app=app, db=db)


app = create_app(os.getenv('FLASKY_CONFIG', 'default'))
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()
