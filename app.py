#from movie import Movie
from users import Users

#user = Users("Anju")

#my_movie = Movie("The Notebook", "Romantic",True)

#user.movies.append(my_movie)

#print(user.movies_watched())

#user.add_movie("The Notebook", "Romantic")
#user.add_movie("The Matrix","Sci-fi")
#user.save_to_file()

user = Users.load_from_file("Users_Movies.txt")
print (user.movies)
print(user.name)