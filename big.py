import numpy as np
from statistics import median,mean,mode



data = [10, 20, 30, 40, 50]
data2=[3, 1, 4, 1, 5, 9, 2]
data3=[6, 1, 6, 7, 9, 6, 4]

result3=mode(data3)
result = mean(data)
result2=median(data2)
print("Median:", result)
print("Media",result2)
print("Moda",result3)

media = np.mean([4, 8, 15, 16, 23, 42])  
print(media)

mediana = np.median([7, 5, 3, 1, 9, 11, 13]) 
print(mediana)