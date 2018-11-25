import cv2
import os
import argparse
import numpy as np
import utils

curdir = os.path.dirname(os.path.abspath(__file__))
parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('out')
parser.add_argument('--size',type=int,default=64)
parser.add_argument('--split',type=float,default=0.8)

def equalizeHist_color_img(img):
    channels = img.shape[-1]
    for c in range(channels):
        img[:,:,c] = cv2.equalizeHist(img[:,:,c])
    return img

def find_red_hanko(img):
    # Convert BGR to HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Binarize
    UPPER_RED1 = np.array([30,255,255], dtype=np.uint8)
    UPPER_RED2 = np.array([180,255,255], dtype=np.uint8)
    LOWER_RED1 = np.array([0,40,120], dtype=np.uint8)
    LOWER_RED2 = np.array([150,40,120], dtype=np.uint8)
    mask1 = cv2.inRange(hsv_img, LOWER_RED1, UPPER_RED1)
    mask2 = cv2.inRange(hsv_img, LOWER_RED2, UPPER_RED2)
    mask = mask1 | mask2

    # Find contours
    _,contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        ind = np.argmax([cv2.contourArea(contour) for contour in contours])
        x,y,w,h = cv2.boundingRect(contours[ind])
        return [x,y,w,h]
    else:
        return None

def main(args):

    # Make image paths
    src_paths = utils.make_paths_from_directory(args.src)

    n = 0;
    records = []
    for src_path in src_paths:
        # Read image
        src_img = cv2.imread(src_path,cv2.IMREAD_COLOR)
        src_img = equalizeHist_color_img(src_img)

        # Find hanko
        ret = find_red_hanko(src_img)
        if ret:
            x,y,w,h = ret
            #croped_img = cv2.rectangle(src_img,(x,y),(x+w,y+h),(0,0,255),2)
            #croped_img = src_img[y:y+h,x:x+w]
            #croped_img = cv2.resize(croped_img,(args.size,args.size))
            #fname = os.path.basename(src_path)
            #cv2.imwrite(os.path.join(args.dst,fname),croped_img)
            records.append('%s,%d,%d,%d,%d,%d\n' % (
                os.path.basename(src_path), # image_name
                x,x+w,y,y+h,1 # (xmin,xmax,ymin,ymax,class_id)
            ))
            n += 1

    # Save csv files
    with open(args.out,'w') as f:
        f.writelines(records)
    print('(%d/%d) images have a hanko' % (n,len(src_paths)))

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
