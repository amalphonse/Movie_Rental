class Movie:
    def __init__(self, name, genre,hasWatched):
        self.name = name
        self.genre = genre
        self.hasWatched = hasWatched

    def __repr__(self):
        return "<Movie: {}>".format(self.name)


