import requests

#Original map webpage: https://global-internet-map-2021.telegeography.com/

url_base = "https://tiles.telegeography.com/maps/global-internet-map-2021/6/"
url_end = ".png8"

for x in range(11, 53):
    for y in range(3, 61):
        url = url_base + str(x) + "/" + str(y)
        url += url_end
        print(url)
        r = requests.get(url, allow_redirects=True)
        filename = "DL/map_" + f'{x:02d}' + "_" + f'{y:02d}' + ".png"
        open(filename, 'wb').write(r.content)

