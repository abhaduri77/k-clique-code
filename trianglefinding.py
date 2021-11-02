# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 10:02:01 2021

@author: hp
"""
import numpy as np
from qiskit import QuantumRegister,ClassicalRegister,QuantumCircuit,execute,BasicAer,IBMQ
from qiskit.tools.visualization import plot_histogram
from qiskit.providers.ibmq import least_busy
import matplotlib.pyplot as plt
from qiskit.dagcircuit import DAGCircuit
from qiskit.converters import circuit_to_dag
from qiskit.compiler import transpile
#from qiskit import compile
import math
from qiskit import *

pi=math.pi
import qiskit.ignis.verification.randomized_benchmarking as rb
from qiskit import IBMQ

token = 'ae54a2937f60a5daeca95a84237ab43fbdc7b4c3e7a3fbe3a249f9c2e50e18a278f3c65340d50560403275052c5e51fa0f5d4558f94b769fef629801039196a3'
url = 'https://quantumexperience.ng.bluemix.net/qx/account/advanced'


IBMQ.save_account(token, overwrite=True)




n=6
ctrl=QuantumRegister(n,'ctrl')

anc=QuantumRegister(3,'anc')
tgt=QuantumRegister(2,'tgt')
c1=ClassicalRegister(n,'c1')

circuit=QuantumCircuit(ctrl,anc,tgt,c1)


circuit.h(ctrl)
circuit.x(tgt[1])
circuit.h(tgt[1])
#circuit.h(tgt)

for i in range(6):
#1st combination 000110

    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[2])
    circuit.x(ctrl[5])
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    circuit.mct(ctrl[2:5],anc[1],None,mode='noancilla')
    circuit.mct([ctrl[0],ctrl[1],ctrl[4],ctrl[5]],anc[2],None,mode='noancilla')
    
    circuit.mct(anc,tgt[0],None,mode='noancilla')
    
    circuit.mct([ctrl[0],ctrl[1],ctrl[4],ctrl[5]],anc[2],None,mode='noancilla')
    circuit.mct(ctrl[2:5],anc[1],None,mode='noancilla')
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    
    
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[2])
    circuit.x(ctrl[5])
    
    #2nd combination 001011
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[3])
    
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    circuit.mct([ctrl[0],ctrl[1],ctrl[4],ctrl[5]],anc[2],None,mode='noancilla')
    
    circuit.mct(anc,tgt[0],None,mode='noancilla')
    
    
    circuit.mct([ctrl[0],ctrl[1],ctrl[4],ctrl[5]],anc[2],None,mode='noancilla')
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    
    
    
    
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[3])
    #3rd combbination 011011
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[3])
    
    
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    circuit.mct(ctrl[2:5],anc[1],None,mode='noancilla')
    
    
    circuit.mct(anc,tgt[0],None,mode='noancilla')
    
    
    circuit.mct(ctrl[2:5],anc[1],None,mode='noancilla')
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    circuit.x(ctrl[0])
    circuit.x(ctrl[3])
    
    #4th combination 000111
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[2])
    
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    
    
    
    circuit.mct(anc,tgt[0],None,mode='noancilla')
    
    
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[2])
    
    
    
    circuit.cx(tgt[0],tgt[1])
    
    
    #Reverse latch
    #4th combination 000111
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[2])
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    
    
    
    circuit.mct(anc,tgt[0],None,mode='noancilla')
    
    
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[2])
    
    #3rd combbination 011011
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[3])
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    circuit.mct(ctrl[2:5],anc[1],None,mode='noancilla')
    
    
    circuit.mct(anc,tgt[0],None,mode='noancilla')
    
    
    circuit.mct(ctrl[2:5],anc[1],None,mode='noancilla')
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[3])
    #2nd combination 001011
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[3])
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    circuit.mct([ctrl[0],ctrl[1],ctrl[4],ctrl[5]],anc[2],None,mode='noancilla')
    
    circuit.mct(anc,tgt[0],None,mode='noancilla')
    
    
    circuit.mct([ctrl[0],ctrl[1],ctrl[4],ctrl[5]],anc[2],None,mode='noancilla')
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    
    
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[3])
    
    #1st combination 000110
    
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[2])
    circuit.x(ctrl[5])
    
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    circuit.mct(ctrl[2:5],anc[1],None,mode='noancilla')
    circuit.mct([ctrl[0],ctrl[1],ctrl[4],ctrl[5]],anc[2],None,mode='noancilla')
    
    circuit.mct(anc,tgt[0],None,mode='noancilla')
    
    circuit.mct([ctrl[0],ctrl[1],ctrl[4],ctrl[5]],anc[2],None,mode='noancilla')
    circuit.mct(ctrl[2:5],anc[1],None,mode='noancilla')
    circuit.mct(ctrl[0:3],anc[0],None,mode='noancilla')
    
    
    
    circuit.x(ctrl[0])
    circuit.x(ctrl[1])
    circuit.x(ctrl[2])
    circuit.x(ctrl[5])
    
    
    
   
    
    #amplification
    
    
    circuit.h(ctrl)
    circuit.x(ctrl)
    circuit.h(ctrl[5])
    
    
    circuit.mct(ctrl[0:4],ctrl[5],None,mode='noancilla')
    
    
    circuit.h(ctrl[5])
    circuit.x(ctrl)
    circuit.h(ctrl)

circuit.h(tgt[1])
circuit.x(tgt[1])
# Insert a barrier before measurement
circuit.barrier()
# Measure all of the qubits in the standard basis
for i in range(n):
    circuit.measure(ctrl[i], c1[i])
########################

###############################################################
# Set up the API and execute the program.
###############################################################


# First version: simulator
provider = IBMQ.load_account()
backend = provider.get_backend('ibmq_qasm_simulator')
my_provider = IBMQ.get_provider()
print(my_provider.backends())

job2=execute(circuit,backend,shots=8192)
result=job2.result()
count=result.get_counts()

print(count)
