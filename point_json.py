import json

x_list=[]
y_list=[]
width_list=[]
height_list=[]
save_file='C:/Users/aaa/Desktop/9th Apple/json1/'

with open('C:/Users/aaa/Desktop/9th Apple/1~10/via_project_8Sep2021_12h24m_json.json', 'r') as f:

    json_data = json.load(f)
    file_name=list(json_data.keys())
    print(file_name)
    
    for i in range(12):
        print(file_name[i])
        name=file_name[i]
        for k in json_data[name]["regions"]: #x 개수 어케 알지
            x=k['shape_attributes']['x']
            y=k['shape_attributes']['y']
            width=k['shape_attributes']['width']
            height=k['shape_attributes']['height']
            
            xmax=x+width
            ymax=y+height
            
            x=str(k['shape_attributes']['x'])
            y=str(k['shape_attributes']['y'])
            xmax=str(xmax)
            ymax=str(ymax)
            
            with open(save_file+name+'.txt', 'a') as f:
                f.write(f'apple {x} {y} {xmax} {ymax}\n')


f.close()
