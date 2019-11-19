# Scrapes images from Google image search for "Spaghetti"

import requests
from bs4 import BeautifulSoup as bs
import os

# my url
url = 'https://www.google.com/search?tbm=isch&source=hp&biw=1922&bih=961&ei=szP4XK75F63I_QbXs4LgDQ&q=spaghetti&oq=spaghetti&gs_l=img.3..0l10.2589.3828..4168...0.0..0.249.722.9j0j1......0....1..gws-wiz-img.....0.G1WfLJSnvAk'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# find all the images
images = soup.findAll('img')

# create image dictionary
if not os.path.exists('sketti_img'):
    os.makedirs('sketti_img')

# move to new dir
os.chdir('sketti_img')

img = 0 # name of image

# write the images
for image in images:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('sketti_img' + str(img) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                img += 1
    except:
        pass
