import generator, sys

def verify(packet, g):
    reminder = generator.mod2div(packet, g)
    return True if not int(reminder) else False

if __name__ == "__main__":
	file_obj = open("input2.txt", "r")
	lines = file_obj.readlines()
	packet = lines[0].rstrip('\n')
	g = lines[1].rstrip('\n')
	verification = verify(packet, g)

	fh = open("output.txt","w")
	if(verification):
		fh.write('message is correct')
	else:
		fh.write('message is wrong') 
