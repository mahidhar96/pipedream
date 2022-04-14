import pickle
import numpy
from PIL import Image
import os

counter = 0

for file in os.listdir("./"):
    if file.startswith("val"):
        print('Starting '+file)
        with open(file, 'rb') as fo:
            dict = pickle.load(fo)
        labels_list = dict['labels']

        for i in range(len(labels_list)):
            img_data = dict['data'][i].reshape(3,64,64).transpose(1,2,0)

            label_info = str(dict['labels'][i])
            if(not os.path.exists('./tt/'+label_info)):
                os.makedirs('./tt/'+label_info)
            else:
                img_New = Image.fromarray(img_data,'RGB')
                img_New.save('./tt/'+label_info+'/'+str(counter)+'.jpg')
                counter+=1
        print('Completed '+file)