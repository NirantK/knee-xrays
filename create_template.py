import numpy as np
import argparse
from pathlib import Path
# import imutils
import glob
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template_input", required=False, help="Path to template image directory", default='./data/smith_profix_1/output/')
ap.add_argument("-v", "--visualize",
	help="Flag indicating whether or not to visualize each iteration")
args = vars(ap.parse_args())
 
# load the image image, convert it to grayscale, and detect edges
data_path = Path(args['template_input'])
assert data_path.exists()

template_path = data_path.parents[0]/'template/'
template_path.mkdir(parents=True, exist_ok=True)
print(template_path)
assert template_path.exists()
idx = 0
for image in list(data_path.iterdir()):
	# print(image.absolute())
	image_path = str(image.absolute())
	template = cv2.imread(image_path)
	template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
	template = cv2.Canny(template, 50, 200)
	idx += 1
	filename = str(template_path.absolute()/(str(idx)+'.jpg'))
	# with template_path.open(mode='w', buffering=-1, encoding=None, errors=None, newline=None) as f:
	cv2.imwrite(filename, template)

	# cv2.imshow("Template", template)
	# cv2.waitKey(2000)
# (tH, tW) = template.shape[:2]
	