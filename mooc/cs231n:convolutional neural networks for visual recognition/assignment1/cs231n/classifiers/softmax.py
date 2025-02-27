from builtins import range
import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):

	"""
	Softmax loss function, naive implementation (with loops)

	Inputs have dimension D, there are C classes, and we operate on minibatches
	of N examples.

	Inputs:
	- W: A numpy array of shape (D, C) containing weights.
	- X: A numpy array of shape (N, D) containing a minibatch of data.
	- y: A numpy array of shape (N,) containing training labels; y[i] = c means
	  that X[i] has label c, where 0 <= c < C.
	- reg: (float) regularization strength

	Returns a tuple of:
	- loss as single float
	- gradient with respect to weights W; an array of same shape as W
	"""
	# Initialize the loss and gradient to zero.
	loss = 0.0
	dW = np.zeros_like(W)

	#############################################################################
	# TODO: Compute the softmax loss and its gradient using explicit loops.     #
	# Store the loss in loss and the gradient in dW. If you are not careful     #
	# here, it is easy to run into numeric instability. Don't forget the        #
	# regularization!                                                           #
	#############################################################################
	# *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
	# The value -Si is gone because u take the derivative with respect to Si on both sides i believe 
	for i in range(X.shape[0]):
		theta = X[i].dot(W) # row of values for each class
		theta -= max(theta)
		total = np.sum(np.exp(theta))

		Si = np.exp( theta [ y[i] ]) / total
		loss += -np.log( Si )
		for j in range(len(theta)):
			if j == y[i]:
				# dW[:,y[i]] += X[i,:] * (Si * (1 - Si)) # Si (1 - Sj)
				dW[:, y[i]] += (Si - 1) * X[i,:]
			else:
				Sj = np.exp(theta[j]) / total
				# print(Si)
				# print(Sj) 
				# dW[:,j] += X[i,:] * Si * Sj * -1  #Si * -1*Sj
				dW[:, j] += Sj * X[i,:]	
	loss /= X.shape[0]
	loss += reg * np.sum (W*W)

	dW /= X.shape[0]
	dW += W * reg
	# *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

	return loss, dW

# Weird fucking bug in the jupyter notebook where it's reading cached data or something?????? 
# Its not running the updated version of soft_max_loss_vectorized 
def softmax_loss_vectorized(W, X, y, reg):
	"""
	Softmax loss function, vectorized version.

	Inputs and outputs are the same as softmax_loss_naive.
	"""
	# Initialize the loss and gradient to zero.
	loss = 0.0
	dW = np.zeros_like(W)

	#############################################################################
	# TODO: Compute the softmax loss and its gradient using no explicit loops.  #
	# Store the loss in loss and the gradient in dW. If you are not careful     #
	# here, it is easy to run into numeric instability. Don't forget the        #
	# regularization!                                                           #
	#############################################################################
	# *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
	
	# calculating loss
	scores = X.dot(W)
	maxes = np.max(scores, axis = 1).reshape(scores.shape[0], 1)
	scores -= maxes
	scores = np.exp(scores)
	sums = np.sum(scores, axis = 1)
	# print(scores)
	# print(sums[0])
	scores /= sums.reshape(sums.shape[0], 1)
	loss_all = scores[(np.arange(scores.shape[0])), y]
	# print(sums.reshape(sums.shape[0], 1)[0])
	loss = np.sum(-np.log(loss_all))
	loss /= X.shape[0]
	# print(loss)
	loss += np.sum (W*W) * reg

	# calculating gradient
	# print(scores[0])
	scores [(np.arange(scores.shape[0])), y] -=1
	# print(scores[0])
	dW = X.T.dot(scores)
	dW /= X.shape[0]
	dW += W * reg


	# *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

	return loss, dW
