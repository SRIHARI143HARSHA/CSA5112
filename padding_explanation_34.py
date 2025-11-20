def pad_bits(bitstr, block=64):
    bitstr += '1'
    bitstr += '0' * ((-len(bitstr)) % block)
    return bitstr

def unpad_bits(bitstr):
    bitstr = bitstr.rstrip('0')      # remove trailing zeros
    i = bitstr.rfind('1')           # find the padding 1
    return bitstr[:i]               # original bits

# example
m = "1011001"
p = pad_bits(m, 8)
u = unpad_bits(p)
print(m, p, u)


output:
1011001 10110011 1011001

=== Code Execution Successful ===
