import sys
import os

curr_proj = os.path.basename(sys.prefix)
if curr_proj == 'usr':
    curr_proj = 'none'

print('Current project: ', curr_proj)
