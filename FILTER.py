import numpy as np
import math
import machinevision as mv
from functools import reduce

def motionblur(length, direction):
    if direction > np.pi / 2 or direction <= - np.pi / 2:
        print('Direction should be in the intervall (-π/2,π/2]')
    elif direction == np.pi / 2:
        filter = np.ones([1,length]) / length
        return filter
    elif direction == 0:
        filter = np.ones([length,1]) / length
        return filter
    else:
        a = np.sign(direction)
        angle = np.abs(direction)
        flag = 0
        if angle > np.pi / 4:
            flag = 1
            angle = np.pi / 4 - angle % (np.pi / 4)
        width = math.ceil(length * np.tan(angle))
        P = np.array([[i, np.tan(angle) * i] for i in range(length)])
        crosspoint = np.empty([width - 1, 2])
        for i in range(width - 1):
            crosspoint[i,1] = i + 1
            crosspoint[i,0] = crosspoint[i,1] / np.tan(angle)
        filter = np.zeros([length,width])
        J = 0
        for i in range(length - 1):
            if P[i,1] // 1 == P[i+1,1] // 1:
                filter[int(P[i,0]),int(P[i,1] // 1)] = 1
            else:
                filter[int(P[i,0]),int(P[i,1]//1)] = crosspoint[J,0] % 1
                filter[int(P[i,0]),int(P[i,1]//1)+1] = (1 - crosspoint[J,0] % 1)
                J = J + 1
        filter[length-1, width - 1] = 1
        if flag == 1:
            filter = np.transpose(filter)
            length, width = width, length
        if a == -1:
            filter_2 = np.empty(filter.shape)
            for i in range(width):
                filter_2[:,i] = filter[:,-1-i]
            filter = filter_2
        # filter_2 = np.empty(filter.shape)
        # for i in range(length - 1):
        #     filter_2[i,:] = filter[-1-i,:]
        # filter = filter_2
        filter = filter / np.sum(filter)
        # filter = np.transpose(filter)
        # Sf = filter.shape
        # filter_temp = np.empty(filter.shape)
        # for i in range(Sf[0]):
        #     for j in range(Sf[1]):
        #         filter_temp[i,j] = filter[-1-i, -1-j]
        # filter = filter_temp
        return filter

def sobel(direction):
    filter = np.array([1,0,-1,2,0,-2,1,0,-1]).reshape(3,-1) / 8
    if direction == 'x':
        return filter
    elif direction == 'y':
        return np.transpose(filter)
    else:
        print('''direction should be 'x' or 'y'.''')

def gaussfilter(size, sigma):
    filter = np.empty([size, size])
    SIGMA = np.array([sigma, 0, 0, sigma]).reshape(2,2)
    for i in range(size):
        for j in range(size):
            x = (size + 1) / 2 - size + i
            y = (size + 1) / 2 - size + j
            p = np.array([x,y]).reshape(2,-1)
            filter[i,j] = 1 / sigma / 2 / np.pi * math.exp(- 0.5 * reduce(np.dot, [np.transpose(p), SIGMA, p]))
    filter = filter / np.sum(filter)
    return filter

def meanfilter(size):
    filter = np.ones([size, size])
    filter = filter / np.sum(filter)
    return filter

def bilateralfilter(I, size, sigma, rho):
    S = I.shape
    SI = [S[0] - size + 1, S[1] -  size + 1]
    I_filter = np.empty(SI)
    for i in range(SI[0]):
        for j in range(SI[1]):
            I_filter[i,j] = 0
            filter = np.empty([size,size])
            for m in range(size):
                for n in range(size):
                    x = int(i+(size-1)/2)
                    y = int(j+(size-1)/2)
                    filter[m,n] = math.exp(-0.5 * ((I[i+m,j+n] - I[x,y])**2) / (rho ** 2)) * math.exp(-0.5*(((m-(size-1)/2)**2)+((n-(size-1)/2)**2))/(sigma ** 2))
            filter = filter / np.sum(filter)
            for m in range(size):
                for n in range(size):
                    I_filter[i,j] = I_filter[i,j] + I[i+m,j+n] * filter[m,n]
    a = np.sign(np.min(I_filter))
    I_filter = (I_filter - a * np.min(I_filter)) / (np.max(I_filter) - np.min(I_filter)) * 255
    return I_filter

def medianfilter(I, size):
    S = I.shape
    SI = [S[0]-size+1, S[1]-size+1]
    I_filter = np.empty(SI)
    for i in range(SI[0]):
        for j in range(SI[1]):
            matrix = I[i:i+size, j:j+size].reshape(1,-1)
            matrix.sort()
            index = int((size ** 2 + 1) / 2)
            I_filter[i,j] = matrix[0,index]
    a = np.sign(np.min(I_filter))
    I_filter = (I_filter - a * np.min(I_filter)) / (np.max(I_filter) - np.min(I_filter)) * 255
    return I_filter

def prewitt(direction):
    filter = np.array([1,0,-1,1,0,-1,1,0,-1]).reshape(3,-1) / 6
    if direction == 'x':
        return filter
    elif direction == 'y':
        return np.transpose(filter)
    else:
        print('''direction should be 'x' or 'y'.''')
