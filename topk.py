
import os

path = "C:/MinneApple/apple_data/"

save_path="C:/MinneApple/yolov5x_1280_topk/"

file_list = os.listdir(path)

for line in file_list:
    
    with open(path+line, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(save_path+line, 'w') as fout:
        fout.writelines(data[:100])

fin.close()
fout.close()