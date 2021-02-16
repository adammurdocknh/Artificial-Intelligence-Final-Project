import numpy as np

# weights = np.array([ 2.72945449e-02, -4.56520008e-01, -3.05190125e+00,  3.02470025e+00,
#         5.88618485e-01, -8.24037571e-02, -5.60063530e-01,  6.10677734e-01,
#         8.45962219e-01, -1.89185232e-01,  4.97685142e-03, -1.11223591e+01,
#         3.28843658e-01], dtype=np.float64)

weights = np.array([-1.89366865,  -0.04759322,  -2.1505478,   4.77749568,
                    0.15633033,   0.01802283,  -0.98560086,   1.39409031,
                    1.2312503,  -0.10300409,  -1.38980471, -15.5746161,
                    -4.48386685])

# weights = np.array([])
# If you want to generate random values
# weights = np.random.rand(13,)

alpha = .000003

# mainSheet = np.load('./src/mainForTesting.npy')

mainSheet = np.load('./src/test-data.npy')

# mainSheet[0,0] = 18

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

avgWin = np.mean(win_ratio_sheet)

userNames = ["impact","ssumday","hauntzer","blaber","bang"]
avg_error = np.zeros(1, dtype='float64')
avg_prediction = np.zeros(1,dtype='float64')
avg_delta = np.zeros(1,dtype='float64')

for i in range(cycles):
    j = 0 
    for row in players_sheet:
        if row[0] > 8:
            index = j
            prediction = row.dot(weights)
            
            error = (win_ratio_sheet[j] - prediction) ** 2
            
            delta = prediction - win_ratio_sheet[j]
            weights = weights - (alpha * (row * delta))
            
            # print("Error:" + str(error) + " Prediction:" + str(prediction))
            avg_error = np.append(avg_error,error)
            avg_prediction = np.append(avg_prediction,prediction)
            avg_delta = np.append(avg_delta,delta)
            print("Player:", userNames[j])
            print("Winrate:", win_ratio_sheet[j])
            print("Targon WR:", prediction)
            print("Error", np.sqrt(error))
            print(">==============<")
            j += 1
        
        else:
            j += 1
    

    finalPredition = prediction
    # if i % (cycles/100) == 0:
    #     print('Cycle i:', i)
    #     print('Target:', avgWin)
    #     print('Prediction:', np.mean(avg_prediction))
    #     print('Avg Error', np.sqrt(np.mean(avg_error)))
    #     print('Delta:', np.mean(avg_delta))
        

    #     avg_error = np.zeros(1, dtype='float64')
    #     avg_prediction = np.zeros(1,dtype='float64')
    #     avg_delta = np.zeros(1,dtype='float64')
        
    # if i == cycles - 2:
    #     avg_error = np.zeros(1, dtype='float64')
    #     avg_prediction = np.zeros(1, dtype='float64')
    #     avg_delta = np.zeros(1, dtype='float64')
    
    # if i == cycles - 1:
    #     print('Last Cycle')
    #     print('Target:', avgWin)
    #     print('Prediction:', np.mean(avg_prediction))
    #     print('Avg Error', np.sqrt(np.mean(avg_error)))
    #     print('Delta:', np.mean(avg_delta))

    #     avg_error = np.zeros(1, dtype='float64')
    #     avg_prediction = np.zeros(1, dtype='float64')
    #     avg_delta = np.zeros(1, dtype='float64')
        
print(repr(weights))
