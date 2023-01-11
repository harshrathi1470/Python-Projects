# #Apni Dictionary
# print("from the following words type the one you want meaning of:")
# dictionary={"Abstract":"Actual instances", 
# "Abstruse":"Hard to understand",
# "Arduous":"Difficult",
# "Augean":"Difficult and Unpleasant"}
# print("""Abstract
# Abtruse
# Arduous
# Augean""") #or use 'here'
# word=str.capitalize(str(input("are you ready:")))
# print(word,"=",dictionary[word])


#Faulty Calculator
# first_number=int(input("enter first number:"))
# second_number=int(input("enter second number:"))
# print("enter the operation you want to carry out from the listed one:\n+[sum]\n-[substraction]\n*[multiply]\n/[float divison]\n//[int divison]")
# operation=str(input("lets go:"))
# if operation=="+":
#     if (first_number==56 or first_number==9)and(second_number==9 or second_number==56):
#      print("addition of numbers = 77")
#     else:
#      print("addition of numbers =",first_number+second_number)                 
# elif operation=="-":
#     if (first_number==56 and second_number==9):
#      print("substraction of numbers = 48") 
#     else:
#      print("substraction of numbers =",first_number-second_number)
# elif operation=="*":
#     if (first_number==45 or first_number==3)and(second_number==3 or second_number==45):
#      print("multiplication of numbers = 556") 
#     else:
#      print("multiplication of numbers =",first_number*second_number)
# elif operation=="/":
#     if first_number==13 and second_number==3:
#      print("float division of numbers = 4.12") 
#     else:
#      print("float division of numbers =",first_number/second_number)
# elif operation=="//":
#     if first_number==56 and second_number==6:
#      print("integer division of numbers = 4") 
#     else:
#      print("integer divison of numbers =",first_number//second_number)
# else:
#     print("Error! Please check your input")



# #Guess the no.{18 out of 1-100}
# a=int(input("You have 9 chances to guess my no. between [1-100] let's go! guess my no:"))
# if a>50 and a<100:
#     print("my no. is far lesser than this")
#     print("8 guesses left\n\n")
# elif a<50 and a>30:
#     print("my no. is quite lesser than this")
#     print("8 guesses left\n\n")
# elif a<10 and a>1:
#     print("good guess my no. is little bigger than this")
#     print("8 guesses left\n\n")
# elif a<30 and a>20:
#     print("good guess my no. is near to it and less than this")
#     print("8 guesses left\n\n")
# elif a<16 and a>10:
#     print("a bold guess but my no. is still few digits greater")
#     print("8 guesses left\n\n")
# elif a==17:
#     print("A very close guess but my no. is a bit less than this")
#     print("8 guesses left\n\n")
# elif a==16:
#     print("A very close guess but my no. is still very few digits big")
#     print("8 guesses left\n\n")
# elif a==19:
#     print("A very close guess but my no. is a bit high than this")
#     print("8 guesses left\n\n")
# no_of_guesses=8
# if a!=18:
#  while (no_of_guesses>0):
#      a=int(input("You still have chance to win guess my no. again:"))
#      if a==18:
#          print("ohhhh! (:==> you did it <==:) congratulations")
#          break
#      else:
#         if a>=50 and a<=100:
#              print("my no. is far lesser than this")
#              no_of_guesses-=1
#              print(no_of_guesses,"guesses left\n\n")
#              continue
#         elif a<50 and a>=30:
#              print("my no. is quite lesser than this")
#              no_of_guesses-=1
#              print(no_of_guesses,"guesses left\n\n")
#              continue
#         elif a<10 and a>=1:
#              print("good guess my no. is little bigger than this")
#              no_of_guesses-=1
#              print(no_of_guesses,"guesses left\n\n")
#              continue
#         elif a<30 and a>=20:
#              print("good guess my no. is near to it and less than this")
#              no_of_guesses-=1
#              print(no_of_guesses,"guesses left\n\n")
#              continue    
#         elif a<16 and a>=10:
#              print("a bold guess but my no. is still few digits greater")
#              no_of_guesses-=1
#              print(no_of_guesses,"guesses left\n\n")
#              continue
#         elif a==17:
#              print("A very close guess but my no. is a bit less than this")
#              no_of_guesses-=1
#              print(no_of_guesses,"guesses left\n\n")
#              continue
#         elif a==16:
#              print("A very close guess but my no. is still very few digits big")
#              no_of_guesses-=1
#              print(no_of_guesses,"guesses left\n\n")
#              continue
#         elif a==19:
#              print("A very close guess but my no. is a bit high than this")
#              no_of_guesses-=1
#              print(no_of_guesses,"guesses left\n\n")
#              continue
#         else:
#             print("game over buddy try later")
# else:
#     print("ohhhh! (:==> you did it <==:) congratulations")


# #Short answer
# n=18

# number_of_guesses=1

# print("Number of guesses is limited to only 9 times: ")

# while (number_of_guesses<=9):

#     guess_number = int(input("Guess the number :\n"))

#     if guess_number<18:

#         print("you enter less number please input greater number.\n")

#     elif guess_number>18:

#         print("you enter greater number please input smaller number.\n ")

#     else:

#         print("you won\n")

#         print(number_of_guesses,"no.of guesses he took to finish.")

#         break

#     print(9-number_of_guesses,"no. of guesses left")

#     number_of_guesses = number_of_guesses + 1



# if(number_of_guesses>9):

#     print("Game Over")




# #Astrologer's stars
# n=int(input("enter a no:"))
# bool_var=int(input("enter 1 or 0 as you boolean input:"))
# if str(bool(bool_var))=="True":
#     x=0
#     for i in range(0,n+1):
#         print("*"*x)
#         x+=1
# else:
#     x=n
#     for j in range(0,n+1):
#         print("*"*x)
#         x-=1
     




# #Health Managment System
# def getdate():
#     import datetime
#     return datetime.datetime.now()
# clients=["Harry","Carry","Bappi lehri"]
# print("Your current clients:",clients)
# n=0
# q=1
# c=1
# while 1:
#     if(c%3==0):
#         c/=3
#         print("Your current clients:",clients)
#     if (q%3)!=0:
#         client_name1=str(input("\nEnter the name of client of which you want to log or retrieve: "))
#         client_name=client_name1.capitalize()
#     else:
#         q/=3
#         client_name2=str(input("\nKoi Baat Ni! dubara daal bande ka naam: ")) 
#         client_name=client_name2.capitalize()  
#     if 1:
#         for item in clients:
#             if (item==client_name):
#                 n=2
#                 break
#             else:
#                 n=0                 
#     if n==2:
#         x=client_name.capitalize()
#         log_retrieve=str(input("\nPress 1 for log | 2 for retrieve: "))
#         if log_retrieve=="1":
#             F_E_L=str(input("Press 1 for food | 2 for exercise: "))
#             if F_E_L=="1":
#                 with open("%s_food.txt"%x,"a") as f: 
#                  for i in range(1,15):
#                     text1=str(input("\nenter what you ate: "))
#                     text=text1.capitalize()
#                     f.write("%s"%str(i)+".  Date and time:"+"["+str(getdate())+"]"+" \t"+text+"\n")
#                     t=str(input("To add what else you ate press 1 | else anything to continue: "))
#                     if t!="1":
#                         break                              
#                 wish=str(input("\nTo continue retrieve or log for other clients press 1 | else anything to exit: "))
#                 if wish=="1":
#                    continue
#                 else:
#                    break     
#             elif F_E_L=="2":
#                 with open("%s_exercise.txt"%x,"a") as f: 
#                   for i in range(1,15):
#                     text1=str(input("\nenter exercise you did: "))
#                     text=text1.capitalize()                    
#                     f.write("%s"%str(i)+".  Date and time:"+"["+str(getdate())+"]"+" \t"+text+"\n")
#                     t=str(input("To add another exercise you did press 1 | else anything to continue: "))
#                     if t!="1":
#                         break
#                 wish=str(input("\nTo continue retrieve or log for other clients press 1 | else anything to exit: "))
#                 if wish=="1":
#                    continue
#                 else:
#                    break
#             else:
#                 print("\n\n\nYou entered a string buddy start again")
#                 c*=3
#                 continue                                      
#         elif log_retrieve=="2":
#             F_E_R=str(input("Press 1 for food | 2 for exercise: "))
#             if F_E_R=="1":            
#                 with open("%s_food.txt"%x) as f: 
#                     r=str(f.read())
#                     print("\n")
#                     print(r)
#                 wish=str(input("\nTo continue retrieve or log for other clients press 1 | else anything to exit: "))
#                 if wish=="1":            
#                    continue
#                 else:
#                    break  
#             elif F_E_R=="2":
#                 with open("%s_exercise.txt"%x) as f: 
#                     r=str(f.read())
#                     print("\n")
#                     print(r)
#                 wish=str(input("\nTo continue retrieve or log for other clients press 1 | else anything to exit: "))
#                 if wish=="1":            
#                    continue
#                 else:
#                    break     
#             else:
#                 print("\n\n\nYou entered a string buddy start again")
#                 c*=3
#                 continue                              
#         else:
#             print("\n\n\nYou entered a string buddy start again")
#             c*=3
#             continue             
#     else:
#         add=str(input("\nPress 1 to add new client | 2 for typing name correctly again: "))
#         if (add=="1"):
#          #    name=(str(input("Enter your new client name: ")))
#          #    z=name.capitalize()
#             clients.append(client_name)
#             print("Your current clients:",clients)
#             continue
#         elif(add=="2"):
#             q*=3
#             continue     
#         else:
#             print("\n\n\nYou entered a string buddy start again")
#             c*=3
#             continue  


# # my issue solution
# f=open("ab.txt","a+")
# f.write("thank you\n")
# f.seek(0)
# print(f.read())
# f.close()






# #Game Development: Stone,Paper,Scissor
# ch={"Stone":"S","Paper":"P","Scissor":"C"}
# print("There will be 10 matches in a series\nAnd this is how you will take your chance:")
# for choice,shortcut in ch.items():
#     print("Press",shortcut,"for",choice)
# N=(str(input("Enter your name: "))).capitalize()
# while 1:
#         start=str(input("Press 'Enter' to start the series\t"))
#         if start=="":
#             break
#         else:
#             continue
# print("\n\nLets go!\n")
# while 1:
#     i=10
#     x=y=0
#     while i>0:
#         if i<4:
#             print(f"\nMatches left : {i}")
#         import random        
#         a=random.choice(list(ch.values()))
#         b1=str(input("Your chance: "))
#         b=b1.capitalize()
#         if b=="Harry bhai":
#             x=100
#             break
#         elif a=="S" and b=="S" or a=="P" and b=="P" or a=="C" and b=="C":
#             print(f"Draw! Play match no. {11-i} again\n")
#             continue
#         elif a=="S" and b=="P":
#             print(f"You win! match no. {11-i}\n")
#             x+=1
#         elif a=="S" and b=="C":
#             print(f"You lose! match no. {11-i}\n")
#             y+=1
#         elif a=="P" and b=="S":
#             print(f"You lose! match no. {11-i}\n")
#             y+=1
#         elif a=="P" and b=="C":
#             print(f"You win! match no. {11-i}\n")
#             x+=1
#         elif a=="C" and b=="S":
#             print(f"You win! match no. {11-i}\n")
#             x+=1
#         elif a=="C" and b=="P":
#             print(f"You lose! match no. {11-i}\n")
#             y+=1
#         else:
#             print(f"Try again wrong input, You typed: {b1}\n")
#             continue
#         if x>5 or y>5:
#             break
#         if x==5 and y==5:
#             break
#         i-=1
#     if x>5:
#         z=str(input(f"\n\n{N} won the series by {x-y} points.\nPress 1 to compete again | 'enter' to exit: "))
#         if z=="1":
#             continue
#         else:
#             break
#     elif y>5:
#         z=str(input(f"\n\nComputer won series luckily by {y-x} points.\nPress 1 to compete again | 'enter' to exit: "))
#         if z=="1":
#             continue
#         else:
#             break
#     else:
#         z=str(input("\n\nThis was a draw play series again.\nPress 1 to play again | 'enter' to exit: "))
#         if z=="1":
#             continue
#         else:
#             break







# # HEALTHY PROGRAMMER
# import time
# from time import localtime,strftime
# from pygame import mixer


# def stamp():
#     T=["water.mp3","eyes.mp3","physical.mp3"]
#     I=[0,1,2]
#     try:
#         for i in I:
#                 with open(f"{T[i][0:-4]}.txt","a+") as f:        
#                     f.write("\n\n\n\n"+strftime("%a, %d %b %Y",localtime())+"\n")
#     except Exception as e:
#         print(e)

# def play_song(i,y):
#     T=["water.mp3","eyes.mp3","physical.mp3"]
#     J=['drank','eydone','exdone']
#     mixer.init()
#     mixer.music.load(T[i])
#     mixer.music.set_volume(0.7)
#     mixer.music.play(loops=0,start=25.23,fade_ms=0)
#     if y=='12:58:00':
#         t_end=time.time()+115
#         while time.time()<t_end:
#             mixer.music.fadeout(110000)
#             query=input(f"Type {J[i]} to exit the program:\t")
#             if query == J[i]:
#                 with open(f"{T[i][0:-4]}.txt","a+") as f:        
#                     f.write("Time\t"+strftime("%H:%M:%S",localtime())+" \t"+J[i].capitalize()+"\n")
#                 mixer.music.stop()
#                 break
#             else:
#                 continue 
#     else:        
#         try:
#             t_end=time.time()+300
#             while time.time()<t_end:
#                 query=input(f"Type {J[i]} to exit the program:\t")
#                 if query == J[i]:
#                     with open(f"{T[i][0:-4]}.txt","a+") as f:        
#                         f.write("Time\t"+strftime("%H:%M:%S",localtime())+" \t"+J[i].capitalize()+"\n")
#                     mixer.music.stop()
#                     break
#                 else:
#                     continue
#         except Exception as e:
#             print(e)
    
# def get_lists():
#     W=[15,17,11]
#     X=[14640,14400,15480]
#     Y=[2040,1800,2880]
#     t=0
#     Z=[]
#     while(t<3):
#         Z.append(t)
#         t+=1
#     global tc
#     tc=[[]for _ in range(t)]
#     for z in Z:
#         fromepochsec=0
#         n=0
#         for times in range(1,W[z]):
#             if times==1:
#                 fromepochsec=fromepochsec+n+X[z]
#                 s=strftime("%H:%M:%S",localtime(fromepochsec))
#                 n=Y[z]     
#             else:
#                 fromepochsec=fromepochsec+n
#                 s=strftime("%H:%M:%S",localtime(fromepochsec))
#             tc[z].append(s)
#     global tcs
#     tcs=[]
#     for i in Z:
#         for t in tc[i]:
#             tcs.append(t)
#     tcs.sort()



# get_lists()
# while 1:
#     y=strftime("%H:%M:%S",localtime())
#     if '17:15:00'==y:
#         time.sleep(56900)
#     elif '09:00:00'==y:
#         stamp()
#         time.sleep(70)
#     elif '13:00:00'==y or '17:00:00'==y:
#         print("Your physical and eye exercise is at the same time do both simultaneously")
#         i=2
#         play_song(i)      
#     elif y in tcs:
#         if y in tc[0]:
#             i=0
#             play_song(i,y)
#         elif y in tc[1]:
#             i=1
#             play_song(i,y)
#         elif y in tc[2]:
#             i=2
#             play_song(i,y)





# # OBJECT ORIENTED MINI PROJECT - LIBRARY MANAGEMENT SYSTEM
# class library: 
#     __Ultimate_dict={}


#     def __init__(self,arg_list_of_books,arg_lib_name):
#         for item in arg_list_of_books:
#             self.__Ultimate_dict[item]={"Name":None,"Class":None,"Roll_no.":None,"Days":None,"Date_time":None}
#         self.__list_of_books=arg_list_of_books
#         self.__lib_name=arg_lib_name
    
#     def display_books(self):
#         self.__list_of_books.sort()
#         for i in range (1,len(self.__list_of_books)+1):
#                 print(f"{i}. {self.__list_of_books[i-1]}")

#     def lend_book(self,bookname):
#         try:
#             if bookname in self.__list_of_books:
#                 if self.__Ultimate_dict[bookname]["Name"]==None and self.__Ultimate_dict[bookname]["Class"]==None and self.__Ultimate_dict[bookname]["Roll_no."]==None and self.__Ultimate_dict[bookname]["Days"]==None and self.__Ultimate_dict[bookname]["Date_time"]==None:    
#                     print("\n"+bookname+" is there in "+self.__lib_name+" collection!")
#                     self.__Ultimate_dict[bookname]["Name"]=(input("Enter Full Name: ")).title()
#                     self.__Ultimate_dict[bookname]["Class"]=(input("Enter Branch/Class: ")).upper()
#                     self.__Ultimate_dict[bookname]["Roll_no."]=(input("Enter University/Class_Roll_no. : "))
#                     while 1:
#                         self.__Ultimate_dict[bookname]["Days"]=input("Enter no. of Days: ")
#                         try:
#                             if int(self.__Ultimate_dict[bookname]["Days"])>0:
#                                 break
#                         except:
#                             print("enter a natural no.")
#                             continue
#                     import datetime
#                     t1 = datetime.datetime.now()
#                     self.__Ultimate_dict[bookname]["Date_time"]=t1.strftime("%Y:%m:%d:%H:%M:%S")
#                 else:
#                     print("\n"+bookname+" was there in "+self.__lib_name+" collection!")
#                     print("It's with "+self.__Ultimate_dict[bookname]["Name"]+" ["+self.__Ultimate_dict[bookname]["Roll_no."]+"] of class "+self.__Ultimate_dict[bookname]["Class"]+" for "+'\033[1m'+'\033[4m'+self.__Ultimate_dict[bookname]["Days"]+'\033[0m'+" days from "+(self.__Ultimate_dict[bookname]["Date_time"])[8:10]+"/"+(self.__Ultimate_dict[bookname]["Date_time"])[5:7]+"/"+(self.__Ultimate_dict[bookname]["Date_time"])[:4]+".")
#             else:
#                 print("\t"+'\033[1m'+'\033[4m'+"Not"+'\033[0m'+" in our "+self.__lib_name+" collection.")
#         except Exception as e:
#             print(e) 
    
#     def add_book(self,bookname):
#         self.__list_of_books.append(bookname)
#         self.__Ultimate_dict[bookname]={"Name":None,"Class":None,"Roll_no.":None,"Days":None,"Date_time":None}
#         print("\n"+'\033[1m'+'\033[7m',"Thanks for adding "+bookname+" in our "+self.__lib_name+'\033[1m'+'\033[7m'+" library.",'\033[0m')

#     def return_book(self,bookname):
#         try:
#             if bookname in self.__list_of_books:
#                 if self.__Ultimate_dict[bookname]["Name"]==None and self.__Ultimate_dict[bookname]["Class"]==None and self.__Ultimate_dict[bookname]["Roll_no."]==None and self.__Ultimate_dict[bookname]["Days"]==None and self.__Ultimate_dict[bookname]["Date_time"]==None:    
#                     print("\nIt was taken without entry.\n")
#                 else:
#                     import datetime
#                     t2=datetime.datetime.now()
#                     d1=datetime.datetime.strptime(self.__Ultimate_dict[bookname]["Date_time"],'%Y:%m:%d:%H:%M:%S')
#                     d2=datetime.datetime.strptime(t2.strftime("%Y:%m:%d:%H:%M:%S"),'%Y:%m:%d:%H:%M:%S')
#                     diff=round((((d2 - d1).total_seconds())/86400),2)
#                     if diff > int(self.__Ultimate_dict[bookname]["Days"]):
#                         print(f'You are late with a fine of {((int(int(self.__Ultimate_dict[bookname]["Days"])-diff))*2)} Rs.')
#                         while 1:
#                             p=str(input("Paid (y,n): "))
#                             if p=="y":
#                                 self.__Ultimate_dict[bookname]["Name"]=None
#                                 self.__Ultimate_dict[bookname]["Class"]=None
#                                 self.__Ultimate_dict[bookname]["Roll_no."]=None
#                                 self.__Ultimate_dict[bookname]["Days"]=None
#                                 self.__Ultimate_dict[bookname]["Date_time"]=None
#                                 break
#                             elif p=="n":
#                                 return
#                             else:
#                                 print("Invalid input")
#                     else:
#                         print('\033[1m',"Thanks! For being on time.",'\033[0m')
#                         self.__Ultimate_dict[bookname]["Name"]=None
#                         self.__Ultimate_dict[bookname]["Class"]=None
#                         self.__Ultimate_dict[bookname]["Roll_no."]=None
#                         self.__Ultimate_dict[bookname]["Days"]=None
#                         self.__Ultimate_dict[bookname]["Date_time"]=None
#             else:
#                 print(f"\nHe might have came to add the book in our {self.__lib_name} library as it is not there.")
#         except Exception as e:
#             print(e)
        

# harry=library(["1984","98","A Doll's House","Absalom, Absalom!","Anna Karenina","Beloved(Beloved Trilogy)","Berlin Alexanderplatz","Blindness","Buddenbrooks: The Decline o...","Crime and Punishment","Dead Souls","Demons","Diary of a Madman and Other...","Don Quixote","Faust, First Part","Ficciones","Gargantua and Pantagruel","Grande Sertão: Veredas","Great Expectations","Gulliver's Travels: Travels...","Hamlet","History (La Storia)","Hunger","Independent People","Invisible Man","Jacques the Fatalist","Journey to the End of the N...","King Lear","Leaves of Grass","Lolita","Love in the Time of Cholera","Madame Bovary","Mahabharata","Medea","Memoirs of Hadrian","Metamorphoses","Middlemarch","Midnight's Children","Moby-Dick or, the Whale","Molloy / Malone Dies / The ...","Mrs. Dalloway","Njal's Saga","Nostromo","Oedipus Rex (The Theban Pl...","One Hundred Years of Solitude","Othello","Pedro Páramo","Pippi Longstocking (Pippi L...","Poems of Paul Celan","Pride and Prejudice","Père Goriot","Ramayana","Romancero gitano","Season of Migration to the ...","Selected Stories of Anton C...","Sentimental Education","Sons and Lovers","Swann's Way","The Adventures of Huckleber...","The Aeneid","The Arabian Nights","The Book of Disquiet","The Book of Job","The Brothers Karamazov","The Canterbury Tales","The Castle","The Collected Tales of Edga...","The Complete Essays","The Complete Fairy Tales","The Complete Stories","The Death of Ivan Ilych","The Decameron","The Divine Comedy","The Epic of Gilgamesh","The Golden Notebook","The Idiot","The Iliad","The Life and Opinions of Tr...","The Magic Mountain","The Man Without Qualities","The Odyssey","The Old Man and the Sea","The Orchard: The Bostan Of ...","The Recognition of Śakuntalā","The Red and the Black","The Sound and the Fury","The Sound of the Mountain","The Stranger","The Tale of Genji","The Tin Drum","The Trial","Things Fall Apart (The Afri...","To the Lighthouse","Ulysses","War and Peace","Wuthering Heights","Zeno's Conscience","Zorba the Greek","أولاد حارتنا","مثنوی معنوی",],str("{}Oaklofi{}".format('\033[3m','\033[0m')))
# methods=['display_book','lend_book','add_book','return_book']
# print("\nWay To use this libarary managment system\n")
# for i in range (len(methods)):
#     print(f"(:=> Press {methods[i][0]} to {methods[i]}")
# print("\nLets start!")
# while 1:
#     wish=str(input("\nWhat to do now: "))
#     if wish=="d":
#         harry.display_books()
#         continue
#     elif wish=="l":
#         book=str(input("Enter name of book you want: ")).title()
#         harry.lend_book(book)
#         continue
#     elif wish=="a": 
#         boo=str(input("Enter name of book you want to add: ")).title()
#         harry.add_book(boo)
#         continue
#     elif wish=="r":
#         bo=str(input("Enter name of book you want to return: ")).title()
#         harry.return_book(bo)
#         continue
#     else:
#         print("invalid input")
#         continue