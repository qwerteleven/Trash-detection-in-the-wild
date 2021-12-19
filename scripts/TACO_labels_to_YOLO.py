
import cv2
import json
import sys

def get_img_shape(path):
    img = cv2.imread(path)
    try:
        return img.shape
    except AttributeError:
        print('error! ', path)
        return (None, None, None)

def convert_labels(x1, y1, x2, y2, width, height):

    '''
    Definition: Parses label files to extract label 
    and bounding box coordinates. Converts (x1, y1, x1, y2) 
    KITTI format to (x, y, width, height) normalized YOLO format.    
    '''


    def sorting(l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin

    xmax, xmin = sorting(x1, x2)
    ymax, ymin = sorting(y1, y2)
    dw = 1. / width
    dh = 1. / height
    x = (xmin + xmax)/2.0
    y = (ymin + ymax)/2.0
    w = xmax - xmin
    h = ymax - ymin
    x = x*dw 
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


f = open("annotations.json",)
training_data = json.load(f)

check_set = set()

image_id = [i ['image_id'] for i in training_data['annotations']]
category_id = [str(i['category_id']) for i in training_data['annotations']]
bbox = [i['bbox'] for i in training_data['annotations']]
filenames = [i['file_name'] for i in training_data['images']]
images_width  = [i['width'] for i in training_data['images']]
images_height = [i['height'] for i in training_data['images']]
images_id_ = [i['id'] for i in training_data['images']]


for i in range(len(training_data['annotations'])):

    kitti_bbox = [bbox[i][0], bbox[i][1], bbox[i][2] + bbox[i][0], bbox[i][3] + bbox[i][1]]
  
    index_id = images_id_.index(image_id[i])

    yolo_bbox = convert_labels(kitti_bbox[0], kitti_bbox[1], kitti_bbox[2], kitti_bbox[3], images_width[index_id], images_height[index_id])
    
    filename = filenames[index_id].split(".")[0] + ".txt"

    content = category_id[i] + " " + str(yolo_bbox[0]) + " " + str(yolo_bbox[1]) + " " + str(yolo_bbox[2]) + " " + str(yolo_bbox[3])
    
    if image_id[i] in check_set:        # Append to file files
        file = open(filename, "a")
        file.write("\n")
        file.write(content)
        file.close()
    elif image_id[i] not in check_set:
        check_set.add(image_id[i])
        # Write files
        file = open(filename, "w")
        file.write(content)
        file.close()















