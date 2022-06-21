#!/usr/bin/env python3

# read file
msg = open("message.txt").read()

# initiate flag list and loop thru the file contents, step by 3 (challenge hinted at groups of 3.
# you can also see by looking that is the case)
flag = []
for i in range(0, len(msg), 3):
	# grab a chunk which is current position plus 3
	chunk = msg[i:i+3]

	# re-assemble chunk to be the 3rd item plus 1st and 2nd
	# then append it to the flag list
	flag.append(chunk[-1:] + chunk[0:2])

# join flag list (currently in chucks of 3) to a string,
#   split at spaces and grab last item
flag = "".join(flag).split()[-1]
print(flag)
