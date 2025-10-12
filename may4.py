import time 
import datetime 





while True:
    time.sleep(1)
    test2 = datetime.datetime.now()
    if test2.second<10:
        print(f"{test2.hour}:{test2.minute}:0{test2.second}")
    else:
         print(f"{test2.hour}:{test2.minute}:c{test2.second}")
         