# import numpy as np
# import glob
# import cv2
#
#
# img_array = []
# for filename in glob.glob('GroundtruthSeq/RawImages/*.bmp'):
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width, height)
#     img_array.append(img)

# out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
#
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()
import cv2
import glob
import re

img_array = []
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

for filename in sorted(glob.glob('GroundtruthSeq/RawImages/*.bmp') , key=numericalSort):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

# out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('final_project.mp4', fourcc, 20.0, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()