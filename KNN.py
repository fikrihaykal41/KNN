import pandas as p

dataTest = p.read_csv('DataTest_Tugas3_AI.csv')
dataTrain = p.read_csv('DataTrain_Tugas3_AI.csv')

k = 5

predict = []
for i in range(0,len(dataTest)):
    distance = []
    for j in range(0,len(dataTrain)):
        distanceResult = abs((dataTest.loc[i].values[1]) - (dataTrain.loc[j].values[1])) +\
                         abs((dataTest.loc[i].values[2]) - (dataTrain.loc[j].values[2])) +\
                         abs((dataTest.loc[i].values[3]) - (dataTrain.loc[j].values[3])) +\
                         abs((dataTest.loc[i].values[4]) - (dataTrain.loc[j].values[4])) +\
                         abs((dataTest.loc[i].values[5]) - (dataTrain.loc[j].values[5]))
        distance.append([distanceResult,(dataTrain.loc[j].values[6])])
    distance.sort()
    label0 = 0;label1 = 0;label2 = 0;label3 = 0;label4 = 0
    for i in range(k):
        if(distance[i][1]==0):
            label0 = label0 + 1
        elif(distance[i][1]==1):
            label1 = label1 + 1
        elif(distance[i][1]==2):
            label2 = label2 + 1
        elif(distance[i][1]==3):
            label3 = label3 + 1
        elif(distance[i][1]==4):
            label4 = label4 + 1

    if(max(label0,label1,label2,label3,label4)==label0):
        predict.append(0)
    elif(max(label0,label1,label2,label3,label4)==label1):
        predict.append(1)
    elif(max(label0,label1,label2,label3,label4)==label2):
        predict.append(2)
    elif(max(label0,label1,label2,label3,label4)==label3):
        predict.append(3)
    elif(max(label0,label1,label2,label3,label4)==label4):
        predict.append(4)

print(predict)

PredictResult = p.DataFrame(predict)
PredictResult.to_csv('TebakanTugas3.csv')