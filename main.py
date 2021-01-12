import random
import time
def dice(x):
        time.sleep(0.5)
        n=random.randint(1,6)
        if n==1:
            print("[      ]")
            print("[   0  ]")
            print("[      ]")
        elif n==2:
            print("[      ]")
            print("[  0 0 ]")
            print("[      ]")
        elif n==3:
            print("[   0   ]")
            print("[   0   ]")
            print("[   0   ]")
        elif n==4:
            print("[  0 0   ]")
            print("[  0 0   ]")
            print("[        ]")
        elif n==5:
            print("[  0 0   ]")
            print("[  0 0   ]")
            print("[  0     ]")
        elif n==6:
            print("[  0 0    ]")
            print("[  0 0    ]")
            print("[  0 0    ]")
if __name__== '__main__':
    print("enter your name")
    s=input().split()
    time.sleep(2)
    print("TYPE Yes or No for dice ")
    x=input()
    if x=="Yes":
        dice(x)


