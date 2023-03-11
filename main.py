import time

def countdown():
    mins = int(input("Enter minutes: "))
    secs = int(input("Enter seconds: "))
    rounds = int(input("Enter number of rounds: "))
    
    for r in range(rounds):
        for t in range(mins * 60 + secs, 0, -1):
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Round:", r+1, "Timer:", timer, end="\r")
            time.sleep(1)
            
        print("Round:", r+1, "completed!")
        
    print("All rounds completed!")
    
countdown()
