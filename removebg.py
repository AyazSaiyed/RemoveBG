
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
import cv2

# image = cv2.imread(args["image"])

def TakeImage(image):
	img = image
	from remove_bg_api import RemoveBg
	# Initialize api wrapper
	API_TOKEN = 'hopYgByRwBcqfSWHnhqnQSUT'
	removebg = RemoveBg(API_TOKEN)  
	# Send and save the finished image
	image = removebg.remove_bg_file(input_path=img, out_path="./a.png", size="preview", raw=False)  
	# Print path
	print("Image was saved along the path: {}".format(image))
	newimg = cv2.imread(image)
	oldimg = cv2.imread(img)
	cv2.imshow("Background Removed ",newimg)
	cv2.imshow("Original Image ",oldimg)
	# cv2.imshow("Background Removed ",oldimg)
	cv2.waitKey(0)


print("args",args["image"])
TakeImage(args["image"])