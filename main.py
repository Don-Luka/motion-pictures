import datetime

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

    def play(self):
        self.views_number += 1

class Movie(MotionPicture):
    pass

class Series(MotionPicture):
    def __init__(self, season_nr, episode_nr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_nr = season_nr
        self.episode_nr = episode_nr
    def __repr__(self) -> str:
        return f'{self.title} S{self.season_nr:02d}E{self.episode_nr:02d}'

def get_movies():
    pass

def get_series():
    pass

def search():
    pass

def generate_views():
    pass

def top_titles(number_of, content_type):
    pass

simpsons  = Series(season_nr=1,episode_nr=1, title='The Simpsons', year = 1994, genre = 'comedy')

print(simpsons)

def main():
    # films = {}
    # films.update({"title": "The Shawshank Redemption", "year": 1994, "genre": "drama"})

    # print(films['title'])
    # print(type(films))

    film_1 = Movie('The Shawshank Redemption', 1994, 'Drama')

    print(film_1.views_number)
    film_1.play()
    film_1.play()
    film_1.play()
    film_1.play()
    film_1.play()
    print(film_1.views_number)
    
main()