# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:30:02 2021

@author: hp
"""
from qiskit.test.mock import FakeMelbourne
device_backend = FakeMelbourne()

from qiskit import QuantumRegister,ClassicalRegister,QuantumCircuit,execute,BasicAer,IBMQ
from qiskit.tools.visualization import plot_histogram
from qiskit.providers.ibmq import least_busy
import matplotlib.pyplot as plt
import math
from qiskit import *
from qiskit.providers.aer import noise
from qiskit.providers.aer.noise import NoiseModel, errors
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


ints = [1, 2, 3, 4, 5, 6]

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

my_provider = IBMQ.get_provider()

properties = device_backend.properties()
coupling_map = device_backend.configuration().coupling_map


noise_model = NoiseModel.from_backend(device_backend)
basis_gates = noise_model.basis_gates

backend = my_provider.get_backend(name='ibmq_qasm_simulator')
sim=execute(circuit,backend=backend,shots=8192)
result = sim.result()
final = result.get_counts()
noisy_sim = execute(circuit, backend=backend, shots=8192,
coupling_map=coupling_map,
noise_model=noise_model,
basis_gates=basis_gates)
noisy_result = noisy_sim.result()
noisy_final = noisy_result.get_counts(circuit)


count=result.get_counts()
data1=result.data()
print(result.get_counts(circuit))

print(circuit.count_ops())
print((circuit.decompose()).count_ops())
print(circuit.decompose().size())
print(circuit.decompose().depth())
print((circuit.decompose()).decompose().count_ops())
print((circuit.decompose()).decompose().size())
print((circuit.decompose()).decompose().depth())
#print(circuit.clifford_2_1())