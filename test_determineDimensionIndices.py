#!/usr/bin/env python
from numpy import *
import ftnbp11helper as ftn

print ftn.determineflattenedindex.__doc__
dimsize = 4
ndims = 3
npoints = dimsize**ndims

testVals = range(1,dimsize**ndims + 1)
testArray = reshape(testVals,ndims*[dimsize])

print testArray

funcInds =  ftn.mapdimensionindices(npoints=npoints,dimsize=dimsize,ndims=ndims)
for i in range(npoints):
  
  k = ftn.determineflattenedindex(idimcounters=funcInds[i,:],dimsize=dimsize)

  funcInds[i,:] -= 1 
  
  print funcInds[i,:] + 1, \
        i+1,k,testArray[funcInds[i,0],funcInds[i,1],funcInds[i,2]]
