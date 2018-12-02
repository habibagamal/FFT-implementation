from scipy.io import wavfile
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

#################
#Function to reverse bits (from geeks for geeks)
##################
def reverseBits(num,bitSize): 
  
     # convert number into binary representation 
     # output will be like bin(10) = '0b10101' 
     binary = bin(num) 
  
     # skip first two characters of binary 
     # representation string and reverse 
     # remaining string and then append zeros 
     # after it. binary[-1:1:-1]  --> start 
     # from last character and reverse it until 
     # second last character from left 
     reverse = binary[-1:1:-1] 
     reverse = reverse + (bitSize - len(reverse))*'0'
  
     # converts reversed binary string into integer 
     return int(reverse,2) 



###########
#function to reverse array elements according to reversed indices
############
def reverseArray (dataIn, N, numOfBits):
	data2 = np.zeros(shape = N)
	for i in range (N):
		rindex = reverseBits(i,numOfBits)
		data2[rindex] = data[i]
	return data2



###########
#FFT function
############
def fft(data, N):


###########
#Calculation of Butterfly
############
def butterfly (a1, a2, N):
	out1 = np.zeros(shape = N, dtype=np.complex_)
	out2 = np.zeros(shape = N, dtype=np.complex_)
	out = np.zeros(shape = 2*N, dtype=np.complex_)
	for i in range (0,N):
		out1[i] = a1[i] + W(i, 2*N) * a2[i]
	for i in range (0, N):
		out2[i] = a1[i] + W(N+i, 2*N) * a2[i]
	for i in range (0, N):
		out[i] = out1[i]
	for i in range (0, N):
		out[N+i] = out2[i]
	return out


###########
#Calculation of W
############
def W (m, N): 
	return (np.cos(-1 * 2 * cmath.pi * m / N) + (np.sin( -1 * 2 * cmath.pi * m / N) * 1j))


###########
#Testing butterfly
############
# x1 = [0.3535]
# x2 = [0.3535]
# print butterfly (x1, x2, 1)

# x1 = [0.6464]
# x2 = [-1.3535]
# print butterfly (x1, x2, 1)

# x1 = [0.3535]
# x2 = [-1.0607]
# print butterfly (x1, x2, 1)

# x1 = [1.0607]
# x2 = [-0.3535]
# print butterfly (x1, x2, 1)

# x1 = [0.707, 0]
# x2 = [-0.707, 1.999]
# x3 = butterfly(x1, x2, 2)
# print "x3",x3

# x1 = [-0.707, 1.414]
# x2 = [0.707, 1.414]
# x4 = butterfly(x1,x2,2)
# print "x4",x4

# print butterfly (x3, x4, 4)