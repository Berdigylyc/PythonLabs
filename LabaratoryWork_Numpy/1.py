from PIL import Image
import numpy as np

input_path = 'lunar_images\\lunar01_raw.jpg'

def contrast_recovery(file_path):

    img = Image.open(file_path)
    data = np.array(img)
    #print (data)
    min_val = np.min(data)
    max_val = np.max(data)
    #print (min_val, max_val)

    edited_data = ((data - min_val) * (255 / (max_val - min_val)))
    #print (stretched_data)
    edited_data = np.clip(edited_data, 0, 255).astype(np.uint8)

    res_img = Image.fromarray(edited_data)
    res_img.save('1.jpg')

contrast_recovery(input_path)
