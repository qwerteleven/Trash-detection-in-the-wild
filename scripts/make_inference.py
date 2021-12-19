import multiprocessing
import cv2
import torch
import compress_json
from detectron2.utils.visualizer import Visualizer
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
import os
import json


def make_analysis():
    """
    COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x/139653917/model_final_2d9806.pkl
    COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl
    COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x/138205316/model_final_a3ec72.pkl


    COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x/139173657/model_final_68b088.pkl
    COCO-Detection/faster_rcnn_R_101_FPN_3x/137851257/model_final_f6e8b1.pkl
    COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl

    """

    #model_inference_test("/mask_rcnn_X_101_32x8d_FPN_3x",
    #                     "COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x/139653917/model_final_2d9806.pkl")

    #model_inference_test("/mask_rcnn_R_50_FPN_3x",
    #                     "COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl")

    #model_inference_test("/mask_rcnn_R_101_FPN_3x",
    #                     "COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x/138205316/model_final_a3ec72.pkl")

    model_inference_test("/faster_rcnn_X_101_32x8d_FPN_3x",
                         "COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x/139173657/model_final_68b088.pkl")

    model_inference_test("/faster_rcnn_R_101_FPN_3x",
                         "COCO-Detection/faster_rcnn_R_101_FPN_3x/137851257/model_final_f6e8b1.pkl")

    model_inference_test("/faster_rcnn_R_50_FPN_3x",
                         "COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl")


    print("done")


def start_thead(target):
    """
    to prevent the models from getting the resources of
    the graph, they are launched as threads

    """
    p = multiprocessing.Process(target=target)
    p.start()
    p.join()


def model_inference_test(model_name, url_weigth):
    count = 0
    if count > 98:
        return

    with open('./annotations.json') as f:
        data = json.load(f)
    cfg = get_cfg()
    cfg.merge_from_file("." + model_name + ".yaml")
    cfg.MODEL.WEIGHTS = "detectron2://" + url_weigth
    pred = DefaultPredictor(cfg)
    os.makedirs("./RESULTS/Datos" + model_name, exist_ok=True)
    os.makedirs("./Images_inference" + model_name, exist_ok=True)

    for i in range(1, 15):
        os.makedirs("./RESULTS/Datos" + model_name + "/batch_" + str(i), exist_ok=True)
        os.makedirs("./Images_inference" + model_name + "/batch_" + str(i), exist_ok=True)


    with torch.no_grad():
        for image in data['images']:
            inputs = cv2.imread('./Dataset_test/' + image['file_name'])
            outputs = pred(inputs)
            os.makedirs("./RESULTS/Datos" + model_name + "/" + image['file_name'].split("/")[0], exist_ok=True)
            instance = outputs["instances"]

            path = "./RESULTS/Datos" + model_name + "/" + image['file_name'].split(".")[0] + ".json"

            compress_json.dump({'pred_boxes': instance.pred_boxes.tensor.tolist(),
                'scores': instance.scores.tolist(),
                'pred_classes': instance.pred_classes.tolist(),
                #'pred_masks': instance.pred_masks.tolist()
                },
                path + ".gz")

        # visualizacion de los resultados
            if count < 100:
                count = count + 1
                v = Visualizer(inputs[:, :, ::-1])
                out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
                cv2.imwrite("./Images_inference" + model_name + "/" + image['file_name'], out.get_image()[:, :, ::-1])
            if count > 98:
                return

            print("Vamos por la imagen numero: ", image['file_name'], "\n")


if __name__ == '__main__':
    make_analysis()