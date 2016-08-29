#!/usr/bin/python
__doc__ = """{f}

Usage:
    {f} [-f  <FONT> | --font <FONT>] [<TEXT>]
    {f} [<TEXT>]
    {f} -h | --help

Options:
    -f, --font <FONT>   font number
    <TEXT>   text to be image
    -h --help           Show this screen and exit.
""".format(f=__file__)

from docopt import docopt

import cv2
import numpy as np
from PIL import Image
width = 1800
height = 500

def RGB2BGR(rgbcolor=(0, 0, 0)):
  return tuple(reversed(rgbcolor))

def main(text, fontnum=0):
  img = np.zeros((height, width, 3), np.uint8)
#  trans = np.asarray(Image.new('RGBA', (width, height), (0, 0, 0, 0)))
#  img2 = trans.copy()
  dot = cv2.imread('./img/block.png', 1)

  color = RGB2BGR((255, 255, 255))
  img[:] = color
  img2 = img.copy()


  fonts = [cv2.FONT_HERSHEY_COMPLEX,  # best
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           cv2.FONT_HERSHEY_DUPLEX,
           cv2.FONT_HERSHEY_PLAIN,
           cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
           cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
           cv2.FONT_HERSHEY_SIMPLEX,
           cv2.FONT_HERSHEY_TRIPLEX,
           cv2.FONT_ITALIC
           ]
  font = fonts[fontnum]
#  line = cv2.CV_AA
  line = 8
  thickness = 12
  size = 15
  cv2.putText(img, text, (0, 400), font, size, (0,0,0), thickness, line)

  for y in range(0, height, dot.shape[0]):
    for x in range(0, width, dot.shape[1]):
      avg = np.average(img[y:y+dot.shape[0], x:x+dot.shape[1]])
      if avg < 230:
        # insert image
        y2 = y+dot.shape[0]
        x2 = x+dot.shape[1]
        if y2 < img.shape[0] and x2 < img.shape[1]:
          img2[y:y2, x:x2] = dot

        
      
  img3 = cv2.resize(img2, (int(img.shape[1]*0.75), int(img.shape[0]*0.75)))
  cv2.imshow('img', img3)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__":
  args = docopt(__doc__)
  text = args.get('<TEXT>') or 'RUNCO'
  font = args.get('--font') or 0

  main(text, int(font)) 
  
