import datetime
import sys
import random
import csv

today = datetime.date.today().strftime('%d.%m.%Y')

def delta_time(f):
    def wrapper(*args, **kwargs):
        t_0 = datetime.datetime.now()
        result = f(*args, **kwargs)
        t_1 = datetime.datetime.now()
        dt = t_1-t_0
        print(f'The operation took {dt.total_seconds()} seconds')
        
        return result
    return wrapper

class MotionPicture():
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        self.views_number = 0

    def __repr__(self) -> str:
        return f'{self.title} ({self.year})'

    def play(self, views = 1):
        self.views_number += views

class Movie(MotionPicture):
    pass

class Series(MotionPicture):
    def __init__(self, season_nr, episode_nr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_nr = season_nr
        self.episode_nr = episode_nr
    def __repr__(self) -> str:
        return f'{self.title} ({self.year}) S{self.season_nr:02d}E{self.episode_nr:02d}'

def get_movies(given_list):
    return sorted([watch for watch in given_list if isinstance(watch, Movie)], key = lambda item: item.title)

def get_series(given_list):
    return sorted([watch for watch in given_list if isinstance(watch, Series)], key = lambda item: item.title)

def search(title, database):
    for item in database:
        if item.title == title:
            found = True
            found_item = item
            break
        else:
            found = False
    if found:
        print(f"Found: {found_item}.")
    else:
        print(f"The title '{title}' was not found in the database.")

def repeat_n_times(repeats = 10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for repeat in range(repeats):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_n_times(repeats=50)
def generate_views(watch_list_):
    watch_list_[random.randint(0,len(watch_list_)-1)].play(random.randint(0,100))

def top_titles(watch_list, number_of_items, content_type):
    if content_type == 'movies':
        watch_list = get_movies(watch_list)
    elif content_type == 'series':
        watch_list = get_series(watch_list)
    tops_list = sorted(watch_list, key = lambda item: item.views_number)[::-1]
    return tops_list[:min(number_of_items, len(tops_list))]

def download_movies_list(filename: str, number_of_movies: int):
    movies_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:
            i += 1
            data = row['title'], int(row['year'][1:5]), (row['genre'].strip('[]').replace("u'","").replace("'","")).split(", ")
            movies_list.append(data)
            if i >= number_of_movies:
                break
    return movies_list

def download_series_list(filename: str, number_of_series: int):
    series_list = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:
            i += 1
            data = row['title'], int(row['year'][1:6]), (row['genre'].strip('[]').replace("u'","").replace("'","")).split(", "), random.randint(1,5), random.randint(5,15)
            series_list.append(data)
            if i >= number_of_series:
                break
    return series_list

def main(content_type, tops = 10):
    global watch_list
    print('''
          Biblioteka filmów i seriali
          ''')

    movies_list = download_movies_list("movies.csv", 20)
    series_list = download_series_list("tv_shows.csv", 20)

    overall_list = movies_list + series_list

    movies = [Movie(title=movie[0], year = movie[1], genre = movie[2]) for movie in movies_list]
    series = [Series(season_nr = random.randint(1,serie[3]), episode_nr = random.randint(1,serie[4]), 
            title=serie[0], year = serie[1], 
            genre = serie[2]) for serie in series_list]
    
    watch_list = movies + series
    
    generate_views(watch_list)

    if content_type == 'movies':
        top_movies = top_titles(watch_list, tops, 'movies')
        print(f"\nTop {tops} fimów dnia {today}:")
        for j in range(tops):
            print(f"{j+1}. {top_movies[j]}: {top_movies[j].views_number}")
    elif content_type == 'series':
        top_series = top_titles(watch_list, tops, 'series')
        print(f"\nTop {tops} seriali dnia {today}:")
        for j in range(tops):
            print(f"{j+1}. {top_series[j]}: {top_series[j].views_number}")
    else:
        pass


main(content_type='series', tops=10)
main(content_type='movies', tops=10)

print(f"\nMovies alphabetically: \n{get_movies(watch_list)}")
print(f"\nSeries alphabetically: \n{get_series(watch_list)}")
search('Emily', watch_list)



def create_list_manually():
    movies_list, series_list = [], []
    movies_list.append(('The Shawshank Redemption', 1994, 'drama'))
    movies_list.append(('The Godfather', 1972, 'crime,drama'))
    movies_list.append(('Toy Story', 1995, 'animation'))
    movies_list.append(('The Blair Witch Project', 1999, 'horror'))

    series_list.append(('The Simpsons', 1989, 'animation,comedy', 20, 12))
    series_list.append(('Twin Peaks', 1990, 'crime, drama', 3, 10))
    series_list.append(('Friends', 1994, 'comedy, romance', 10, 15))
    series_list.append(('Breaking Bad', 2008, 'crime,drama', 5, 16))
    return movies_list, series_list
