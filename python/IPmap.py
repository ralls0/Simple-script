import geocoder
import folium

g = ""

resp = input("Vuoi inserire un ip? [y/n]")
if resp == "y":
  nip = input("Inserisci l'ip: ")
  g = geocoder.ip(nip)
else:
  g = geocoder.ip("me")


myAddress = g.latlng

my_map = folium.Map(location=myAddress,
zoom_start=12)

folium.CircleMarker(location=myAddress,
radius=55,
popup="Me").add_to(my_map)

folium.Marker(location=myAddress,
popup="Me").add_to(my_map)

my_map.save('my_map.html')
