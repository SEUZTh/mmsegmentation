import cv2
import os
from PIL import Image
import numpy as np
path = '/media/zth/T7/毕业设计/数据集/ttpla-DatasetNinja/chasedb1_format/annotations/validation'
for i in os.listdir(path):

    masks = np.array(Image.open(os.path.join(path, i)).convert('L'))
    # masks = cv2.(os.path.join(path, mask), cv2.IMREAD_GRAYSCALE)

    masks[masks==255] = 1
    masks = Image.fromarray(masks).convert('L')
    masks.save(os.path.join(path, i))
    # cv2.imwrite(os.path.join(path, mask), masks)