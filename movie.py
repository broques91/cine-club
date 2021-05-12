# coding: utf-8
import logging
import json
import os

LOGGER = logging.getLogger()
CUR_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CUR_DIR, "data")
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
    with open(DATA_FILE, "r") as f:
        movies = json.load(f)
        
    movies = [Movie(movie) for movie in movies]
    return movies


class Movie():
    
    def __init__(self, title):
        self.title = title.title()
    
    def __str__(self):
        return self.title
    
    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
        
    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)
            
    def add_to_movies(self):
        movies = self._get_movies()
        
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            LOGGER.warning(f"Le film {self.title} est déjà enregistré")
            return False
        
    def remove_from_movies(self):
        movies = self._get_movies()
        
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            LOGGER.warning(f"Le film {self.title} n'est pas enregistré")
            return False
        
    
if __name__ == "__main__":
    movies = get_movies()
    print(movies)