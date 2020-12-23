from __future__ import print_function
import numpy as np
import sys
import struct
import time

sys.path.append('/home/xilinx')
from pynq import Overlay

if __name__ == "main":
    print('Entry:', sys.argv[0])
    print('System argument(s):', len(sys.argv))

    print('Start of \"' + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFiles/wang_dct_axi_master.bit")
    regIP = ol.top_fdct_0

    inBuffer0  = np.allocate(shape=(32,), dtype=np.int32)
    outBuffer0  = np.allocate(shape=(32,), dtype=np.int32)

    for i in range(32):
        inBuffer0[i] = (input_block[i*2+1]*(2**16) + input_block[i+2])
    regIP.write(0x10, inBuffer0.device_address)
    regIP.write(0x18, outBuffer0.device_address)

    timeKernelStart = time()
    regIP.write(0x00, 0x01)
    while(regIP.read(0x00)&0x04) == 0x00:
        continue
    print("===========================")
    timeKernelEnd = time()

    print("Kernel execution time: "+str(timeKernelEnd - timeKernelStart)+" s")

    output = np.zeros(64)
    for i in range(32):
        output_block = outBuffer0[i]
        num2 = output_block // (2**16)
        num1 = output_block - num2*(2**16)
        if(num1>2**15):
            num1 -= 2**16
        if(num2>2**15):
            num2 -= 2**16
        output[2*i] = num1
        output[2*i+1] = num2
    print("Exit process")
