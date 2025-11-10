import sys
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from geopy.geocoders import Nominatim
import matplotlib.image as mpimg
import requests
from io import BytesIO
from adjustText import adjust_text

def create_map_with_cities(cities, logo_url):
    geolocator = Nominatim(user_agent="world_map_application")

    plt.figure(figsize=(14, 10))
    ax = plt.axes(projection=ccrs.Robinson(central_longitude=20))

    ax.set_global()

    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAKES, alpha=0.5)

    texts = []

    for city in cities:
        try:
            location = geolocator.geocode(city)
            if location:
                lon, lat = location.longitude, location.latitude

                ax.plot(lon, lat, 'ro', markersize=10, transform=ccrs.PlateCarree())

                text = ax.text(lon + 2, lat + 2, city.split(',')[0], transform=ccrs.PlateCarree(),
                               fontsize=12, fontweight='bold', bbox=dict(facecolor='white', alpha=0.7))
                texts.append(text)

                print(f"Added {city} at coordinates: {lat}, {lon}")
            else:
                print(f"Could not find coordinates for {city}")
        except Exception as e:
            print(f"Error processing {city}: {e}")

    cern_lat, cern_lon = 46.2330, 6.0556
    ax.plot(cern_lon, cern_lat, 'bo', markersize=10, transform=ccrs.PlateCarree())
    cern_text = ax.text(cern_lon + 2, cern_lat + 2, "CERN", transform=ccrs.PlateCarree(),
                        fontsize=12, fontweight='bold', bbox=dict(facecolor='white', alpha=0.7))
    texts.append(cern_text)
    print(f"Added CERN at coordinates: {cern_lat}, {cern_lon}")

    adjust_text(texts, expand_points=(1.5, 1.5))

    try:
        response = requests.get(logo_url)
        logo_img = mpimg.imread(BytesIO(response.content))

        logo_ax = plt.axes([0.75, 0.25, 0.1, 0.1], frameon=False)
        logo_ax.imshow(logo_img)
        logo_ax.axis('off')

        print("Added logo successfully")
    except Exception as e:
        print(f"Error adding logo: {e}")

    plt.savefig("LHCb_map_output.png", dpi=300, bbox_inches='tight')
    print("Map saved as LHCb_map_output.png")

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        raise ValueError("Please provide at least one city as a command-line argument.")

    cities_to_show = sys.argv[1:]
    logo_url = "https://fredi.web.cern.ch/pics/lhcb_logo.png"
    create_map_with_cities(cities_to_show, logo_url)
