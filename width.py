import os

path_dir = "C:/Users/aaa/Documents/GitHub/MinneApple/Locations/for_get_AP_yx/ground-truth/"
save_dir = "C:/MinneApple/yolo_train/"
file_list = os.listdir(path_dir)

for i in range(len(file_list)):
    img_name = path_dir+'/'+file_list[i]
    f = open(img_name,"r")
    save_name =save_dir+'/'+file_list[i]
    save = open(save_name,"w")
    lines = f.readlines()

    for line in lines:
        line = line.strip('\n')
        list = line.split(' ')
        name = list[0]
        # for i in range(4):
        #     list[i+1]=str(round(float(list[i+1])))
        #print(f'{name} {list[2]} {list[1]} {list[4]} {list[3]}\n')
        width=(int(list[3])-int(list[1]))/1000
        height=(int(list[4])-int(list[2]))/1000
        x=((int(list[1])+int(list[3]))/2)/1000
        y=((int(list[2])+int(list[4]))/2)/1000
        save.write(f'53 {x} {y} {width} {height}\n')
f.close()
save.close()