from objectdetection import objectdetection 
from posedetection import *
import emotion_detection
import cv2
import os.path
import sys

input_location = ''
save_location = ''
#detection flags
i_l = False #locations
s_l = False

o_d = False #detections
p_d = False
e_d = False

if len(sys.argv) == 1:
    print("Wrong number of arguments.")
    exit(0)

itr = iter(range(1,len(sys.argv)))
for i in itr:
    # print(i)
    current_arg = sys.argv[i]
    # print(current_arg)
    if current_arg[0] == '-':
        if 'o' in current_arg:
            s_l = True
            if i < len(sys.argv):
                save_location = sys.argv[i+1]
            else:
                print("Wrong number of arguments.")
                exit(0)
            next(itr)
        if 'a' in current_arg:
            o_d = True
            p_d = True
            e_d = True     
        if 'd' in current_arg:
            o_d = True
        if 'p' in current_arg:
            p_d = True
        if 'e' in current_arg:
            e_d = True
    elif not i_l:
        input_location = sys.argv[i]
        i_l = True
    else:
        print("Wrong number of arguments.")
        exit(0)

input_location = os.path.abspath(input_location)
save_location = os.path.abspath(save_location)

if not i_l:
    print("No input image.")
    exit(0)


temp = cv2.imread(input_location)
input_path_head,input_path_tail = os.path.split(input_location)

if o_d or p_d or e_d:
    if p_d:
        temp = pose_detection.poseDetection(input_location)
        # print(temp)
    if o_d:
        rectangles = objectdetection.get_people_coordinates(input_location)
        print(rectangles)
        for i in rectangles:
            print((i[0],i[1]),(i[2],i[3]),(255,0,0),2)
            cv2.rectangle(temp,(i[0],i[1]),(i[2],i[3]),(255,0,0),2)
    if e_d:
        rectangles = emotion_detection.get_emotions(input_location)
        for i in rectangles:
            cv2.rectangle(temp,i[0],i[1],(255,0,0),2)
            # TODO:add emotion text
        print(rectangles)
if not s_l:
    save_location = input_path_head + '/a.jpg'
cv2.imwrite(save_location,temp)
# print(input_location,save_location,end=' ')
# print()
# print(o_d,p_d,e_d)