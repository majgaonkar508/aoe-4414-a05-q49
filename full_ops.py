# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
# Script to determine the output shape and operation count of a 
# fully-connected layer. 
# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors
# Output (all int):
#  c_out: output channel count
#  h_out: output height count
#  w_out: output width count
#  adds: number of additions performed
#  muls: number of multiplications performed
#  divs: number of divisions performed
# Written by Mandar Ajgaonkar
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import sys # argv

# initialize script arguments
c_in = float('nan')   
n_wv = float('nan')   

# parse script arguments
if len(sys.argv) == 3:
  c_in = float(sys.argv[1])
  n_wv = float(sys.argv[2])
  ...
else:
  print(\
   'Usage: '\
   'python3 full_ops.py c_in n_wv'\
  )
  exit()

# determine output channel count, height and width of output map
c_out = n_wv
h_out = 1
w_out = 1

# calculate number of additions, multiplications, and divisions
adds = n_wv*c_in
muls = n_wv*c_in
divs = 0 # no divisions required

# print results
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed