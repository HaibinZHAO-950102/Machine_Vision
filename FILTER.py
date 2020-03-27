import numpy as np
import math
import machinevision as mv

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
