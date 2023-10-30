import geopandas as gpd
import matplotlib.pyplot as plt

# Load the world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Select the countries in Europe and Africa
selected_countries = ['United States', 'Canada', 'China', 'India', 'Pakistan', 
                        'Saudi Arabia', 'United Kingdom', 'Russia', 'Denmark', 
                        'Brazil', 'Nigeria', 'Kenya', 'South Africa', 'Ghana', 
                        'Algeria', 'Egypt'
                    ]
filtered_map = world[world['name'].isin(selected_countries)]

# Plot the selected countries on the map
fig, ax = plt.subplots(figsize=(12, 8))
world.plot(ax=ax, color='lightgray')
filtered_map.plot(ax=ax, color='blue')
plt.title('Selected Countries in Europe and Africa')
plt.show()