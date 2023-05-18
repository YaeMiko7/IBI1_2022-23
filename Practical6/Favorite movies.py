movie = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22,
         'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7}
# Create a dictionary called Favorite movies
movie_genres = list(movie.keys())
students_number = list(movie.values())
# Print the "movie" dictionary to the console.
print(movie)
# use matplotlib to draw a plot
import matplotlib.pyplot as plt
plt.pie(students_number, labels=movie_genres, autopct='%1.1f%%')
# show the pie chart
plt.show()
# requested genres variable is here (eg. 'War')
requested_genre = 'War'
print(movie[requested_genre])
