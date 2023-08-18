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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Series(MotionPicture):
    def __init__(self, season_nr, episode_nr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_nr = season_nr
        self.episode_nr = episode_nr


def main():
    films = {}
    films.update({"title": "The Shawshank Redemption", "year": 1994, "genre": "drama"})

    print(films['title'])
    print(type(films))

    film_1 = MotionPicture('The Shawshank Redemption', 1994, 'Drama')

    print(film_1.views_number)
    film_1.play()
    film_1.play()
    film_1.play()
    film_1.play()
    film_1.play()
    print(film_1.views_number)