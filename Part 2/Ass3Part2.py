from scipy.io import wavfile
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from numpy  import array
#################
#Function to reverse bits (from geeks for geeks)
##################
def reverseBits(num,bitSize): 
  
     binary = bin(num) 

     reverse = binary[-1:1:-1] 
     reverse = reverse + (bitSize - len(reverse))*'0'
  
     return int(reverse,2) 



###########
#function to reverse array elements according to reversed indices
############
def reverseArray (dataIn, N):
	data2 = np.zeros(shape = N, dtype=np.complex_)
	for i in range (N):
		i2 = bin(i)[2:].zfill(13)
		rindex = reverseBits(i, 13)
		data2[rindex] = dataIn[i]
	return data2



###########
#FFT function
############
def fft (data, N, size):
	dataIn = reverseArray(data, size)
	for i in range (0, N):
		dataIn = butterfly(dataIn, np.power(2,i), size)
	return dataIn



###########
#Calculation of Butterfly for fft
############
def butterfly (a1, N, size):
	out = []
	j = 0
	while j < size:
		out1 = np.zeros(shape = N, dtype=np.complex_)
		out2 = np.zeros(shape = N, dtype=np.complex_)
		for i in range (0,N):
			out1[i] =  a1[i + j] + W(i, 2 * N) * a1[N + i + j]
			out.append(out1[i])
		for i in range (0, N):
			out2[i] = a1[i + j] + W(N+i, 2 * N) * a1[N + i + j]
			out.append(out2[i])
		j += (2*N)
	return out



###########
#IFFT function
############
def ifft (data, N, size):
	dataIn = reverseArray(data, size)
	for i in range (0, N):
		dataIn = ibutterfly(dataIn, np.power(2,i), size)
	for i in range (0, size):
		dataIn[i] = 1.0/size * dataIn[i]
	return dataIn


###########
#Calculation of Butterfly for ifft
############
def ibutterfly (a1, N, size):
	out = []
	j = 0
	while j < size:
		out1 = np.zeros(shape = N, dtype=np.complex_)
		out2 = np.zeros(shape = N, dtype=np.complex_)
		for i in range (0,N):
			out1[i] =  a1[i + j] + W(-1*i, 2 * N) * a1[N + i + j]
			out.append(out1[i])
		for i in range (0, N):
			out2[i] = a1[i + j] + W(-1*(N+i), 2 * N) * a1[N + i + j]
			out.append(out2[i])
		j += (2*N)
	return out




###########
#Calculation of W
############
def W (m, N): 
	return (np.cos(-1 * 2 * cmath.pi * m / N) + (np.sin( -1 * 2 * cmath.pi * m / N) * 1j))


# ###########
# #Testing butterfly
# ############
# x1 = [0.3535, 0.3535, 0.6464, -1.3535, 0.3535, -1.0607, 1.0607, -0.3535]
# x = butterfly (x1,  1, 8)
# x = butterfly (x, 2, 8)
# x = butterfly (x, 4, 8)
# print x
# print len(x)



# ###########
# #Testing fft
# ############
# x2 = [0.3535, 0.3535, 0.6464, 1.0607, 0.3535, -1.0607, -1.3535, -0.3535]
# fftout = fft(x2, 3, 8)
# print fftout



# ###########
# #Testing ifft
# ############
# print x2
# ifftout = ifft(fftout, 3, 8)
# print ifftout

rate, data = wavfile.read("whistle.wav")

data = np.pad(data, (0,192), 'constant', constant_values=(0))

fftOutput = fft (data, 13 , 8192)
draw = array(fftOutput)


dom = np.arange(0, 8192, 1)
plt.figure(1)
plt.stem(dom , abs(draw), 'c')
plt.hold()
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

filer = np.zeros(shape = 8192)

for i in range (0, 8192):
	# /if ((i>6700)):
	if (i<1300 or i>6700 or (i>1800 and i<6200)):
		filer[i] = 1
	else:
		filer[i] = 0.01

ifftIn = draw * filer

dom = np.arange(0, 8192, 1)
plt.figure(2)
plt.stem(dom , abs(ifftIn), 'c')
plt.hold()
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

ifftOutput = ifft (ifftIn, 13, 8192)

listen = array(ifftOutput)

wavfile.write("output.wav", rate, listen.real)


