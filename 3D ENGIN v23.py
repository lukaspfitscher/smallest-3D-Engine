#pygame: for displaing a window and setting pixels
#random: for randomly choosing observation pixel
import pygame,random#u need to install this (pip install pygame)
dtc=50#max distanc, further points wound be checkt
Xcm,Ycm,Zcm=50,50,50#camera position (x,y,z-coordinates)
Xpo,Ypo,Zpo= 0, 0, 0#observing point (x,y,z-coordinates)
Xcn,Ycn,Zcn= 0, 0, 0#counter res,res, d
res=800#resolution res x res pixel, camera
screen=pygame.display.set_mode((res, res))
while True:#main loop
	if pygame.event.poll().type == pygame.QUIT:exit()#close the programm
	ZS=0
	while ZS<1000:
		ZS+=1#just to speed up the program
		Zpo=Zcm-Zcn#calculating observing point coordinants (camera points always in z-direction)
		Xpo=Xcm+Zcn-2*Zcn/res*Xcn#calculating observing point from observing pixel and distance(hard to understand)
		Ypo=Ycm-Zcn+2*Zcn/res*Ycn#calculating observing point from observing pixel and distance(hard to understand)
		if(#if observation point within these borders draw a pixel
			44<=Xpo<=56 and 28<=Ypo<=40 and 17<=Zpo<=23 or#head
			40<=Xpo<=60 and 44<=Ypo<=48 and 18<=Zpo<=22 or#shoulders
			40<=Xpo<=44 and 44<=Ypo<=56 and 18<=Zpo<=22 or#right arm
			40<=Xpo<=42 and 53<=Ypo<=55 and 12<=Zpo<=30 or#spear
			56<=Xpo<=60 and 44<=Ypo<=56 and 18<=Zpo<=22 or#left arm
			60<=Xpo<=62 and 46<=Ypo<=58 and 12<=Zpo<=26 or#shield
			48<=Xpo<=52 and 40<=Ypo<=62 and 18<=Zpo<=22 or#body
			44<=Xpo<=48 and 58<=Ypo<=74 and 18<=Zpo<=22 or#right leg
			52<=Xpo<=56 and 58<=Ypo<=74 and 18<=Zpo<=22 or#left  leg
			 0<=Xpo<=99 and 74<=Ypo<=82 and  0<=Zpo<=40): #floor
			color=int(round(255-255*(Zcn/dtc)))#for shadows, the more away the darker
			pygame.draw.rect(screen,(color,color,color),(Xcn,Ycn,1,1))#draw pixel
			Zcn=dtc+1#break if pixel is drawn
		Zcn=Zcn+1
		if Zcn>dtc:Zcn=0;Ycn=random.randint(0,799);Xcn=random.randint(0,799);
	pygame.display.update()