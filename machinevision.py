import numpy as np
from functools import reduce
import math

def itpl(x, X, y, Y, Vxy, VXy, VxY, VXY, P):
    a = (X - x) * (Y - y)
    b = np.array([X - P[0], P[0] - x])
    c = np.array([[Vxy, VxY], [VXy, VXY]])
    d = np.array([[Y - P[1]], [P[1] - y]])
    V = float(reduce(np.dot,[1/a, b, c, d]))
    return V

def rgb2gray(I):
    S = I.shape
    Igray = I[:,:,0] * 0.3 + I[:,:,1] * 0.59 + I[:,:,2] * 0.11
    return Igray

def imrotate(I, angle):
    R = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    S = I.shape
    a = np.array([[0], [S[1]]])
    b = np.array([[S[0]], [0]])
    c = np.array([[S[0]], [S[1]]])
    A = np.dot(R,a)
    B = np.dot(R,b)
    C = np.dot(R,c)
    Xmin = int(min(A[0], B[0], C[0], 0))
    Xmax = int(max(A[0], B[0], C[0], 0))
    Ymin = int(min(A[1], B[1], C[1], 0))
    Ymax = int(max(A[1], B[1], C[1], 0))
    I_rotate = np.empty([Xmax - Xmin, Ymax - Ymin])
    translation = np.array([1,0,-Xmin,0,1,-Ymin,0,0,1]).reshape(3,-1)
    rotation = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    matrix = np.dot(translation, rotation)
    MATRIX = np.linalg.inv(matrix)
    for i in range(Xmax - Xmin):
        for j in range(Ymax - Ymin):
            origin_coordinate = np.dot(MATRIX, np.array([[i],[j],[1]]))
            x = int(origin_coordinate[0][0])
            X = int(origin_coordinate[0][0]) + 1
            y = int(origin_coordinate[1][0])
            Y = int(origin_coordinate[1][0]) + 1
            if min(x, y) < 0 or X >= S[0] or Y >= S[1]:
                I_rotate[i,j] = 255
            else:
                Vxy = I[x,y]
                VXy = I[X,y]
                VxY = I[x,Y]
                VXY = I[X,Y]
                P = [origin_coordinate[0][0],origin_coordinate[1][0]]
                V = itpl(x, X, y, Y, Vxy, VXy, VxY, VXY, P)
                I_rotate[i,j] = V
    return I_rotate

def imscale(I, factorx, factory):
    S = I.shape
    size = [int((S[0] - 1) * factorx), int((S[1] - 1) * factory)]
    I_scale = np.empty(size)
    for i in range(size[0]):
        for j in range(size[1]):
            origin_coordinate = [i / factorx, j / factory]
            x = int(origin_coordinate[0])
            X = int(origin_coordinate[0]) + 1
            y = int(origin_coordinate[1])
            Y = int(origin_coordinate[1]) + 1
            Vxy = I[x,y]
            VXy = I[X,y]
            VxY = I[x,Y]
            VXY = I[X,Y]
            P = [origin_coordinate[0],origin_coordinate[1]]
            V = itpl(x, X, y, Y, Vxy, VXy, VxY, VXY, P)
            I_scale[i,j] = V
    return I_scale

def gammacorrection(I, gamma):
    S = I.shape
    gmax = I.max()
    I_gamma = np.empty([S[0], S[1]])
    for i in range(S[0]):
        for j in range(S[1]):
            I_gamma[i,j] = gmax * (I[i,j]/ gmax) ** gamma
    return I_gamma

def histogramm(I, resolution = 1):
    a = math.ceil(256 / resolution)
    H = [1 for i in range(a)]
    H = np.array(H)
    S = I.shape
    for i in range(S[0]):
        for j in range(S[1]):
            H[int(I[i,j]//resolution)] = H[int(I[i,j]//resolution)] + 1
    return H / H.sum()

def hdri(*I):
    S = I[1].shape
    print(group)
    I_group = np.empty([len(I), S[0], S[1]])
    for i in range(len(I)):
        I_group[i,:,:] = I[i]
    return True
