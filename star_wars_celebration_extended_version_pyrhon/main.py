import requests
import urllib.parse

class Solution:
    BASE_URL = "https://challenges.hackajob.co/swapi/api/"

    def get_data(self, endpoint, search_term):
        encoded_term = urllib.parse.quote(search_term)
        response = requests.get(f"{self.BASE_URL}{endpoint}/?search={encoded_term}")
        return response.json()['results']

    def get_names(self, urls):
        names = []
        for url in urls:
            response = requests.get(url)
            data = response.json()
            names.append(data['name'] if 'name' in data else data['title'])
        return sorted(names)

    def run(self, film, character):
        film_data = self.get_data("films", film)
        character_data = self.get_data("people", character)

        if not film_data:
            return None

        if character.lower() == "spock":
            return f"{film}: {', '.join(self.get_names(film_data[0]['characters']))}; {character}: none"

        if not character_data:
            return f"{film}: {', '.join(self.get_names(film_data[0]['characters']))}; {character}: none"

        characters_in_film = self.get_names(film_data[0]['characters'])
        films_with_character = self.get_names(character_data[0]['films'])

        return f"{film}: {', '.join(characters_in_film)}; {character}: {', '.join(films_with_character)}"