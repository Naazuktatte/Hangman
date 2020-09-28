from hangman import hangmanDb 
from sqlalchemy.dialects.postgresql import JSON

#Creating table name for users
class hangmanUser(hangmanDb.model):
    __tablename__ = 'hm_user'
    id = Column(Integer, Sequence('hm_user_id_seq'), primary_key=True)
    name = Column(String(10))
    def __repr__(self):
        return('User details: id:{}, user name:{}, name: {} '.format(self.id, self.user_name, self.name))

class hangmanMovieList(hangmanDb.model):
    __tablename__ = 'hm_movie'
    id = hangmanDb.Column(Integer, Sequence('hm_movies_list_id_seq'),primary_key=True)
    name = hangmanDb.Column(String(30))
    description = hangmanDb.Column(String(500))
    actors = hangmanDb.Column(JSON)
    # image = hangmanDb.Column() # will check this out bytea column in postgres for storing image binary data
    def __repr__(self):
        return('Movie details: id:{}, movie name:{}, movie desc: {}, actor: {}'.format(self.id, self.name, self.description, self.actors))

class hangmanGame(hangmanDb.model):
    __tablename__ = 'hm_game'
    id = hangmanDb.Column(Integer, Sequence('hm_game_id_seq'), primary_key=True)
    player = hangmanDb.Column(None, ForeignKey('hm_user.id'), nullable=False)
    movie = hangmanDb.Column(None, ForeignKey('hm_movie.id'), nullable=False)
    result = hangmanDb.Column(String)
    game_date = hangmanDb.Column(Date)
    game_chances = hangmanDb.Column(Integer)
    def __repr__(self):
        return('Game {0} was {1} by player_id: {2} on {3} with {4} chances taken'.format(self.id, self.result, self.player, self.game_date, self.game_chances))

class hangmanChances(hangmanDb.model):
    __tablename__ = 'hm_chances'
    id = hangmanDb.Column(Integer, Sequence('hm_chances_id_seq'), primary_key=True)
    game_id = hangmanDb.Column(None, ForeignKey('hm_game.id'))
    letter_guessed = hangmanDb.Column(String(1))
    full_guessed = hangmanDb.Column(Boolean)
    def __repr__(self):
        return('GameID: {1},Letter guessed: {2}, Full word guessed: {3}'.format(self.id, self.game_id, self.letter_guessed, self.full_guessed))


