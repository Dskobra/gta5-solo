loop = 0
timewaster = 1000000 # lower or increase to whatever works for you.
def timeout():
    global loop
    global timewaster
    convert_string = str(timewaster)
    # Previously preset 1000000. Now just change the timewaster variable
    print("Will count to " + convert_string + " to time out session")
    for counter in range(timewaster):
        print("Timing session out: ",counter)

while loop < 5:
    timeout()
    loop = loop + 1
    if loop == 1:
        break
    print("Resuming GTA Process")
