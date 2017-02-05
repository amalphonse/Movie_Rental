class Movie:
    def __init__(self, name, genre,hasWatched):
        self.name = name
        self.genre = genre
        self.hasWatched = hasWatched

    def __repr__(self):
        return "<Movie: {}>".format(self.name)

    def json(self):
        return{
            'name': self.name,
            'genre':self.genre,
            'hasWatched': self.hasWatched
        }

    @classmethod
    def from_json(cls,json_data):
        return Movie(json_data['name'],json_data['genre'],json_data['hasWatched'])


