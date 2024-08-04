import requests
import urllib.parse

class Solution:

	def run(self, character):

		encoded_name = urllib.parse.quote(character)

		url= f"https://challenges.hackajob.co/swapi/api/people/?search={encoded_name}"

		response = requests.get(url)
		data = response.json()

		if 'results' in data and len(data['results']) > 0:
			character_data = data['results'][0]

			number_of_films = len(character_data['films'])
			return number_of_films
		else:
			return 0