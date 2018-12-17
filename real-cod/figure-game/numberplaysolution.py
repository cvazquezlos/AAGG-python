# -*- coding:utf8 -*-

import random
import numpy as np



class NumberPlaySolution:
	
	def __init__(self, N):
		"""
		Constructor. 
		
		Initializes the solution with given operations.   + --> 0, * --> 1, - --> 2
		"""
		self.numbers = [75, 3, 1, 4, 50, 6, 12, 8]
		self.individualMatrix = np.random.randint(4,size=(N,7))
		#print (self.individualMatrix)
		#print ('initMat\n')
		
	def fitness(self, numbers, matrix, numind): 
		"""
		Evaluates the solution on the given numbers.
		
		Note:
		I don't check there if numbers has the right number of numbers (that 
		is: len(numbers) = len(self.operations) + 1) because I assume that 
		it's already been checked in the class NumberPlay.
		The following coding scheme has been adopted:

		+ --> 0, 
		* --> 1, 
		- --> 2.
		/ --> 3.

		Arguments:
			numbers		A list of numbers to be computed following the rules of
						this instance.
			matrix      The matrix of the individual we want to evaluate the fitness of
			numind      len(matrix) total numbers of individuals, children included			
		Returns:
			The result of the computations.
		"""
		
		fitVec = []
		
		#para los 20 individuos
		for i in range(0, numind):
			
			total = numbers[0]
			#print("total ini: ",total)
			#print("numbers[0]: ",numbers[0])
			#print("numbers: ",numbers)
			#print("matrix: ",matrix)

			for j in range(0, 7):
				if matrix[i][j] == 0:
					total += numbers[j+1]
				elif matrix[i][j] == 1:
					total *= numbers[j+1]
				elif matrix[i][j] == 2:
					total -= numbers[j+1]
				elif matrix[i][j] == 3:
					total /= numbers[j+1]
			
			#print("total final: ",total)
			fitVec.append(abs(852 -total)) # Tenga cuidado cuando llame a esta función sin evaluar todo el array podría ser un problema
		return fitVec
			
	
	def mutation(self, matrix, numind, N, threshold, points):
		"""
		Randomly changes a digit of the children.

		Arguments:
			N 	        Initial population

			numind      Len(matrix) total numbers of individuals, children included

			threshold   1-Probability of mutation (it can be decreased throughout the iterations)

			points      Number of elements of the individual to be mutated 1 <= points <= 5

		"""   
		for p in range(0,points):
			for i in range(N,numind):
				if 	np.random.uniform() > threshold:
						matrix[i][random.randint(0,6)] = random.randint(0,3)                 

		return matrix

	
	def probCrossover(self, matrix, fitVec, NM):
	
		"""
		Same as previuos crossover function, but now the selection
		of the parents is probabilistic
		
		Arguments:

			matrix  Matrix of individuals

			fitVec  Vector with fitness values of the
					individuals in the matrix
			NM      Number of pairs to be crossed,
		            giving birth to 2*NM children
		"""
		
		fitVec = np.array(fitVec, 'double')
		probVec = fitVec
		order = []

		for i in range(0,len(fitVec)):
			probVec[i] = (1/(fitVec[i]+0.00001)) 
			

		probVec = probVec/(sum(probVec))
	

		for k in range(0,2*NM):
			randVec = []
			for h in range(0,len(fitVec)):
				randVec.append(np.random.uniform())
			order.append(np.argmax(randVec*probVec))

		
		i = 0	
		for j in range(0,NM):                        
			crosspoint = random.randint(1,6)	    #devuelve un número entero entre 1 y 4, para elegir los puntos de cruce                              
			#print("matrix[order[i]][:crosspoint]: ",matrix[order[i]][:crosspoint])
			#print("matrix[order[i+1]][crosspoint:]: ",matrix[order[i+1]][crosspoint:])
			tmpvec1 = np.append(matrix[order[i]][:crosspoint],matrix[order[i+1]][crosspoint:]) #first child
			#print("matrix[order[i+1]][:crosspoint]: ",matrix[order[i+1]][:crosspoint])
			#print("matrix[order[i]][crosspoint:]: ",matrix[order[i]][crosspoint:])
			tmpvec2 = np.append(matrix[order[i+1]][:crosspoint],matrix[order[i]][crosspoint:]) #second child
			matrix = np.vstack([matrix,tmpvec1])
			matrix = np.vstack([matrix,tmpvec2])
			i+=2
		
		return matrix

	def replace(self, matrix, fitVec, N):

		"""
		Keeps N best-fitness individuals, sorts the new matrix
		by ascending fitness values

		Arguments:
			N 		population initial size

		"""
		
		sortvec = np.argsort(fitVec)
		tempmatrix = np.empty((0,7), int)
		matrix = np.matrix(matrix)
		
		for i in range(0, N):
			tempmatrix = np.append(tempmatrix, matrix[sortvec[i]][:], axis=0)

		tempmatrix = np.array(tempmatrix)

		return tempmatrix


	def probReplace(self, matrix, fitVec, N):

		"""
		Same as before but the replacement is now 
		probabilistic

		Arguments:
			N 		population initial size

		"""
		
		fitVec = np.array(fitVec, 'double')
		probVec = fitVec
		order = []

		for i in range(0,len(fitVec)):
			probVec[i] = fitVec[i]/sum(fitVec)
		

		for k in range(0,N):
			randVec = []
			for h in range(0,len(fitVec)):
				randVec.append(np.random.uniform())
			order.append(np.argmax(randVec*probVec))

		print (order)

		tempmatrix = np.empty((0,7), int)
		matrix = np.matrix(matrix)
		
		for i in range(0, N):
			tempmatrix = np.append(tempmatrix, matrix[sortvec[i]][:], axis=0)

		tempmatrix = np.array(tempmatrix)

		return tempmatrix













	