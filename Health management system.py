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