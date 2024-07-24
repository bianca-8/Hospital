# imports
import requests
from selenium import webdriver
import folium
import datetime
import time

# method to return coordinates using ip address
def locationCoordinates():
	try:
		response = requests.get('https://ipinfo.io')
		data = response.json()
		loc = data['loc'].split(',')
		lat, long = float(loc[0]), float(loc[1])
		city = data.get('city', 'Unknown')
		state = data.get('region', 'Unknown')
		return lat, long, city, state # return lat, long
	except:
		print("Internet Not avialable") # error message
		exit() # close program
		return False


# method to get coordinates and make a html file of the map
def gps_locator():

	obj = folium.Map(location=[0, 0], zoom_start=2)

	try:
		lat, long, city, state = locationCoordinates()
		print("Place: {},{}".format(city, state))
		print("Latitude = {} and Longitude = {}".format(lat, long))
		folium.Marker([lat, long], popup='Current Location').add_to(obj)

		fileName = "C:/screengfg/Location" + \
			str(datetime.date.today()) + ".html"

		obj.save(fileName)

		return fileName

	except:
		return False


# main method
if __name__ == "__main__":

	print("GPS\n")

	# call function
	page = gps_locator()
	print("\nOpening File.............")
	dr = webdriver.Chrome()
	dr.get(page)
	time.sleep(4)
	dr.quit()
	print("\nBrowser Closed..............")