import sys

def alter(packet, i):
    p = list(packet)
    if p[i] == '0':
        p[i] = '1' 
    else:
        p[i] = '0'
    return ''.join(p)

if __name__ == "__main__":
	file_obj = open("alter_input.txt", "r")
	lines = file_obj.readlines()
	packet = lines[0].rstrip('\n')
	index = int(lines[1].rstrip('\n'))
	altered_packet= alter(packet, index)

	fh = open("alter_output.txt","w")
	fh.write(altered_packet)
   


	
		
		
		