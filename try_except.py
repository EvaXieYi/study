from sys import exit
from time import sleep
try:  
    index=0
    indexname=True
    while True:
        print('  '*index,end='')
        print('*******')
        sleep(0.1)
        if indexname:
            index=index+1
            if index==20:
                indexname=False
        else:
            index=index-1
            if index==0:
                indexname=True
except KeyboardInterrupt as abc:
    exit(),abc.
    
    