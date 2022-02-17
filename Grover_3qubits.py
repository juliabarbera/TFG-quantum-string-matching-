#!/usr/bin/env python
# coding: utf-8

# ## Grover's algorithm 3 qubits

# In[1]:


import numpy as np
from qibo.models import Circuit
from qibo import gates
from qibo import callbacks
import matplotlib.pyplot as plt 


# ### ORACLE

# In[2]:


def MCZ(q0,q1,q2): # defining multi-controlled Z function 
    c.add(gates.H(q0))
    c.add(gates.TOFFOLI(q2,q1,q0))
    c.add(gates.H(q0))
    return c 


# In[3]:


def oracle(q0,q1,q2): 
    c.add(gates.X(q2)) 
    MCZ(q0,q1,q2)
    c.add(gates.X(q2))
    return c 


# ### DIFUSSION OPERATOR

# In[4]:


def difussion(q0,q1,q2): 
    for i in range(0,3):
        c.add(gates.H(i))
        
    for i in range(0,3):
        c.add(gates.X(i))
        
    MCZ(q0,q1,q2)
    
    for i in range(0,3):
        c.add(gates.X(i))
        
    for i in range(0,3):
        c.add(gates.H(i))
    return c


# ### GROVER'S ALGORITHM 1 ITERATION

# In[6]:


c = Circuit(3) # Construct the circuit (2 qubits)

for i in range(0,3):
    c.add(gates.H(i)) # Add some gates
print(c.draw())

# Rotation of the wanted state
oracle(0,1,2) 
print(c.draw())

difussion(0,1,2)
print(c.draw())

# Execute the circuit and obtain the final state
result = c() # c.execute(initial_state) also works
# should print `tf.Tensor([1, 0, 0, 0])`
print(result.state(numpy=True))
# Draw the circuit
print(c.draw())

x = ['000','001','010','011','100','101','110','111']
y = result.state(numpy=True)

prob = [x**2 for x in y] # elevating coeficients
print(prob)

fig, ax = plt.subplots()

ax.bar(x, prob, width=1, edgecolor="white", linewidth=0.7)
ax.set(ylim=(0, 1), xlabel = 'states', ylabel = 'probabilities')

plt.show()


# ### GROVER'S ALGORITHM 2 ITERATION

# In[8]:


c = Circuit(3) # Construct the circuit (2 qubits)

for i in range(0,3):
    c.add(gates.H(i)) # Add some gates

oracle(0,1,2) 

difussion(0,1,2)

oracle(0,1,2) 

difussion(0,1,2)

# Execute the circuit and obtain the final state
result = c() # c.execute(initial_state) also works
# Draw the circuit
print(c.draw())

x = ['000','001','010','011','100','101','110','111']
y = result.state(numpy=True)

prob = [x**2 for x in y] # elevating coeficients
print(prob)

fig, ax = plt.subplots()

ax.bar(x, prob, width=1, edgecolor="white", linewidth=0.7)
ax.set(ylim=(0, 1), xlabel = 'states', ylabel = 'probabilities')

plt.show()


# In[ ]:




