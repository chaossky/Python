import folium
m=folium.Map(location=[38.3897,126.9533],zoom_start=5)

folium.Marker(location=[38.3897,126.9533],popup='Delhi').add_to(m)

m.save('map_anyang.html')
m
