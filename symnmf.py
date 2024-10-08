import sys
import pandas as pd
import numpy as np
import math
import os
import mysymnmf as sy

def print_result(result):
    for row in result:
        format_row = ["%.4f" % num for num in row]
        print(*format_row,sep=",")
#check for correct amount of arguments and valid goal recieved from the user
num_args = len(sys.argv) - 1
if(num_args == 3):
    k = (int)(sys.argv[1])
    goal = sys.argv[2]
    check = os.path.isfile(sys.argv[3])
    if not (check):
        print("An Error Has Occurred")
        exit()
    txtFile = sys.argv[3]
elif(num_args == 2):
    goal = sys.argv[1]
    check = os.path.isfile(sys.argv[2])
    if not (check):
        print("An Error Has Occurred")
        exit()
    txtFile = sys.argv[2] 
else:
    print("An Error Has Occurred")
    exit()

EPS = 0.0001
iter = 300
df1 = pd.read_csv(txtFile,sep = ",",header=None,float_precision='high')
points = df1.values.tolist()

if(goal == "sym"):
    result = sy.sym(points)
    print_result(result)
elif(goal == "ddg"):
    result = sy.ddg(points)
    print_result(result)
elif(goal == "norm"):
    result = sy.norm(points)
    print_result(result)
elif (goal == "symnmf"):
    if (k >= len(points)):
        print("An Error Has Occurred")
        exit()
    w = sy.norm(points)
    m = np.mean(w)
    n = len(points)
    np.random.seed(0)
    H = [[np.random.uniform(0,2*math.sqrt(m/k)) for _ in range(k)] for _ in range(n)]
    result = sy.symnmf(H,w,iter,EPS)
    print_result(result)

else:
    print("An Error Has Occurred")
    exit()



