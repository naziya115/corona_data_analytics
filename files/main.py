import folium

# run my code
marker_map = folium.Map(location=[42.36021388083161, -71.09404198274717], zoom_start=12, tiles='Stamen Terrain')
folium.Marker(
    location=[42.36021388083161, -71.09404198274717],
    popup='massachusetts institute of technology',
    icon=folium.Icon(icon='cloud'),
).add_to(marker_map)

marker_map.save('mit_map.html')
