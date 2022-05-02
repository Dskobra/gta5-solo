loop = 0
def timeout():
    global loop
    print("Will count to 1000000 to time out session")
    for counter in range(1000000):
        print("Timing session out: ",counter)

while loop < 5:
    timeout()
    loop = loop + 1
    if loop == 1:
        break
    print("Resuming GTA Process")
