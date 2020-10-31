import numpy as np
from torch._C import dtype

weights = np.array([0.56774643,  0.47112446, -1.04678128,  0.95022474,  1.09802062,
                    -0.15844113, -0.03392968, -0.01863788,  0.41180123, -0.54731532,
                    -0.22394692, -1.69846885, -0.01616816], dtype=np.float64)

# alpha = .00000001
alpha = .0000001


mainSheet = np.load('./src/main.npy')

# First 13 columns of main sheet that store data
players_sheet = mainSheet[:,:13]
weighted_sheet = np.zeros((2,13),dtype=np.float64)
print(players_sheet.dtype)
weighted_sheet = np.delete(weighted_sheet, (0), axis=0)
weighted_sheet = np.delete(weighted_sheet, (0), axis=0)
# Last column from sheet
win_ratio_sheet = mainSheet[:,15:]

print(np.size(weights))
# 1000 235.37

cycles = 1


# def Average(lst):
#     return sum(lst) / len(lst)


avgWin = np.mean(win_ratio_sheet)
# avgWin = np.empty(1,dtype='float64')
avgError = np.array(1, dtype='float64')
finalPredition = []

# for number of cycles:
#   for i in number of rows in input:
#       for cell in row
#           row weighted with np.multiply
#           pred = row summed with np.sum()
#           error = actual winrate - prediction ** 2
#           delta = prediction - actual winrate
#           new weight = old weights - (alpha * (input * delta))
#           weights = weights - (alpha * input)
#           print('Error:' + str(error))
#           print('Prediction:' + str(prediction))



for i in range(cycles):
    j = 0
    # print(weights)
    for row in players_sheet:
        
        index = j
        prediction = row.dot(weights)
        # print(prediction)
        # print(j)
        np.append(weighted_sheet,prediction)
        
        error = (win_ratio_sheet[j] - prediction) ** 2
        
        delta = prediction - win_ratio_sheet[j]
        weights = weights - (alpha * (row * delta))
        
        # print("Error:" + str(error) + " Prediction:" + str(prediction))
        np.append(avgError,error)
        # np.append(avgWin,win_ratio_sheet[j])
        # predictions.append(prediction)
        # avgError.append(error)
        # avgWin.append(win_ratio_sheet[j])
        j += 1
        
    finalPredition = prediction
    if i % (cycles/10) == 0:
        
        print('Cycle i:', i)
        print('Target:', avgWin)
        print('Prediction:', prediction)
        print('error', error)
        print('Delta:', delta)
        print(repr(weights))

# print('Final error %:', ((Average(avgError)/Average(avgWin))*100))
# print('avg error:',np.mean(avgError))
print('avg win:', avgWin, '%')
print('final prediction:',finalPredition,'%')
print(repr(weights))



                

# for i in range(cycles):
#     prediction = input.dot(weights)
    # error = (goal_prediction - prediction)
