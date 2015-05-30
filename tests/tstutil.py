import os
import os.path
import urllib.request

import pyfreeimage.io

IMG_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')

IMG_URL = {'5.2.10.tiff': 'http://sipi.usc.edu/database/download.php?vol=misc&img=5.2.10',
           'kodim22.png': 'http://r0k.us/graphics/kodak/kodak/kodim22.png',
           'kochtreffen.jpg': 'http://upload.wikimedia.org/wikipedia/commons/thumb/3/36/13-09-01-kochtreffen-wien-RalfR-02.jpg/320px-13-09-01-kochtreffen-wien-RalfR-02.jpg'}

def load_image(name):
    os.makedirs(IMG_DIR, exist_ok=True)
    path = os.path.join(IMG_DIR, name)
    if not os.path.isfile(path):
        g = urllib.request.urlopen(IMG_URL[name])
        with open(path, 'w+b') as f:
            f.write(g.read())
    return pyfreeimage.io.load(path)
