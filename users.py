from movie import Movie

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

    def movies_watched(self):
        #watched_movies = []
        #for movie in self.movies:
         #   if movie.hasWatched:
        #        watched_movies.append(movie)
        #return watched_movies
        # instead of this function we can use filter() method
        watched_movies = list(filter(lambda movie: movie.hasWatched,self.movies)) # filter method returns a filter object so we need to convert to list.
        return watched_movies


    def save_to_file(self):
        with open("Users_Movies.txt",'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.name, movie.genre,str(movie.hasWatched)))

#classmethid runs on the class itself
    @classmethod
    def load_from_file(cls,filename):
        with open(filename,'r') as f:
            content =f.readlines()
            username = content[0]
            movie_name = []
            for line in content[1:]:
                movie_data = line.split(",")
                movie_name.append(Movie(movie_data[0],movie_data[1],movie_data[2] == "True"))
        user = cls(username)
        user.movies = movie_name
        return user
