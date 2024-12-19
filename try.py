from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
def process(image):
    # cv2.destroyAllWindows()
    # cv2.imshow(f"{num}", image)
    clone = image.copy()
    gray = cv2.cvtColor(clone, cv2.COLOR_BGR2GRAY)  # convert the image to grayscale
    # cv2.imshow(f"{num} gray", gray)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # kernel for morphological operations
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    # cv2.imshow(f"{num} Opening: (5, 5)", opening)
    blurred = cv2.GaussianBlur(opening, (7, 7), 0)  # blur
    # cv2.imshow(f"{num} Blurred", blurred)
    (T, thresh) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)   # thresholding the image using Otsu's method

    labels = measure.label(thresh, background=0)
    mask = np.zeros(thresh.shape, dtype="uint8")
    for (i, label) in enumerate(np.unique(labels)):
        # ignore the background label 
        if label == 0:
            continue
        # otherwise, construct the label mask to display only connected components for the current label
        labelMask = np.zeros(thresh.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)
        # if the number of pixels in the component is sufficiently large, add it to our mask of "large" blobs
        if numPixels > 17776 and numPixels < 35000:
            mask = cv2.add(mask, labelMask)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)  
    hullImage = np.zeros(gray.shape[:2], dtype="uint8")
    
    # loop over the contours
    for (i, c) in enumerate(cnts):
        # compute the area of the contour along with the bounding box to compute the aspect ratio
        area = cv2.contourArea(c)
        (x, y, w, h) = cv2.boundingRect(c)
        # compute the aspect ratio of the contour, which is simply the width divided by the height of the bounding box
        aspectRatio = w / float(h)
        # use the area of the contour and the bounding box area to computethe extent
        extent = area / float(w * h)
        # compute the convex hull of the contour, 
        # then use the area of the original contour and the area of the convex hull to compute thesolidity
        hull = cv2.convexHull(c)
        hullArea = cv2.contourArea(hull)
        if hullArea == 0:
            continue
        solidity = area / float(hullArea)
        
        Area  = area / 1000
        
        if solidity > 0.99999 or solidity == 0.00 or Area < 3 or Area > 70:
            continue
        # visualize the original contours and the convex hull and initialize the name of the shape
        cv2.drawContours(hullImage, [hull], -1, 255, -1)
        cv2.drawContours(clone, [c], -1, (159, 0, 240), 2)
        shape = ""
        if solidity >= 0.949:
            if Area > 28:
                shape = "# Ten thousand"
            elif Area > 15:
                shape = "# 0"
            elif Area > 13:
                shape = "# B"
            elif Area > 10:
                shape = "# E"
        elif solidity >= 0.9:
            if Area > 40:
                shape = "# 40"
            elif Area > 38:
                if extent > 0.73:
                    shape = "# 90"
                else:
                    shape = "# 20"
            elif Area > 37:
                shape = "# 30"
            elif Area > 35:
                shape = "# 50"
            elif Area > 33:
                shape = "# 10"
            elif Area > 32:
                shape = "# Thousand"
            elif Area > 11:
                shape = "# F"
            elif Area > 10:
                if extent > 0.6:
                    shape = "# A"
                else:
                    shape = "# D"
            elif Area > 8:
                if extent > 0.6:
                    shape = "# M"
                else:
                    shape = "# O"
            else:
                shape = "# S"  
        elif solidity >= 0.85:
            if Area > 30:
                shape = "# 60"
            elif Area > 10:
                shape = "# Brother"
            elif Area > 8:
                shape = "# N"
            elif Area > 7:
                if aspectRatio > 0.5:
                    shape = "# H"
                else:
                    shape = "# U"
            else:
                shape = "# J"
        elif solidity >= 0.8:
            if Area >= 30:
                shape = "# Hundred"
            elif Area >= 27:
                shape = "# 9"
            elif Area >= 26:
                shape = "# 8"
            elif Area >= 20:
                shape = "# 1"
            elif Area >= 10:
                shape = "# C"
            elif Area >= 7:
                shape = "# R"
            else:
                if aspectRatio > 0.5:
                    shape = "# I"
                else:
                    shape = "# X" 
        elif solidity >= 0.747:
            if Area >= 25:
                shape = "# 6"
            elif Area >= 8:
                shape = "# W"
            elif Area >= 7.7:
                if aspectRatio > 1.4:
                    shape = "# T"
                else:
                    shape = "# P"
            elif Area >= 7.4:
                shape = "# G"
            elif Area >= 7:
                shape = "# Z"
            else:
                shape = "# K"
        elif solidity >= 0.696:
            if Area >= 27:
                shape = "# 4"
            elif Area >= 25:
                shape = "# 7"
            elif Area >= 20:
                shape = "# 2"
            elif Area >= 8:
                shape = "# Y"
            else:
                shape = "# V"    
        elif solidity >= 0.6:
            if Area >= 30:
                shape = "# 5"
            elif Area >= 25:
                shape = "# 3"
            elif Area >= 20:
                shape = "# Love"
            elif Area >= 6:
                shape = "# L"
            else:
                shape = "# Q"
        elif solidity >= 0.48:
            shape = "# 70"
        elif solidity >= 0.4:
            shape = "# 80"
        # draw the shape name on the image
        cv2.putText(clone, shape, (x, y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (240, 0, 159), 2)
        # show the contour properties
        print("Image -- aspect_ratio={:.2f}, extent={:.2f}, solidity={:.2f}, area={:.2f}".format(aspectRatio, extent, solidity, Area))
        print(shape)
        # cv2.imshow(f"{num} Convex Hull", hullImage)
        resized = imutils.resize(clone, width=image.shape[1] * 2, inter=cv2.INTER_LINEAR)
        cv2.imshow("Image", resized)
        cv2.waitKey(0)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to show the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
process(image)
'''
num_img = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 10000]
c_img = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]  
w_img = ["bro", "love"]      

for i in num_img:
    a = f"{i}.png"
    image = cv2.imread(f"img/{a}")
    process(i, image)   
    
cv2.destroyAllWindows()

for i in c_img:
    a = f"{i}.png"
    image = cv2.imread(f"img/{a}")
    process(i, image)
    
cv2.destroyAllWindows()

for i in w_img:
    a = f"{i}.png"
    image = cv2.imread(f"img/{a}")
    process(i, image)

print(f"Data: {len(num_img) + len(c_img) + len(w_img)}")
'''  