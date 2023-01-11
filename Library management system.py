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