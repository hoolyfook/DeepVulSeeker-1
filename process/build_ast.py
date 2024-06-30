from sklearn import tree
import string
import numpy as np
import os

path = "../data/c"
fileList = os.listdir(path) 
os.chdir(path) 
num = 0  
for fileName in fileList:
    num += 1
print(num)

ast_matrix = np.ones((num, 200, 200)) * (-1)

#check working folder
# import subprocess
# result = subprocess.run(['pwd'], capture_output=True, text=True)
# print(result.stdout)

for j in range(0, num):
    path_ast =str(j+1) + ".c"
    if os.path.isfile(path_ast):
        with open(path_ast, "r", encoding='utf8') as f:
            c = f.readlines()
            fin = 0
            head_node = c[0][0:9]
            n = 0
            for i in c:
                if i[0:11] == '  ' + head_node:
                    fin += 1
                if fin > 1:
                    if i != c[-1]:
                        m = int(i[7]) * 100 + int(i[8]) * 10 + int(i[9]) - 100
                        m1 = int(i[20]) * 100 + int(i[21]) * 10 + int(i[22]) - 100
                        if m < 200 and m1 < 200:
                            ast_matrix[j][m][m1] = 1
                            ast_matrix[j][m1][m] = 1
                elif fin <= 1 and i != c[0]:
                    s = int(i[5]) * 100 + int(i[6]) * 10 + int(i[7]) - 100
                    if s < 200:
                        ast_matrix[j][s][s] = 1
                        n += 1
        f.close()
print("shape:")
print(ast_matrix.shape)
np.save("../../data/ast/test_ast.npy", ast_matrix)
