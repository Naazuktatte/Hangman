import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from hangman import hangman, hangmanDb

hangman.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(hangman, hangmanDb)
manager = Manager(hangman)

manager.add_command('hangmanDb', MigrateCommand)

if __name__=='__main__':
    manager.run()
