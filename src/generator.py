import sys

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(msg, g):
    g_length = len(g)
    tmp = msg[0 : g_length]
    temp_msg = msg + (g_length -1 )*'0'
    while g_length < len(temp_msg):
        if tmp[0] == '1':
            tmp = xor(g, tmp) + temp_msg[g_length]
        else:
            tmp = xor('0'*g_length, tmp) + temp_msg[g_length]
        g_length += 1
    if tmp[0] == '1':
        tmp = xor(g, tmp)
    else:
        tmp = xor('0'*g_length, tmp)
    return tmp

def generate(msg, g):
    crc = mod2div(msg, g)
    return msg+crc

if __name__ == "__main__":
    file_obj = open("input1.txt", "r")
    lines = file_obj.readlines()
    msg = lines[0].rstrip('\n')
    g = lines[1].rstrip('\n')
    packet = generate(msg, g)
    
    fh = open("input2.txt","w")
    fh.write(packet+ '\n')
    fh.write(g)
    fh.close()
