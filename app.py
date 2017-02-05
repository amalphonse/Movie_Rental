import os

#from movie import Movie
#from users import Users

from users_json import Users
import json

#user = Users("Anju")

#my_movie = Movie("The Notebook", "Romantic",True)

#user.movies.append(my_movie)

#print(user.movies_watched())

#user.add_movie("The Notebook", "Romantic")
#user.add_movie("The Matrix","Sci-fi")
#user.save_to_file()
#print(user.json())
#user = Users.load_from_file("Users_Movies.txt")
#print (user.movies)
#print(user.name)
#with open('json_users.txt','w') as f:
 #   json.dump(user.json(),f)
#with open('json_users.txt','r') as f:
 #   json_data = json.load(f)
#    user = Users.from_json(json_data)
 #   print(user.json())
def menu():
    user_name = input("Enter your name: ")
    #check if file exits for the user
    file_name = "{}.txt".format(user_name)
    if file_exists(file_name):
        with open(file_name,'r') as f:
            json_data = json.load(f)
        user = Users.from_json(json_data)
    else:
        user = Users(user_name)
    user_input = input("Enter 'a' to add a movie, 'w' to set the movie to watched"
          ", 's' to see the list fof movies, 'd' to delete a movie,"
          "'l' to see list of watched movies,'f' to save  or 'q' to quit:  " )

    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("enter the movie genre: ")
            user.add_movie(movie_name,movie_genre)
        elif user_input == 'w':
            name_movie = input("Enter the ame of the movie to set to watched: ")
            user.set_watched(name_movie)
        elif user_input == 's':
            for movie in user.movies:
                print("Movie Name: {} Genre: {} Watched: {}".format(movie.name,movie.genre,movie.hasWatched))
        elif user_input == 'd':
            movie_del_name = input("Enter the name of movie you want deleted: ")
            user.delete_movie(movie_del_name)
        elif user_input == 'l':
            for movie in user.movies_watched:
                print("Movie Name: {} Genre: {} Watched: {}".format(movie.name,movie.genre,movie.hasWatched))
        elif user_input == 'f':
            with open(file_name,'w') as f:
                json.dump(user.json(), f)

        user_input = input("Enter 'a' to add a movie, 'w' to set the movie to watched"
                           ", 's' to see the list fof movies, 'd' to delete a movie,"
                           "'l' to see list of watched movies or 'q' to save and quit:  ")


def file_exists(file_name):
    return os.path.isfile(file_name)

menu()