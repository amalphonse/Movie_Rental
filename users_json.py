from movie_json import Movie

class Users:
    def __init__(self,name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User: {}>".format(self.name)


    def add_movie(self,name,genre):
        movie =  Movie(name,genre,False)
        self.movies.append(movie)


    def delete_movie(self,name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))


    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.hasWatched = True

    def movies_watched(self):
        #watched_movies = []
        #for movie in self.movies:
         #   if movie.hasWatched:
        #        watched_movies.append(movie)
        #return watched_movies
        # instead of this function we can use filter() method
        watched_movies = list(filter(lambda movie: movie.hasWatched,self.movies)) # filter method returns a filter object so we need to convert to list.
        return watched_movies


    def json(self):
        return{
            'name': self.name,
            'movies': [movie.json() for movie in self.movies]
        }

    @classmethod
    def from_json(cls,json_data):
        user = Users(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
           # movies.append(Movie(movie['name'],movie['genre'],movie['hasWatched']))
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user