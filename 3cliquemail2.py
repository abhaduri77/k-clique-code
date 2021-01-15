
from qiskit import QuantumRegister,ClassicalRegister,QuantumCircuit,execute,BasicAer,IBMQ
from qiskit.tools.visualization import matplotlib_circuit_drawer as circuit_drawer
from qiskit.tools.visualization import plot_histogram
from qiskit.providers.ibmq import least_busy
import matplotlib.pyplot as plt
from qiskit import compile
import math

pi=math.pi
from qiskit import IBMQ
IBMQ.stored_accounts()
token = 'ae54a2937f60a5daeca95a84237ab43fbdc7b4c3e7a3fbe3a249f9c2e50e18a278f3c65340d50560403275052c5e51fa0f5d4558f94b769fef629801039196a3'
url = 'https://quantumexperience.ng.bluemix.net/qx/account/advanced'
IBMQ.enable_account(token)

IBMQ.save_account(token, overwrite=True)


IBMQ.load_accounts()
print(IBMQ.backends())


n=6
ctrl=QuantumRegister(n,'ctrl')

anc=QuantumRegister(9,'anc')
tgt=QuantumRegister(7,'tgt')
c1=ClassicalRegister(n,'c1')

circuit=QuantumCircuit(ctrl,anc,tgt,c1)


circuit.h(ctrl)
circuit.x(tgt[6])
circuit.h(tgt[6])
#circuit.h(tgt)
circuit.x(ctrl[0])
circuit.x(ctrl[3])
circuit.x(ctrl[4])
circuit.x(ctrl[5])

#1st combination 000110


circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffoli
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])

circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])


circuit.ccx(tgt[0],tgt[1],tgt[3])
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.cx(tgt[4],tgt[5])#4th toffoli
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.ccx(tgt[0],tgt[1],tgt[3])



circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])

circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffoli
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])

circuit.x(ctrl[0])
circuit.x(ctrl[3])
circuit.x(ctrl[4])
circuit.x(ctrl[5])

#2nd combination 001011
circuit.x(ctrl[2])
circuit.x(ctrl[4])
circuit.x(ctrl[5])


circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])



circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffoli
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])




circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])

circuit.ccx(tgt[0],tgt[1],tgt[3])
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.cx(tgt[4],tgt[5])#4th toffoli
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.ccx(tgt[0],tgt[1],tgt[3])

#3rd toffoli
circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])

circuit.cx(anc[8],tgt[2])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])

circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffoli
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])

circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])


circuit.x(ctrl[2])
circuit.x(ctrl[4])
circuit.x(ctrl[5])
#3rd combbination 011011

circuit.x(ctrl[2])
circuit.x(ctrl[5])

circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])

circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffol
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])



circuit.ccx(tgt[0],tgt[1],tgt[3])
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.cx(tgt[4],tgt[5])#4th toffoli
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.ccx(tgt[0],tgt[1],tgt[3])




circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffol
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])

circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])


circuit.x(ctrl[2])
circuit.x(ctrl[5])

#4th combination 000111
circuit.x(ctrl[3])
circuit.x(ctrl[4])
circuit.x(ctrl[5])

circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])

circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffol
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])


circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])


circuit.ccx(tgt[0],tgt[1],tgt[3])
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.cx(tgt[4],tgt[5])#4th toffoli
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.ccx(tgt[0],tgt[1],tgt[3])

circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])


circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffol
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])


circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])


circuit.x(ctrl[3])
circuit.x(ctrl[4])
circuit.x(ctrl[5])



circuit.cx(tgt[5],tgt[6])


#Reverse latch
#4th combination 000111
circuit.x(ctrl[3])
circuit.x(ctrl[4])
circuit.x(ctrl[5])

circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])

circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffol
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])


circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])


circuit.ccx(tgt[0],tgt[1],tgt[3])
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.cx(tgt[4],tgt[5])#4th toffoli
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.ccx(tgt[0],tgt[1],tgt[3])

circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])


circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffol
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])


circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])


circuit.x(ctrl[3])
circuit.x(ctrl[4])
circuit.x(ctrl[5])
#3rd combbination 011011

circuit.x(ctrl[2])
circuit.x(ctrl[5])

circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])

circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffol
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])



circuit.ccx(tgt[0],tgt[1],tgt[3])
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.cx(tgt[4],tgt[5])#4th toffoli
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.ccx(tgt[0],tgt[1],tgt[3])




circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffol
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])

circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])


circuit.x(ctrl[2])
circuit.x(ctrl[5])
#2nd combination 001011
circuit.x(ctrl[2])
circuit.x(ctrl[4])
circuit.x(ctrl[5])


circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])



circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffoli
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])




circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])

circuit.ccx(tgt[0],tgt[1],tgt[3])
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.cx(tgt[4],tgt[5])#4th toffoli
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.ccx(tgt[0],tgt[1],tgt[3])

#3rd toffoli
circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])

circuit.cx(anc[8],tgt[2])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])

circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffoli
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])

circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.cx(anc[2],tgt[0])#1st toffoli
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])


circuit.x(ctrl[2])
circuit.x(ctrl[4])
circuit.x(ctrl[5])
circuit.x(ctrl[0])
circuit.x(ctrl[3])
circuit.x(ctrl[4])
circuit.x(ctrl[5])

#1st combination 000110


circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffoli
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])

circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])


circuit.ccx(tgt[0],tgt[1],tgt[3])
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.cx(tgt[4],tgt[5])#4th toffoli
circuit.ccx(tgt[2],tgt[3],tgt[4])
circuit.ccx(tgt[0],tgt[1],tgt[3])



circuit.ccx(ctrl[0],ctrl[1],anc[6])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.cx(anc[8],tgt[2])#3rd toffoli
circuit.ccx(ctrl[5],anc[7],anc[8])
circuit.ccx(ctrl[4],anc[6],anc[7])
circuit.ccx(ctrl[0],ctrl[1],anc[6])

circuit.ccx(ctrl[2],ctrl[3],anc[3])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.cx(anc[5],tgt[1])#2nd toffoli
circuit.ccx(ctrl[5],anc[4],anc[5])
circuit.ccx(ctrl[4],anc[3],anc[4])
circuit.ccx(ctrl[2],ctrl[3],anc[3])

circuit.x(ctrl[0])
circuit.x(ctrl[3])
circuit.x(ctrl[4])
circuit.x(ctrl[5])


print(tgt[6])
print(IBMQ.stored_accounts())
#phase flip gate
#circuit.cz(ctrl,ctrl[5])
#circuit.z(ctrl)

#amplification


circuit.h(ctrl)
circuit.x(ctrl)
circuit.h(ctrl[5])
#circuit.cu1(pi/4, ctrl[0], ctrl[3])
#circuit.cx(ctrl[0], ctrl[1])
#circuit.cu1(-pi/4, ctrl[1], ctrl[3])
#circuit.cx(ctrl[0], ctrl[1])
#circuit.cu1(pi/4, ctrl[1], ctrl[3])
#circuit.cx(ctrl[1], ctrl[2])
#circuit.cu1(-pi/4, ctrl[2], ctrl[3])

#circuit.cx(ctrl[1], ctrl[2])
#circuit.cu1(-pi/4, ctrl[2], ctrl[3])
#circuit.cx(ctrl[0],ctrl[2])
#circuit.cu1(-pi/4,ctrl[2],ctrl[3])

circuit.ccx(ctrl[0],ctrl[1],anc[0])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[4],anc[2],anc[3])

circuit.cx(anc[3],ctrl[5])
circuit.ccx(ctrl[4],anc[2],anc[3])
circuit.ccx(ctrl[3],anc[1],anc[2])
circuit.ccx(ctrl[2],anc[0],anc[1])
circuit.ccx(ctrl[0],ctrl[1],anc[0])

#circuit.ccx(ctrl[3],ctrl[4],ctrl[5])
circuit.h(ctrl[5])
circuit.x(ctrl)
circuit.h(ctrl)

circuit.h(tgt[6])
circuit.x(tgt[6])
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
backend=IBMQ.get_backend(name='ibmq_qasm_simulator')

qobj = compile(circuit, backend=backend, shots=8192)
job = backend.run(qobj)
result=job.result()
print(job.status())
count=result.get_counts()
data1=result.data()
print(result.get_counts(circuit))
#plot_histogram(count,figsize=(90,50)).savefig('C:\size3op.png')

result_freqs = {'000000':0, '000001':0, '000010':0, '000011':0, '000100':0,'000101':0,'000110':0,'000111':0,'001000':0,'001001':0,'001010':0,'001011':0,'001100':0,'001101':0,'001110':0,'001111':0,'010000':0,'010001':0,'010010':0,'010011':0,'010100':0,'010101':0,
                '010110':0,'010111':0,'011000':0,'011001':0,'011010':0,'011011':0,'011100':0,'011101':0,'011110':0,'011111':0,'100000':0,'100001':0,'100010':0,'100011':0,'100100':0,'100011':0,'100100':0,'100101':0,'100110':0,'100111':0,'101000':0,'101001':0,'101010':0,
                '101011':0,'101100':0,'101101':0,'101110':0,'101111':0,'110000':0,'110001':0,'110010':0,'110011':0,'110100':0,'110101':0,'110110':0,'110111':0,'111000':0,'111001':0,'111010':0,'111011':0,'111100':0,'111101':0,'111110':0,'111111':0
                }
for key in count.keys():
    freq_key = key[0:6]
    result_freqs[freq_key] = result_freqs[freq_key] +count[key] 
          
D = result_freqs
plt.figure(figsize=(80,50))
plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))
# QASM from a program

QASM_source = Q_program.get_qasm("Circuit")

print(QASM_source)
#plt.savefig('c:\op112.png')
print(circuit)
