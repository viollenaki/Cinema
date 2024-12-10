from flask import Flask, jsonify, request
from collections import defaultdict
app = Flask(__name__)
class Movie:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.seances= {}

    def add_seance(self, date):
        if date not in self.seances:
            self.seances[date] = []
            
    def add_booking(self,date, seats):
        self.seances[date].extend(seats)
        

class Cinema:
    def __init__(self):
        self.movies = {}  # Словарь фильмов
        self.history = []  # История бронирований

    def add_movie(self, name, price, date):
        if name not in self.movies:
            self.movies[name] = Movie(name, price)
        # Добавляем сеанс на дату, даже если фильм уже есть
        self.movies[name].add_seance(date)
        return True

    def get_movies(self):
        films = {}
        for movie in self.movies.values():
            films[movie.name] = [movie.price, movie.seances]
        return films

    def get_movie_seances(self, movie_name):
        if movie_name in self.movies:
            return self.movies[movie_name].seances
        else:
            return {}  # Если фильм не найден, возвращаем пустой словарь

    def booking(self, name, movie_name, date, seats):
        if movie_name in self.movies and date in self.movies[movie_name].seances:
            self.movies[movie_name].add_booking(date, seats)
            # Добавляем запись в историю с указанием мест
            self.history.append((name, movie_name, date, seats))
            return f"Места {seats} успешно забронированы для {movie_name} на {date}."
        return "Фильм или дата не найдены."

    def get_user_history(self, name):
        arr = []
        for n, movie_name, seance, seats in self.history:
            if n == name:
                arr.append((movie_name, seance, seats)) 
        return arr


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

users = {}


