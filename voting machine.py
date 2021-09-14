#Python voting machine program
from tabulate import tabulate
partydata=[["S.No","Party Name","Candidate Name"],[1,"DMK","D.Arul nidhi"],[2,"AIADMK","G.Ramar"],[3,"DMDK","A.k.Mani"],[4,"PMK","D.Deena"],[5,"NTK","A.Karpagam"],[6,"VCK","A.Sundar"],[7,"TMC","L.Meenachi"],[8,"BJP","G.Rajeshwari"],[9,"MNM","R.Manimegalai"],[10,"AMMK","G.Hariharan"]]

from pyzbar.pyzbar import decode
from PIL import Image
d=decode(Image.open('C:/Users/RSSS/Downloads/TRQ0837429.png'))
code_no=d[0]. data.decode("ascii")
#print(code_no)


#current time
import time
t = time.localtime()
Time = time.strftime("%H:%M:%S", t)
#print(Time)


#current date
from datetime import date
today = date.today()
# dd/mm/YY
Date = today.strftime("%d/%m/%Y")
#print(Date)

#completed sensor beep sound
import playsound
song="C:/Users/RSSS/Desktop/sensor beep.mp3"
# playsound.playsound(song)


import pandas as pd
data=pd.read_csv("C:/Users/RSSS/Desktop/Voter_list.csv")
voter_list=list(data.iloc[:,0])


if (code_no in voter_list):
    print(tabulate(partydata, headers='firstrow', tablefmt='fancy_grid'))
    
    import time
    time.sleep(15)
    print("Enter your vote")
    vote=int(input("Enter Party's No. : "))
    
    if (vote<=10):
        from csv import DictWriter
        field_names = ['Date','Time','Voter ID','Party']
        dictionary={'Date':Date,'Time':Time,'Voter ID':code_no,'Party':vote}
        with open('C:/Users/RSSS/Desktop/Vote list.csv', 'a') as f_object:
            twriter_object = DictWriter(f_object, fieldnames=field_names)
            twriter_object.writerow(dictionary)
        f_object.close()
        
        print("Your vote successfully saved!")
        playsound.playsound(song)
    
    else:
        print("Enter correct Party's Number")
else:
    print("Invalid QR-code")
        

    
    
    

