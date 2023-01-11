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