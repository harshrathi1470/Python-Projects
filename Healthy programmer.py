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