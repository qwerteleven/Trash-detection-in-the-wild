
import compress_json
import json
import os
path_labels = "./Datos/mask_rcnn_R_50_FPN_3x/"

with open("./annotations.json") as f:
    data = json.load(f)


#print(D1['pred_boxes'])
#print(data['annotations'][0]['bbox'])
#print(data['images'][0]['file_name'])

def save_csv(data):

    for instance in data:
        f.write(str(instance) + ",")
    f.write("\n")
 

def bbox_IoU(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou



f = open("./data.csv", "w")
data_AP = []

for image, annotation in zip(data['images'], data['annotations']):
    if os.path.isfile(path_labels + image['file_name'].split(".")[0] + ".json.gz"):
        prediction = compress_json.load(path_labels + image['file_name'].split(".")[0] + ".json.gz")
        GT = annotation['bbox']

        AP_image = [image['file_name']]

        for pred in prediction['pred_boxes']:
            AP = []
            if isinstance(GT[0], list):
                for GT_ in GT:
                    AP.append(bbox_IoU(pred, GT_))
                AP_image.append(max(AP))
            else:
                AP_image.append(bbox_IoU(pred, GT))

        save_csv(AP_image)
    print(image['file_name'])

f.close()


