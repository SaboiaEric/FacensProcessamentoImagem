import numpy as np
import cv2


kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype = np.uint8)


dados =  np.array([[1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                  [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
                  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                  [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]], dtype = np.uint8)

saida = np.zeros((10,10), dtype = np.uint8)

for col in range(0, len(dados[0]), 3):
    for lin in range(0, len(dados), 1):
        if(dados[col:col+3,lin:lin+3].shape == kernel[:,:].shape):
            if(np.array_equal(dados[col:col+3,lin:lin+3], kernel[:,:])):
                saida[col+1,lin+1] = 1

print("Total de erosões realizadas: %d"%np.count_nonzero(saida))

kernel_2 = np.array([1, 1, 1, 1], dtype = np.uint8)

for lin in range(0, len(saida[0]), 3):
    for col in range(0, len(saida), 1):
        if(saida[col,lin:lin+4].shape == kernel_2.shape):
            if(np.array_equal(saida[lin+1,col:col+4], kernel_2)):
                saida[lin+1, col+1] = 0
                saida[lin+1, col+2] = 0

print("Quadrados existentes  %d"%np.count_nonzero(saida))


#Eric Saboia - 140730
#Guilherme Panayotou - 140114
