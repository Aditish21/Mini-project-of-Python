import time
start=int(input("Enter a number to start the countdown: "))
while start>0:
    print(start)
    time.sleep(1)
    start-=1
print("Countdown Complete\n Happy birthday!")