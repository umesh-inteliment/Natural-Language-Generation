import numpy as np

EVENTS_DATASET_PATH = './weather/all.events'
DESC_LABELS_PATH = './weather/all.text'


ordinal_mappings = { 'WNW':13,
 'Def':400, 'N':1, 'SSW':14, 'S':2, 'SE':6, 
 'NNE':9, 'Lkly':300, 'SW':7, 'SSE':11, 
  'ENE':12, 'NW':8, 'E':3, 'NNW':10,
   'SChc':100, 'NE':5, 'WSW':16, 
   'ESE':15, 'W':4, 
   'Chc':200,'--':-999,'':-999}


f = open(EVENTS_DATASET_PATH,'r')
data = f.read()

f = open(DESC_LABELS_PATH,'r')
labels = f.read()

lines =data.split('\n')
labels = labels.split('\n')

x = [] #features
y = [] #labels
flag = False
for i,(line,label) in enumerate(zip(lines,labels)):
    attr = line.split()
    vec = []
    if len(attr) == 83:
        try:
            for at in attr:
                #print(at)
                vals = at.split(":")
                cols = vals[0].split(".")
                if cols[1] == 'mode':
                        vec.append(ordinal_mappings[vals[1]])
                elif '-' in vals[1]:
                    nums = vals[1].split("-")
                    vec.append(int(nums[0]))
                    vec.append(int(nums[1]))
                elif vals[1] == '--':
                    vec.append(-999)
                else:
                    vec.append(int(vals[1]))
            x.append(np.array(vec))
            y.append(label)
            
        except Exception as e:
            pass
        

import pickle
with open('dataset.pkl','wb') as data:
    pickle.dump((x,y),data)



            
            
                


