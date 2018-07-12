import numpy as np
import argparse
from pathlib import Path
# import imutils
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template", required=False, help="Path to template image directory", default='./data/smith_profix_1/output/')
ap.add_argument("-i", "--images", required=False,
	help="Path to images where template will be matched", default='./data/raw/output_100/')
ap.add_argument("-v", "--visualize",
	help="Flag indicating whether or not to visualize each iteration")
args = vars(ap.parse_args())
 
# load the image image, convert it to grayscale, and detect edges
data_path = Path(args['template'])
search_path = Path(args['images'])
assert data_path.exists()
assert search_path.exists()


for search in search_path.iterdir():
	found = None
	search_image = cv2.imread(str(search.absolute()), 0)
	for template in data_path.iterdir():
		template_image = cv2.imread(str(template.absolute()), 0)
		
		tH, tW = template_image.shape
		imgH, imgW = search_image.shape
		r = float(imgW) / float(imgH)
		
		if imgH < tH or imgW < tW:
			break
		
		edged = cv2.Canny(search_image, 50, 200)
		result = cv2.matchTemplate(edged, template_image, cv2.TM_CCOEFF)
		(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
		# if we have found a new maximum correlation value, then ipdate
		# the bookkeeping variable
		if found is None or maxVal > found[0]:
			found = (maxVal, maxLoc, r)

	if found is not None:
		print(search, found)
		(_, maxLoc, r) = found
		(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
		(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
		cv2.rectangle(search_image, (startX, startY), (endX, endY), (0, 0, 255), 2)
		cv2.imshow("Image", search_image)
		cv2.waitKey(3000)