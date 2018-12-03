import os
import sys
path ='..\\data\\'
sys.path.append('..\\lib\\')
with open(path + 'Harry Potter 5 - Order of the Phoenix.txt') as f1:
    file2 = f1.readlines()
print(file2)