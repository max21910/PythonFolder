import os 
#library for making the folder
import time 
# add delay with time.sleep()

choice = input("Select 1 for Create a folder \n Select 2 for github link  \n")
choice = int(choice) 
 #chose what to do 
# initialise choice 

if choice == 1: 
# if the choice is 1 then :

 print("Created with ❤️ in 🇫🇷 by Max21910")
 
 time.sleep(1) 
 #delay of 1 sec
 
 Name = 'Hello word' 
  #name of the folder
 Path = '/Users/maxime/Desktop' 
 #path of the folder
 make = os.path.join(Path, Name) 
 #join the 2 path and Name
 os.mkdir(make) 
 #make the folder with the name and the path
 
 print("created folder succefully")
  # say that the folder is create
 
if choice == 2: 
#if the choice is 2 then : 
 print("https://github.com/Max21910") 
 # show my github link 
 
if choice >= 3:
 #if the user select a random choice wish is not on the "scipt"
 print("Please select a correct option")
 #created with love by max21910