import urllib
import ssl
import requests
import lxml
from bs4 import BeautifulSoup

def run():
	for i in range(21,31):
		response = requests.get('https://xkcd.com/{}'.format(i))
		soup = BeautifulSoup(response.content, 'lxml')
		image_container = soup.find(id='comic')
		image_url = image_container.find('img')['src']
		image_name = image_url.split('/')[-1]
		print('Dowload image {}'.format(image_name))
		urllib.request.urlretrieve('https:{}'.format(image_url), image_name)


if __name__ == "__main__":
	run()
