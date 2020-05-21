#!/usr/bin/env python
# -*- coding: utf-8 -*-

#the next line is only needed for python2.x and not necessary for python3.x
from __future__ import print_function, division
import pygame
import os
from math import pi

class Game(object):
    def main(self,screen):
        pygame.init()
        try:
            
            background = surface = pygame.Surface((4500, 3000), )#pygame.SRCALPHA
            snake = pygame.image.load("background.png")
        except:
            raise(UserWarning, "Unable to find the images in the folder")

        
        pygame.init()

        #Variable Definitions

        BLACK = (0,0,0)
        WHITE = (255,255,255)
        BLUE =  (  0,  0,255)
        GREEN = (  0,255,  0)
        RED =   (255,  0,  0)

        blue=(0,0,255)
        red=(95,0,0)
        green=(0,155,0)
        white=(255,255,255)
        black=(0,0,0)

        x=100
        y=600
        # y coor of roads
        yr=0    

        pi=3.142

        halfgate=210

        x_park=x+50-100
        y_park=y+700
        l_park=800
        b_park=400
        g_park=242
        c_park=242+30

        x_car=x+100+100
        y_car=y+100
        l_car=220
        b_car=400

        x_pg=x+550
        y_pg=y+700
        l_pg=300
        b_pg=230
        li=150
        bi=50

        x_work=x+1050
        y_work=y+600-30
        l_work=370
        b_work=360

        x_cblock=x+550
        y_cblock=y+1060
        l_cblock=430
        b_cblock=330

        x_ablock=x+550
        y_ablock=y+30
        l_ablock=430
        b_ablock=330


        x_bblock=x+1450
        y_bblock=y+30
        l_bblock=430
        b_bblock=330

        x_dblock=x+1450
        y_dblock=y+1060
        l_dblock=430
        b_dblock=330

        x_power2=x+1150
        y_power2=y+1650

        x_fg=x+2100
        y_fg=y
        l_fg=1350
        b_fg=1050

        x_ab=x+1150
        y_ab=y
        l_ab=400
        b_ab=200

        x_cd=x+1150
        y_cd=y+1030
        l_cd=400
        b_cd=200


        x_kcant=x+1530
        y_kcant=y+600

        x_robo=x+2980
        y_robo=y+1550


        x_lcanteen=x+2380+100
        y_lcanteen=y+1650-50
        l_lcanteen=330
        b_lcanteen=200

        x_boyho=x+2280
        y_boyho=y+2000
        l_boyho=330
        b_boyho=200

        x_b1=x+2980
        y_b1=y+2050

        x_cric=x+3500
        y_cric=y+1300

        x_nim=x+3600
        y_nim=y


        x_pharma=x+4400
        y_pharma=y

        x_pcant=x+4200
        y_pcant=y+700

        x_science=x+4400
        y_science=y+1000


        x_lblock=x+2250
        y_lblock=y+1160
        l_lblock=330
        b_lblock=230

        x_girlho=x+2750
        y_girlho=y+1240
        l_girlho=410
        b_girlho=154

        x_ten1=x+3400
        y_ten1=y+2600

        x_ten2=x+3650
        y_ten2=y+2600

        x_ten3=x+3900
        y_ten3=y+2600

        x_bask1=x+4200
        y_bask1=y+2600

        x_bask1=x+4200
        y_bask1=y+2600

        x_bask2=x+4450
        y_bask2=y+2600

        x_vol1=x+4800
        y_vol1=y+2600

        x_vol2=x+5100
        y_vol2=y+2600

        x_cricpit=x+5400
        y_cricpit=y+2600

        #--road colors--------
        colab=200
        colcd=200

        col01=200
        col02=200
        col03=200
        col04=200
        col05=200
        col06=200
        col07=200
        col08=200
        col09=200
        col10=200
        col11=200
        col12=200
        col13=200
        col14=200
        col15=200
        col16=200
        col17=200
        col18=200
        col19=200
        col20=200
        col21=200
        col22=200
        col23=200
        col24=200
        col25=200
        col26=200
        col27=200
        col28=200
        col29=200
        col30=200
        col31=200
        col32=200
        col33=200
        col34=200
        col35=200
        col36=200
        col37=200
        col38=200
        col39=200
        col40=200
        col41=200
        col42=200
        col43=200
        col44=200
        col45=200
        col46=200
        col47=200
        col48=200
        col49=200
        col50=200
        col51=200
        col52=200
        col53=200
        col54=200
        col55=200
        col56=200
        col57=200
        col58=200
        col59=200
        col60=200

        col11_1=200
        col07_1=200
        col23_2=200
        col23_1=200
        col45_1=200
        col46_1=200
        col20_1=200
        col54_1=200
        col31_1=200
        col38_1=200
        

        #--------------------

        x_src=0
        y_src=0
        x_dst=0
        y_dst=0

        mouse_x=-5600
        mouse_y=-5100

        pixel_src=(0,0,0,0)
        pixel_dst=(0,0,0,0)

        #------ROADS coordinates--------------

        x_ab1=x_ab
        y_ab1=y_ab+b_ab/2

        x_cd1=x_cd
        y_cd1=y_cd+b_cd/2

        x_4=x_cblock-40
        y_4=y_cblock+l_cblock+10

        x_5=x_cblock+l_cblock
        y_5=y_cblock+(b_cblock/2)

        x_6=x_cblock+l_cblock
        y_6=y_cblock


        x_8=x_pg+l_pg+60
        y_8=y_pg+(b_pg/2)

        x_10=x_pg+l_pg+80
        y_10=y_pg-160

        x_13=x_ablock+485
        y_13=y_ablock-50

        x_12=x_13
        y_12=y_13+200

        x_16=x_bblock-50
        y_16=y_ablock-50

        x_17=x_16
        y_17=y_13+200

        x_19=x_work-30  
        y_19=y_work-70

        x_18=x_19+150  
        y_18=y_work-70

        x_20=x_18+350  
        y_20=y_work-70


        x_21=x_work+350
        y_21=y_work

        x_20_1=x_20-50
        y_20_1=y_20

        x_22=x_work+350
        y_22=y_work+190


        x_23_1=x_8+10
        y_23_1=y_8+165 

        x_23=x_23_1+190
        y_23=y_23_1

        x_23_2=x_23
        y_23_2=y_23


        x_24=x_23+70+b_ab
        y_24=y_23

        x_25=x_24
        y_25=y_24+200

        x_26=x_dblock-40
        y_26=y_dblock+l_dblock

        x_28=x_dblock-40
        y_28=y_dblock+l_dblock



        x_32=x_23_2+300
        y_32=y_23_2

        x_31=x_32+500
        y_31=y_32

        x_31_1=x_31+30
        y_31_1=y_31+100

        x_30=x_31
        y_30=y_31+100

        x_33=x_31
        y_33=y_kcant

        x_34=x_bblock+l_bblock
        y_34=y_bblock-80


        x_29=x_34
        y_29=y_30+300


        x_7_1=x_23_1
        y_7_1=y_23_1

        x_7=x_pg
        y_7=y_pg+280

        x_24=x_23+70+b_ab
        y_24=y_23

        x_11=x_pg
        y_11=y_pg-200

        x_11_1=x_11+400
        y_11_1=y_11

        x_9=x_pg+l_pg+60
        y_9=y_pg-200

        x_14=x_ablock
        y_14=y_ablock-120

        x_15=x_14+520
        y_15=y_14

        x_35=x_15+330
        y_35=y_14

        x_36=x_fg+160
        y_36=y_fg-280


        x_42=x_lblock-250
        y_42=y_lblock+330

        x_41=x_42+340
        y_41=y_42

        x_40=x_41+400
        y_40=y_41



        x_59=x_36+1200
        y_59=y_36

        x_57=x_59+400
        y_57=y_59

        x_37=x_59-200
        y_37=y_59



        x_56=x_57+400
        y_56=y_57

        x_58=x_fg+160
        y_58=y_fg-280

        x_59=x_36+1200
        y_59=y_36

       
        x_38=x_31+l_fg
        y_38=y_kcant

        x_38_1=x_38
        y_38_1=y_38+480

        x_39=x_38
        y_39=y_38+550

        x_49=x_31+l_fg
        y_49=y_kcant

        x_50=x_49+450
        y_50=y_kcant

        x_53=x_science
        y_53=y_science-200

        x_52=x_53
        y_52=y_53-200

        x_54=x_53
        y_54=y_52-200

        x_54_1=x_53
        y_54_1=y_52-200

        x_51=x_science
        y_51=y_science-200

        x_55=x_science
        y_55=y_ablock-350

        x_42=x_lblock-250
        y_42=y_lblock+330

        x_41=x_42+340
        y_41=y_42

        x_40=x_41+400
        y_40=y_41

        x_60=x_59
        y_60=y_59-500

        x_45=x_40-40
        y_45=y_40+40

        x_45_1=x_45
        y_45_1=y_45+200

        x_46=x_45
        y_46=y_45+200

        x_46_1=x_46
        y_46_1=y_46+400

        x_43=x_41+120
        y_43=y_41

        x_44=x_43
        y_44=y_43+200

        x_compass=-20
        y_compass=0

        x_47=x_38
        y_47=y_38+550+300

        x_48=x_38
        y_48=y_38+550+500







        #Setting up the environment

        screen=pygame.display.set_mode((1240,600)) 

        background.fill((215,218,210))

        # png image has transparent color
        snake = snake.convert_alpha()
        # store a unmodified copy of the snake surface       
        snake_original = snake.copy()
        # start position of snake surface      
        snakex, snakey = 0,0           
        # snake speed in pixel per second !
        dx, dy  = 0, 0                   
        # in pixel / second
        speed = 700                      
        # current orientation of snake 
        angle = 0                        
        # current zoom factor
        zoom = 0.2                       
        zoomspeed = 0.1
        # in Grad (360) per second
        turnspeed = 180                  
        

        #overwrite all
        screen.blit(background, (0,0))     
        # blit the snake shape
        screen.blit(snake, (snakex, snakey))
        # create pygame clock object   
        clock = pygame.time.Clock()         
        mainloop = True
        FPS = 120         
        flag=0 
        # desired max. framerate in frames per second.
        mx=0
        my=0                  


        while mainloop:
        	
        	# milliseconds passed since last frame
            milliseconds = clock.tick(FPS)  
            # seconds passed since last frame
            seconds = milliseconds / 1000.0 


            for event in pygame.event.get():
               
                #To toggle betweeen fulscreen and normal mode
               
                if event.type is pygame.KEYDOWN and event.key == pygame.K_F11:   
                    screen=pygame.display.set_mode((950,700))
                if event.type is pygame.KEYDOWN and event.key == pygame.K_F10:
                    screen=pygame.display.set_mode((950,700),pygame.FULLSCREEN)
                
                #Closing the window
                if event.type == pygame.QUIT:
                    mainloop = False # pygame window closed by user
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False # user pressed ESC
                #Detecting mouse movement
                elif event.type==pygame.MOUSEMOTION:
                     x_compass,y_compass=event.pos
                     x_compass=5
                     y_compass=5

                #Detecting mouseclick     	
                elif  event.type==pygame.MOUSEBUTTONDOWN:
                    
                    #left click
                    if event.button==1:
                        print("left")
                        # stores coordinates of leftclick
                        x_src,y_src=event.pos 
                        print(screen.get_at((x_src,y_src)))
                        pixel_src=screen.get_at((x_src,y_src))
                        print(pixel_src)
                    
                    #right click    
                    elif event.button==3:
                        print("right")
                        #stores coordinates of rightclick
                        x_dst,y_dst=event.pos 
                        pixel_dst=screen.get_at((x_dst,y_dst))

            

            pygame.display.set_caption("Navigate: Arrow keys, Zoom: W and S, Rotate:A and D "
                "%.2f zoom: %.2f angle %.2f" % (clock.get_fps(), zoom, angle))
            
            screen.blit(background,(0,0))
                
            
            # move snake with cursor keys
            pressedkeys = pygame.key.get_pressed()
            # no cursor key, no movement
            dx, dy  = 0, 0   
            if pressedkeys[pygame.K_LEFT]:
                dx += speed
            if pressedkeys[pygame.K_RIGHT]:
                dx -= speed
            if pressedkeys[pygame.K_UP]:
                dy += speed
            if pressedkeys[pygame.K_DOWN]:
                dy -= speed
            
            #calculate new center of snake 
            # time based movement
            snakex += dx * seconds 
            snakey += dy * seconds
            

            # rotate snake with a and d key
            # neither a nor d, no turning
            turnfactor = 0  
            # counter-clockwise
            if pressedkeys[pygame.K_a]:
                turnfactor += 1 
            #clock-wise    
            if pressedkeys[pygame.K_d]:
                turnfactor -= 1 
            

            # zoom snake with w and s key
            # neither w nor s, no zooming
            zoomfactor = 1.0 
            if pressedkeys[pygame.K_w]:
                zoomfactor += zoomspeed
            if pressedkeys[pygame.K_s]:
                zoomfactor -= zoomspeed
            if turnfactor != 0 or zoomfactor !=1.0 or 1:
                angle += turnfactor * turnspeed * seconds # time-based turning
                zoom *= zoomfactor 
                # the surface shrinks and zooms and moves by rotating
                oldrect = snake.get_rect() # store current surface rect
               
                pygame.draw.lines(snake_original,BLACK,False,[[x_park,y_park],[x_park+b_park+20,y_park],[x_park+b_park+20,y_park+g_park+10-35],[x_park+b_park+20+20,y_park+g_park+10-35],[x_park+b_park+20+20,y_park+g_park+10]],7)
                
                pygame.draw.arc(snake_original, BLACK,[x_park+b_park, y_park+g_park+10-80, 80, 80], pi,3*pi/2,7)

                pygame.draw.lines(snake_original,BLACK,False,[[x_park+b_park,y_park+g_park+10-40],[x_park+b_park+10,y_park+g_park+10-40],[x_park+b_park+10,y_park+10],[x_park+b_park+10-35,y_park+10]],7)



                #bike parking
                
                #1
                # left arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25,y_park+10+45-22,44,44],pi/2,3*pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22,y_park+10+45-22],[x_park+10+25+22,y_park+10+45-15],[x_park+10+25+22+5,y_park+10+45-15],[x_park+10+25+22+5,y_park+10+45-5]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22,y_park+10+45+22],[x_park+10+25+22,y_park+10+45+15],[x_park+10+25+22+5,y_park+10+45+15],[x_park+10+25+22+5,y_park+10+45+5]],7) 

                # central lines
                pygame.draw.line(snake_original,BLACK,(x_park+10+25+22+5,y_park+10+45-5),(x_park+10+25+22+5+290,y_park+10+45-5),7)
                pygame.draw.line(snake_original,BLACK,(x_park+10+25+22+5,y_park+10+45+5),(x_park+10+25+22+5+290,y_park+10+45+5),7)

                # right arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25+22+5+290+5-22,y_park+10+45-22,44,44],3*pi/2, 2*pi,7)
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25+22+5+290+5-22,y_park+10+45-22,44,44],0, pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22+5+290+5,y_park+10+45-22],[x_park+10+25+22+5+290+5,y_park+10+45-15],[x_park+10+25+22+5+290,y_park+10+45-15],[x_park+10+25+22+5+290,y_park+10+45-5]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22+5+290+5,y_park+10+45+22],[x_park+10+25+22+5+290+5,y_park+10+45+15],[x_park+10+25+22+5+290,y_park+10+45+15],[x_park+10+25+22+5+290,y_park+10+45+5]],2         ) 
                #2
                # left arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25,y_park+10+45+10+45+2-22,44,44],pi/2,3*pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22,y_park+10+45-22+10+45+2],[x_park+10+25+22,y_park+10+45-15+10+45+2],[x_park+10+25+22+5,y_park+10+45-15+10+45+2],[x_park+10+25+22+5,y_park+10+45+10+45-5+2]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22,y_park+10+45+22+10+45+2],[x_park+10+25+22,y_park+10+45+15+10+45+2],[x_park+10+25+22+5,y_park+10+45+15+10+45+2],[x_park+10+25+22+5,y_park+10+45+5+10+45+2]],7) 
                # central lines
                pygame.draw.line(snake_original,BLACK,(x_park+10+25+22+5,y_park+10+45-5+10+45+2),(x_park+10+25+22+5+290,y_park+10+45-5+10+45+2),7)
                pygame.draw.line(snake_original,BLACK,(x_park+10+25+22+5,y_park+10+45+5+10+45+2),(x_park+10+25+22+5+290,y_park+10+45+5+10+45+2),7)
                # right arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25+22+5+290+5-22,y_park+10+45-22+10+45+2,44,44],3*pi/2, 2*pi,7)
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25+22+5+290+5-22,y_park+10+45-22+10+45+2,44,44],0, pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22+5+290+5,y_park+10+45-22+10+45+2],[x_park+10+25+22+5+290+5,y_park+10+45-15+10+45+2],[x_park+10+25+22+5+290,y_park+10+45-15+10+45+2],[x_park+10+25+22+5+290,y_park+10+45-5+10+45+2]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22+5+290+5,y_park+10+45+22+10+45+2],[x_park+10+25+22+5+290+5,y_park+10+45+15+10+45+2],[x_park+10+25+22+5+290,y_park+10+45+15+10+45+2],[x_park+10+25+22+5+290,y_park+10+45+5+10+45+2]],7) 
                #3
                # left arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25,y_park+10+45+2*(10+45)-22+4,44,44],pi/2,3*pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22,y_park+10+45-22+2*(10+45)+4],[x_park+10+25+22,y_park+10+45-15+2*(10+45)+4],[x_park+10+25+22+5,y_park+10+45-15+2*(10+45)+4],[x_park+10+25+22+5,y_park+10+45-5+2*(10+45)+4]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22,y_park+10+45+22+2*(10+45)+4],[x_park+10+25+22,y_park+10+45+15+2*(10+45)+4],[x_park+10+25+22+5,y_park+10+45+15+2*(10+45)+4],[x_park+10+25+22+5,y_park+10+45+5+2*(10+45)+4]],7) 
                # central lines
                pygame.draw.line(snake_original,BLACK,(x_park+10+25+22+5,y_park+10+45-5+2*(10+45)+4),(x_park+10+25+22+5+290,y_park+10+45-5+2*(10+45)+4),7)
                pygame.draw.line(snake_original,BLACK,(x_park+10+25+22+5,y_park+10+45+5+2*(10+45)+4),(x_park+10+25+22+5+290,y_park+10+45+5+2*(10+45)+4),7)
                # right arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25+22+5+290+5-22,y_park+10+45-22+2*(10+45)+4,44,44],3*pi/2, 2*pi,7)
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25+22+5+290+5-22,y_park+10+45-22+2*(10+45)+4,44,44],0, pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22+5+290+5,y_park+10+45-22+2*(10+45)+4],[x_park+10+25+22+5+290+5,y_park+10+45-15+2*(10+45)+4],[x_park+10+25+22+5+290,y_park+10+45-15+2*(10+45)+4],[x_park+10+25+22+5+290,y_park+10+45-5+2*(10+45)+4]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22+5+290+5,y_park+10+45+22+2*(10+45)],[x_park+10+25+22+5+290+5,y_park+10+45+15+2*(10+45)+4],[x_park+10+25+22+5+290,y_park+10+45+15+2*(10+45)+4],[x_park+10+25+22+5+290,y_park+10+45+5+2*(10+45)+4]],7) 
                #4
                # left arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25,y_park+10+45-22+3*(10+45+2),44,44],pi/2,(3*pi/2)+(pi/16),7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22,y_park+10+45-22+3*(10+45+2)],[x_park+10+25+22,y_park+10+45-15+3*(10+45+2)],[x_park+10+25+22+5,y_park+10+45-15+3*(10+45+2)],[x_park+10+25+22+5,y_park+10+45-5+3*(10+45+2)]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22,y_park+10+45+22],[x_park+10+25+22,y_park+10+45+15],[x_park+10+25+22+5,y_park+10+45+15],[x_park+10+25+22+5,y_park+10+45+5]],7) 
                # central lines
                pygame.draw.line(snake_original,BLACK,(x_park+10+25+22+5,y_park+10+45-5+3*(10+45+2)),(x_park+10+25+22+5+290,y_park+10+45-5+3*(10+45+2)),7)
                pygame.draw.line(snake_original,BLACK,(x_park+10+25+22+5-2,y_park+10+45+5+3*(10+45+2)+15),(x_park+10+25+22+5+290,y_park+10+45+5+3*(10+45+2)+15),7)
                # right arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25+22+5+290+5-22,y_park+10+45-22+3*(10+45+2),44,44],(3*pi/2)-(pi/16), 2*pi,7)
                pygame.draw.arc(snake_original,BLACK,[x_park+10+25+22+5+290+5-22,y_park+10+45-22+3*(10+45+2),44,44],0, pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22+5+290+5,y_park+10+45-22+3*(10+45+2)],[x_park+10+25+22+5+290+5,y_park+10+45-15+3*(10+45+2)],[x_park+10+25+22+5+290,y_park+10+45-15+3*(10+45+2)],[x_park+10+25+22+5+290,y_park+10+45-5+3*(10+45+2)]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+25+22+5+290+5,y_park+10+45+22],[x_park+10+25+22+5+290+5,y_park+10+45+15],[x_park+10+25+22+5+290,y_park+10+45+15],[x_park+10+25+22+5+290,y_park+10+45+5]],7) 
                #car parking
                #1
                #top arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+70,y_park+10+c_park,70,70],0,pi,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70,y_park+10+c_park+35],[x_park+10+70+15,y_park+10+c_park+35],[x_park+10+70+15,y_park+10+c_park+35+5],[x_park+10+70+15+15,y_park+10+c_park+35+5]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+70,y_park+10+c_park+35],[x_park+10+70+70-15,y_park+10+c_park+35],[x_park+10+70+70-15,y_park+10+c_park+35+5],[x_park+10+70+70-15-15,y_park+10+c_park+35+5]],7) 
                # central lines
                pygame.draw.line(snake_original,BLACK,(x_park+10+70+15+15,y_park+10+c_park+35+5),(x_park+10+70+15+15,y_park+10+c_park+35+5+460),7)
                pygame.draw.line(snake_original,BLACK,(x_park+10+70+70-15-15,y_park+10+c_park+35+5),(x_park+10+70+70-15-15,y_park+10+c_park+35+5+460),7)
                # bottom arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+70,y_park+10+c_park+40+460+5-35,70,70],pi, 2*pi,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70,y_park+10+c_park+35+5+460+5],[x_park+10+70+15,y_park+10+c_park+35+5+460+5],[x_park+10+70+15,y_park+10+c_park+35+5+460],[x_park+10+70+15+15,y_park+10+c_park+35+5+460]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+70,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+40,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+40,y_park+10+c_park+35+5+460],[x_park+10+70+15+15+10,y_park+10+c_park+35+5+460]],7) 
                
                #2
                #top arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+70+110,y_park+10+c_park,70,70],0,pi,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+110,y_park+10+c_park+35],[x_park+10+70+15+110,y_park+10+c_park+35],[x_park+10+70+15+110,y_park+10+c_park+35+5],[x_park+10+70+15+15+110,y_park+10+c_park+35+5]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+70+110,y_park+10+c_park+35],[x_park+10+70+70-15+110,y_park+10+c_park+35],[x_park+10+70+70-15+110,y_park+10+c_park+35+5],[x_park+10+70+70-15-15+110,y_park+10+c_park+35+5]],7) 
                # central lines
                pygame.draw.line(snake_original,BLACK,(x_park+10+70+15+15+110,y_park+10+c_park+35+5),(x_park+10+70+15+15+110,y_park+10+c_park+35+5+460),7)
                pygame.draw.line(snake_original,BLACK,(x_park+10+70+70-15-15+110,y_park+10+c_park+35+5),(x_park+10+70+70-15-15+110,y_park+10+c_park+35+5+460),7)
                # bottom arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+70+110,y_park+10+c_park+40+460+5-35,70,70],pi, 2*pi,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+110,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+110,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+110,y_park+10+c_park+35+5+460],[x_park+10+70+15+15+110,y_park+10+c_park+35+5+460]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+70+110,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+40+110,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+40+110,y_park+10+c_park+35+5+460],[x_park+10+70+15+15+10+110,y_park+10+c_park+35+5+460]],7) 
                #3
                #top arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+70+220,y_park+10+c_park,70,70],0,pi,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+220,y_park+10+c_park+35],[x_park+10+70+15+220,y_park+10+c_park+35],[x_park+10+70+15+220,y_park+10+c_park+35+5],[x_park+10+70+15+15+220,y_park+10+c_park+35+5]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+70+220,y_park+10+c_park+35],[x_park+10+70+70-15+220,y_park+10+c_park+35],[x_park+10+70+70-15+220,y_park+10+c_park+35+5],[x_park+10+70+70-15-15+220,y_park+10+c_park+35+5]],7) 
                # central lines
                pygame.draw.line(snake_original,BLACK,(x_park+10+70+15+15+220,y_park+10+c_park+35+5),(x_park+10+70+15+15+220,y_park+10+c_park+35+5+460),7)
                pygame.draw.line(snake_original,BLACK,(x_park+10+70+70-15-15+220,y_park+10+c_park+35+5),(x_park+10+70+70-15-15+220,y_park+10+c_park+35+5+460),7)
                # bottom arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+70+220,y_park+10+c_park+40+460+5-35,70,70],pi, 2*pi,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+220,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+220,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+220,y_park+10+c_park+35+5+460],[x_park+10+70+15+15+220,y_park+10+c_park+35+5+460]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+70+220,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+40+220,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+40+220,y_park+10+c_park+35+5+460],[x_park+10+70+15+15+10+220,y_park+10+c_park+35+5+460]],7) 
                #4
                #top arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+70+330,y_park+10+c_park,70,70],pi/2,pi,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+330,y_park+10+c_park+35],[x_park+10+70+15+330,y_park+10+c_park+35],[x_park+10+70+15+330,y_park+10+c_park+35+5],[x_park+10+70+15+15+330,y_park+10+c_park+35+5]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+70,y_park+10+c_park+35],[x_park+10+70+70-15,y_park+10+c_park+35],[x_park+10+70+70-15,y_park+10+c_park+35+5],[x_park+10+70+70-15-15,y_park+10+c_park+35+5]],7) 
                # central lines
                pygame.draw.line(snake_original,BLACK,(x_park+10+70+15+15+330,y_park+10+c_park+35+5),(x_park+10+70+15+15+330,y_park+10+c_park+35+5+460),7)
                pygame.draw.line(snake_original,BLACK,(x_park+10+70+70-15-15,y_park+10+c_park+35+5),(x_park+10+70+70-15-15,y_park+10+c_park+35+5+460),7)
                # bottom arc and adjacent lines
                pygame.draw.arc(snake_original,BLACK,[x_park+10+70+330,y_park+10+c_park+40+460+5-35,70,70],pi, 3*pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+330,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+330,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+330,y_park+10+c_park+35+5+460],[x_park+10+70+15+15+330,y_park+10+c_park+35+5+460]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_park+10+70+70,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+40,y_park+10+c_park+35+5+460+5],[x_park+10+70+15+40,y_park+10+c_park+35+5+460],[x_park+10+70+15+15+10,y_park+10+c_park+35+5+460]],7) 
         
        		#Car Parking

                pygame.draw.lines(snake_original,BLACK,False,[[x_car,y_car+b_car-75],[x_car,y_car],[x_car+l_car,y_car],[x_car+l_car,y_car+b_car-2],[x_car+l_car-26,y_car+b_car-2]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_car+l_car,y_car+b_car-75],[x_car+l_car-25,y_car+b_car-75],[x_car+l_car-25,y_car+b_car-50],[x_car+l_car-75,y_car+b_car-50]],7)

                pygame.draw.arc(snake_original,BLACK,[x_car+l_car-75,y_car+b_car-100,100,100],pi,3*pi/2,7)

                pygame.draw.lines(snake_original,BLACK,False,[[x_car+15,y_car+b_car-78],[x_car+15,y_car+35],[x_car+15+25,y_car+35],[x_car+15+25,y_car+15],[x_car+l_car-25,y_car+15],[x_car+l_car-25,y_car+35],[x_car+l_car,y_car+35]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_car+15,y_car+b_car-78],[x_car+15+25,y_car+b_car-78],[x_car+15+25,y_car+b_car-50],[x_car+15+25+50,y_car+b_car-50]],7)

                pygame.draw.arc(snake_original,BLACK,[x_car+15+25-50,y_car+b_car-100,100,100],3*pi/2,2*pi,7)

                pygame.draw.lines(snake_original,BLACK,False,[[x_car-10,y_car+b_car-75],[x_car+15,y_car+b_car-75],[x_car+15,y_car+b_car-65],[x_car+15+19,y_car+b_car-65],[x_car+15+22,y_car+b_car-62],[x_car+15+22,y_car+b_car-62+44],[x_car+15+19,y_car+b_car-62+44+3],[x_car-29,y_car+b_car-62+44+3],[x_car-32,y_car+b_car-62+44],[x_car-32,y_car+b_car-62],[x_car-29,y_car+b_car-62-3],[x_car-10,y_car+b_car-65],[x_car-10,y_car+b_car-75]],7)
                
                #PG Block
                pygame.draw.polygon(snake_original, BLACK, [[x_pg,y_pg], [x_pg+l_pg,y_pg], [x_pg+l_pg,y_pg+b_pg],[x_pg,y_pg+b_pg]],7)
                pygame.draw.polygon(snake_original,BLACK,[[x_pg+(l_pg-li)/2,y_pg+(b_pg-bi)/2],[x_pg+(l_pg-li)/2+li,y_pg+(b_pg-bi)/2],[x_pg+(l_pg-li)/2+li,y_pg+(b_pg-bi)/2+bi],[x_pg+(l_pg-li)/2,y_pg+(b_pg-bi)/2+bi]],7)
                pygame.draw.polygon(snake_original,BLACK,[[x_pg,y_pg+(b_pg-bi)/2],[x_pg+20,y_pg+(b_pg-bi)/2],[x_pg+20,y_pg+(b_pg-bi)/2+bi],[x_pg,y_pg+(b_pg-bi)/2+bi]],7)

                pygame.draw.arc(snake_original, BLACK,[x_pg+(l_pg-li)/2-15+li,y_pg+(b_pg-bi)/2+10, 30, 30], pi/2,3*pi/2,7)
                pygame.draw.arc(snake_original, BLACK,[x_pg+(l_pg-li)/2-8+li,y_pg+(b_pg-bi)/2+17, 16, 16], pi/2,3*pi/2,7)
                pygame.draw.line(snake_original,BLACK,(x_pg+l_pg-20,y_pg+(b_pg-bi)/2+17),(x_pg+l_pg+20,y_pg+(b_pg-bi)/2+17),7)
                pygame.draw.line(snake_original,BLACK,(x_pg+l_pg-20,y_pg+(b_pg-bi)/2+17+16+5),(x_pg+l_pg+20,y_pg+(b_pg-bi)/2+17+16+5),7)

                pygame.draw.line(snake_original,BLACK,(x_pg+l_pg+20,y_pg+(b_pg-bi)/2-10),(x_pg+l_pg+20,y_pg+(b_pg-bi)/2+bi+10),7)
                pygame.draw.line(snake_original,BLACK,(x_pg+l_pg+20,y_pg+(b_pg-bi)/2-10),(x_pg+l_pg+20+20,y_pg+(b_pg-bi)/2-10),7)
                pygame.draw.line(snake_original,BLACK,(x_pg+l_pg+20,y_pg+(b_pg-bi)/2+bi+10),(x_pg+l_pg+20+20,y_pg+(b_pg-bi)/2+bi+10),7)

                pygame.draw.lines(snake_original,BLACK,False,[[x_pg+l_pg,y_pg+(b_pg-bi)/2+17],[x_pg+l_pg,y_pg+(b_pg-bi)/2],[x_pg+l_pg+20,y_pg+(b_pg-bi)/2]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_pg+l_pg,y_pg+(b_pg-bi)/2+17+16+5],[x_pg+l_pg,y_pg+(b_pg-bi)/2+bi],[x_pg+l_pg+20,y_pg+(b_pg-bi)/2+bi]],7)
                

                #Workshop
                pygame.draw.lines(snake_original,BLACK,False,[[x_work,y_work+130],[x_work+40,y_work+90],[x_work+40+20,y_work+90],[x_work+40+20+40,y_work+130],[x_work+40+20+40+10,y_work+130-10],[x_work+40+20+40+10-25,y_work+130-10-25],[x_work+40+20+40+10-25,y_work+130-10-25-20],[x_work+40+20+40+10-25+40,y_work+130-10-25-20-40],[x_work+40+20+40+10-25+40+20,y_work+130-10-25-20-40],[x_work+40+20+40+10-25+40+20,y_work+15],[x_work+40+20+40+10-25+40+20+15,y_work]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_work,y_work+130],[x_work,y_work+130+20],[x_work+40,y_work+130+20+40],[x_work+40,y_work+130+20+40+10]],7)
                pygame.draw.arc(snake_original,BLACK,[x_work+15,y_work+130+20+40+10,50,50],pi/2, 3*pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_work+40,y_work+130+20+40+10+50],[x_work+40,y_work+130+20+40+10+50+10],[x_work,y_work+130+20+40+10+50+10+40],[x_work,y_work+130+20+40+10+50+10+40+20],[x_work+40,y_work+b_work]],7)
                
                pygame.draw.line(snake_original,BLACK,(x_work+40,y_work+b_work),(x_work+l_work-40,y_work+b_work),7)
                    
                pygame.draw.lines(snake_original,BLACK,False,[[x_work+l_work-40,y_work+130+20+40+10+50],[x_work+l_work-40,y_work+130+20+40+10+50+10],[x_work+l_work,y_work+130+20+40+10+50+10+40],[x_work+l_work,y_work+130+20+40+10+50+10+40+20],[x_work+l_work-40,y_work+b_work]],7)
                pygame.draw.arc(snake_original,BLACK,[x_work+l_work-15-50,y_work+130+20+40+10,50,50],3*pi/2, 2*pi,7)
                pygame.draw.arc(snake_original,BLACK,[x_work+l_work-15-50,y_work+130+20+40+10,50,50],0, pi/2,7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_work+l_work,y_work+130],[x_work+l_work,y_work+130+20],[x_work+l_work-40,y_work+130+20+40],[x_work+l_work-40,y_work+130+20+40+10]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_work+l_work,y_work+130],[x_work+l_work-40,y_work+90],[x_work+l_work-40-50,y_work+90+50],[x_work+l_work-40-50-25,y_work+90+50-25], [x_work+l_work-40-20-40-10+25,y_work+130-10-15-20], [x_work+l_work-40-20-40-10+25-40,y_work+130-10-15-20-10-40],[x_work+l_work-40-20-40-10+25-40-20,y_work+130-10-15-20-10-40],[x_work+l_work-40-20-40-10+25-40-20,y_work+15],[x_work+l_work-40-20-40-10+25-40-20-15,y_work]],7)
                    
                pygame.draw.line(snake_original,BLACK,(x_work+155,y_work+35),(x_work+155,y_work+15),7)
                pygame.draw.line(snake_original,BLACK,(x_work+215,y_work+35),(x_work+215,y_work+15),7)

                pygame.draw.line(snake_original,BLACK,(x_work+155,y_work+15),(x_work+170,y_work),7)
                pygame.draw.line(snake_original,BLACK,(x_work+215,y_work+15),(x_work+200,y_work),7)

                pygame.draw.line(snake_original,BLACK,(x_work+160,y_work),(x_work+170,y_work),7)
                pygame.draw.line(snake_original,BLACK,(x_work+200,y_work),(x_work+210,y_work),7)
                    
                pygame.draw.line(snake_original,BLACK,(x_work+155,y_work+15),(x_work+215,y_work+15),7)


                #C-Block
                pygame.draw.lines(snake_original,BLACK, False, [(x_cblock,y_cblock),((x_cblock+30),(y_cblock-30)),((x_cblock+30+l_cblock),(y_cblock-30)),
                    ((x_cblock+l_cblock+30+30),(y_cblock)),((x_cblock+l_cblock+30),(y_cblock+30)),((x_cblock+30+l_cblock),(y_cblock+halfgate-30)),
                    ((x_cblock+30+l_cblock+30+30),(y_cblock+halfgate-30)),((x_cblock+30+l_cblock+30+30),(y_cblock+halfgate)),((x_cblock+30+l_cblock),
                        (y_cblock+halfgate)),((x_cblock+l_cblock+30),(y_cblock+b_cblock+30)),((x_cblock+l_cblock+30),(y_cblock+b_cblock+30)),
                    ((x_cblock+l_cblock+30+30),(y_cblock+b_cblock+30+30)),((x_cblock+l_cblock+30),(y_cblock+b_cblock+30+30+30)),((x_cblock+l_cblock+30),
                        (y_cblock+b_cblock+30+30+30)),((x_cblock+30),(y_cblock+b_cblock+30+30+30)),((x_cblock),(y_cblock+b_cblock+30+30)),(x_cblock+30,y_cblock+b_cblock+30),
                    (x_cblock+30,y_cblock+30),(x_cblock,y_cblock)],7)


               


                #A-Block
                pygame.draw.lines(snake_original,BLACK, False, [(x_ablock,y_ablock),((x_ablock+30),(y_ablock-30)),((x_ablock+30+l_ablock),(y_ablock-30)),
                    ((x_ablock+l_ablock+30+30),(y_ablock)),((x_ablock+l_ablock+30),(y_ablock+30)),((x_ablock+30+l_ablock),(y_ablock+halfgate-30)),
                    ((x_ablock+30+l_ablock+30+30),(y_ablock+halfgate-30)),((x_ablock+30+l_ablock+30+30),(y_ablock+halfgate)),((x_ablock+30+l_ablock),
                        (y_ablock+halfgate)),((x_ablock+l_ablock+30),(y_ablock+b_ablock+30)),((x_ablock+l_ablock+30),(y_ablock+b_ablock+30)),
                    ((x_ablock+l_ablock+30+30),(y_ablock+b_ablock+30+30)),((x_ablock+l_ablock+30),(y_ablock+b_ablock+30+30+30)),((x_ablock+l_ablock+30),
                        (y_ablock+b_ablock+30+30+30)),((x_ablock+30),(y_ablock+b_ablock+30+30+30)),((x_ablock),(y_ablock+b_ablock+30+30)),(x_ablock+30,y_ablock+b_ablock+30),
                    (x_ablock+30,y_ablock+30),(x_ablock,y_ablock)],7)

                #B-block
                pygame.draw.lines(snake_original, BLACK, False, [(x_bblock,y_bblock),((x_bblock+30),(y_bblock-30)),((x_bblock+30+l_bblock),(y_bblock-30)),((x_bblock+l_bblock+30+30),
                    (y_bblock)),
                   ((x_bblock+l_bblock+30),(y_bblock+30)),((x_bblock+30+l_bblock),(y_bblock+b_bblock+30)),((x_bblock+30+l_bblock+30),(y_bblock+b_bblock+30+30)),((x_bblock+30+l_bblock),(y_bblock+b_bblock+30+30+30)),((x_bblock+30),
                        (y_bblock+b_bblock+30+30+30)),((x_bblock),(y_bblock+b_bblock+30+30)),((x_bblock+30),(y_bblock+b_bblock+30)),((x_bblock+30),(y_bblock+halfgate)),((x_bblock-30),(y_bblock+halfgate)),
                    ((x_bblock-30),(y_bblock+halfgate-30)),((x_bblock+30),(y_bblock+halfgate-30)),((x_bblock+30),(y_bblock+30)),(x_bblock,y_bblock)],7)

        		#AB Lawn

                pygame.draw.lines(snake_original, BLACK, False, [(x_ab,y_ab),((x_ab+b_ab),(y_ab)),],7)
                pygame.draw.arc(snake_original,(BLACK),(x_ab+b_ab-25,y_ab,50,50),0,pi/2,7)

                pygame.draw.lines(snake_original, BLACK, False, [(x_ab+b_ab+25,y_ab+25),((x_ab+b_ab+25),(y_ab+25+l_ab)),],7)
                pygame.draw.arc(snake_original,(BLACK),(x_ab+b_ab-25,y_ab+l_ab,50,50),3*pi/2,2*pi,7)
         
                pygame.draw.lines(snake_original, BLACK, False, [(x_ab+b_ab,y_ab+l_ab+50),((x_ab),(y_ab+l_ab+50)),],7)
                pygame.draw.arc(snake_original,(BLACK),(x_ab-25,y_ab+l_ab,50,50),pi,3*pi/2,7)
                
                pygame.draw.lines(snake_original, BLACK, False, [(x_ab-25,y_ab+l_ab+25),((x_ab-25),(y_ab+25)),],7)
                pygame.draw.arc(snake_original,(BLACK),(x_ab-25,y_ab,50,50),pi/2,pi,7)

        		#CD Lawn

                pygame.draw.lines(snake_original, BLACK, False, [(x_cd,y_cd),((x_cd+b_cd),(y_cd)),],7)
                pygame.draw.arc(snake_original,(BLACK),(x_cd+b_cd-25,y_cd,50,50),0,pi/2,7)

                pygame.draw.lines(snake_original, BLACK, False, [(x_cd+b_cd+25,y_cd+25),((x_cd+b_cd+25),(y_cd+25+l_cd)),],7)
                pygame.draw.arc(snake_original,(BLACK),(x_cd+b_cd-25,y_cd+l_cd,50,50),3*pi/2,2*pi,7)
         
                pygame.draw.lines(snake_original, BLACK, False, [(x_cd+b_cd,y_cd+l_cd+50),((x_cd),(y_cd+l_cd+50)),],7)
                pygame.draw.arc(snake_original,(BLACK),(x_cd-25,y_cd+l_cd,50,50),pi,3*pi/2,7)
                
                pygame.draw.lines(snake_original, BLACK, False, [(x_cd-25,y_cd+l_cd+25),((x_cd-25),(y_cd+25)),],7)
                pygame.draw.arc(snake_original,(BLACK),(x_cd-25,y_cd,50,50),pi/2,pi,7)


                #D-block
                pygame.draw.lines(snake_original,BLACK, False, [(x_dblock,y_dblock),((x_dblock+30),(y_dblock-30)),((x_dblock+30+l_dblock),(y_dblock-30)),((x_dblock+l_dblock+30+30),
                    (y_dblock)),
                   ((x_dblock+l_dblock+30),(y_dblock+30)),((x_dblock+30+l_dblock),(y_dblock+b_dblock+30)),((x_dblock+30+l_dblock+30),(y_dblock+b_dblock+30+30)),((x_dblock+30+l_dblock),(y_dblock+b_dblock+30+30+30)),((x_dblock+30),
                        (y_dblock+b_dblock+30+30+30)),((x_dblock),(y_dblock+b_dblock+30+30)),((x_dblock+30),(y_dblock+b_dblock+30)),((x_dblock+30),(y_dblock+halfgate)),((x_dblock-30),(y_dblock+halfgate)),
                    ((x_dblock-30),(y_dblock+halfgate-30)),((x_dblock+30),(y_dblock+halfgate-30)),((x_dblock+30),(y_dblock+30)),(x_dblock,y_dblock)],7)
         
                #LAW   

                pygame.draw.arc(snake_original,BLACK,(x_lblock,y_lblock,100,100),pi/2,pi,7)
                pygame.draw.lines(snake_original, BLACK, False, [(x_lblock+50,y_lblock),(x_lblock+250,y_lblock)],7)
                pygame.draw.arc(snake_original,BLACK,(x_lblock+200,y_lblock,100,100),0,pi/2,7)
                pygame.draw.lines(snake_original,BLACK, False, [(x_lblock+300,y_lblock+50),(x_lblock+300,y_lblock+250)],7)
                pygame.draw.arc(snake_original,BLACK,(x_lblock+200,y_lblock+200,100,100),3*pi/2,2*pi,7)
                pygame.draw.lines(snake_original,BLACK, False, [(x_lblock+250,y_lblock+300),(x_lblock+50,y_lblock+300)],7)
                pygame.draw.arc(snake_original,BLACK,(x_lblock,y_lblock+200,100,100),pi,3*pi/2,7)
                pygame.draw.lines(snake_original,BLACK, False, [(x_lblock,y_lblock+250),(x_lblock,y_lblock+50)],7)
                #inside square
                pygame.draw.lines(snake_original,BLACK, False, [(x_lblock+100,y_lblock+100),(x_lblock+200,y_lblock+100),(x_lblock+200,y_lblock+200),(x_lblock+100,y_lblock+200),(x_lblock+100,y_lblock+100)],7)
                #gate
                pygame.draw.lines(snake_original,BLACK, False, [(x_lblock,y_lblock+100),(x_lblock-100,y_lblock+100),(x_lblock-100,y_lblock+125),(x_lblock,y_lblock+125),(x_lblock,y_lblock+175),(x_lblock-100,y_lblock+175),(x_lblock-100,y_lblock+200),(x_lblock,y_lblock+200)],7)
                #steps
                pygame.draw.line(snake_original,BLACK, (x_lblock-10,y_lblock+125),(x_lblock-10,y_lblock+175),7)
                pygame.draw.line(snake_original,BLACK, (x_lblock-20,y_lblock+125),(x_lblock-20,y_lblock+175),7)
                pygame.draw.line(snake_original, BLACK, (x_lblock-30,y_lblock+125),(x_lblock-30,y_lblock+175),7)
                pygame.draw.line(snake_original, BLACK, (x_lblock-40,y_lblock+125),(x_lblock-40,y_lblock+175),7)            
                    
                pygame.draw.line(snake_original,BLACK, (x_lblock-70,y_lblock+125),(x_lblock-70,y_lblock+175),7)            
                pygame.draw.line(snake_original, BLACK, (x_lblock-80,y_lblock+125),(x_lblock-80,y_lblock+175),7)
                pygame.draw.line(snake_original, BLACK, (x_lblock-90,y_lblock+125),(x_lblock-90,y_lblock+175),7)            
                
       
                #Girls Hostel

                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho,y_girlho+72],[x_girlho+25,y_girlho+72-25],[x_girlho+25+10,y_girlho+72-25],[x_girlho+25+10+25,y_girlho+72],[x_girlho+60+15,y_girlho+72],[x_girlho+60+15,y_girlho+72-5],[x_girlho+60+10,y_girlho+72-5]],7)
                pygame.draw.line(snake_original,BLACK,(x_girlho,y_girlho+72),(x_girlho,y_girlho+82),7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho,y_girlho+82],[x_girlho+25,y_girlho+82+25],[x_girlho+25+10,y_girlho+82+25],[x_girlho+25+10+25,y_girlho+82],[x_girlho+60+15,y_girlho+82],[x_girlho+60+15,y_girlho+82+5],[x_girlho+60+10,y_girlho+82+5]],7)
                   
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+60+10,y_girlho+72-5],[x_girlho+60+10,y_girlho+72-5-55],[x_girlho+60+10+20,y_girlho+72-5-55],[x_girlho+60+10+20,y_girlho],[x_girlho+60+10+20+48,y_girlho],[x_girlho+60+10+20+48,y_girlho+12],[x_girlho+60+10+20+48+20,y_girlho+12],[x_girlho+60+10+20+48+20,y_girlho+12+30],[x_girlho+60+10+20+48+20+22,y_girlho+12+30],[x_girlho+60+10+20+48+20+22,y_girlho+12+30-35],[x_girlho+60+10+20+48+20+22+50,y_girlho+12+30-35]],7)        
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+60+10,y_girlho+82+5],[x_girlho+60+10,y_girlho+82+5+55],[x_girlho+60+10+20,y_girlho+82+5+55],[x_girlho+60+10+20,y_girlho+b_girlho],[x_girlho+60+10+20+48,y_girlho+b_girlho],[x_girlho+60+10+20+48,y_girlho+b_girlho-12],[x_girlho+60+10+20+48+20,y_girlho+b_girlho-12],[x_girlho+60+10+20+48+20,y_girlho+b_girlho-12-30],[x_girlho+60+10+20+48+20+20,y_girlho+b_girlho-12-30],[x_girlho+60+10+20+48+20+20,y_girlho+b_girlho-12-30+30],[x_girlho+60+10+20+48+20+20+54,y_girlho+b_girlho-12-30+30]],7)

                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+l_girlho-60-10,y_girlho+72-5],[x_girlho+l_girlho-60-10,y_girlho+72-5-55],[x_girlho+l_girlho-60-10-20,y_girlho+72-5-55],[x_girlho+l_girlho-60-10-20,y_girlho],[x_girlho+l_girlho-60-10-20-48,y_girlho],[x_girlho+l_girlho-60-10-20-48,y_girlho+12],[x_girlho+l_girlho-60-10-20-48-20,y_girlho+12],[x_girlho+l_girlho-60-10-20-48-20,y_girlho+12+30],[x_girlho+l_girlho-60-10-20-48-20-22,y_girlho+12+30],[x_girlho+l_girlho-60-10-20-48-20-22,y_girlho+12+30-35]],7)        
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+l_girlho-60-10,y_girlho+82+5],[x_girlho+l_girlho-60-10,y_girlho+82+5+55],[x_girlho+l_girlho-60-10-20,y_girlho+82+5+55],[x_girlho+l_girlho-60-10-20,y_girlho+b_girlho],[x_girlho+l_girlho-60-10-20-48,y_girlho+b_girlho],[x_girlho+l_girlho-60-10-20-48,y_girlho+b_girlho-12],[x_girlho+l_girlho-60-10-20-48-20,y_girlho+b_girlho-12],[x_girlho+l_girlho-60-10-20-48-20,y_girlho+b_girlho-12-30],[x_girlho+l_girlho-60-10-20-48-20-20,y_girlho+b_girlho-12-30],[x_girlho+l_girlho-60-10-20-48-20-20,y_girlho+b_girlho-12-30+30]],7)

                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+l_girlho,y_girlho+72],[x_girlho+l_girlho-25,y_girlho+72-25],[x_girlho+l_girlho-25-10,y_girlho+72-25],[x_girlho+l_girlho-25-10-25,y_girlho+72],[x_girlho+l_girlho-60-15,y_girlho+72],[x_girlho+l_girlho-60-15,y_girlho+72-5],[x_girlho+l_girlho-60-10,y_girlho+72-5]],7)
                pygame.draw.line(snake_original,BLACK,(x_girlho+l_girlho,y_girlho+72),(x_girlho+l_girlho,y_girlho+82),7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+l_girlho,y_girlho+82],[x_girlho+l_girlho-25,y_girlho+82+25],[x_girlho+l_girlho-25-10,y_girlho+82+25],[x_girlho+l_girlho-25-10-25,y_girlho+82],[x_girlho+l_girlho-60-15,y_girlho+82],[x_girlho+l_girlho-60-15,y_girlho+82+5],[x_girlho+l_girlho-60-10,y_girlho+82+5]],7)
                   
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+60+10+20+48+20+20+3,y_girlho+b_girlho-12-30+30],[x_girlho+60+10+20+48+20+20+3,y_girlho+b_girlho-12-30+30+30],[x_girlho+60+10+20+48+20+20+3-12,y_girlho+b_girlho-12-30+30+30+12]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+l_girlho-60-10-20-48-20-20-3,y_girlho+b_girlho-12-30+30],[x_girlho+l_girlho-60-10-20-48-20-20-3,y_girlho+b_girlho-12-30+30+30],[x_girlho+l_girlho-60-10-20-48-20-20-3+12,y_girlho+b_girlho-12-30+30+30+12]],7)

                #lower stairs
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+60+10+20+48+20+20+3+3,y_girlho+b_girlho-12-30+30],[x_girlho+60+10+20+48+20+20+3+3,y_girlho+b_girlho-12-30+30+30],[x_girlho+60+10+20+48+20+20+3-12+3,y_girlho+b_girlho-12-30+30+30+12]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+l_girlho-60-10-20-48-20-20-3-3,y_girlho+b_girlho-12-30+30],[x_girlho+l_girlho-60-10-20-48-20-20-3-3,y_girlho+b_girlho-12-30+30+30],[x_girlho+l_girlho-60-10-20-48-20-20-3+12-3,y_girlho+b_girlho-12-30+30+30+12]],7)
                    
                    
                pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+20+3-12+3,y_girlho+b_girlho-12-30+30+30+12),(x_girlho+l_girlho-60-10-20-48-20-20-3+12-3,y_girlho+b_girlho-12-30+30+30+12),7)
                  # pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+20+3-12+3+2,y_girlho+b_girlho-12-30+30+30+12-2),(x_girlho+l_girlho-60-10-20-48-20-20-3+12-3-2,y_girlho+b_girlho-12-30+30+30+12-2),7)
                pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+20+3-12+3+4,y_girlho+b_girlho-12-30+30+30+12-4),(x_girlho+l_girlho-60-10-20-48-20-20-3+12-3-4,y_girlho+b_girlho-12-30+30+30+12-4),7)
                  # pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+20+3-12+3+6,y_girlho+b_girlho-12-30+30+30+12-6),(x_girlho+l_girlho-60-10-20-48-20-20-3+12-3-6,y_girlho+b_girlho-12-30+30+30+12-6),7)
                pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+20+3-12+3+8,y_girlho+b_girlho-12-30+30+30+12-8),(x_girlho+l_girlho-60-10-20-48-20-20-3+12-3-8,y_girlho+b_girlho-12-30+30+30+12-8),7)
                  # pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+20+3-12+3+10,y_girlho+b_girlho-12-30+30+30+12-10),(x_girlho+l_girlho-60-10-20-48-20-20-3+12-3-10,y_girlho+b_girlho-12-30+30+30+12-10),7)
                pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+20+3-12+3+12,y_girlho+b_girlho-12-30+30+30+12-12),(x_girlho+l_girlho-60-10-20-48-20-20-3+12-3-12,y_girlho+b_girlho-12-30+30+30+12-12),7)
                  
                #upper stairs
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+60+10+20+48+20+22,y_girlho+12+30-35],[x_girlho+60+10+20+48+20+22,y_girlho+12+30-35-20],[x_girlho+60+10+20+48+20+22+5,y_girlho+12+30-35-20],[x_girlho+60+10+20+48+20+22+15,y_girlho+12+30-35]],7)
                pygame.draw.lines(snake_original,BLACK,False,[[x_girlho+l_girlho-60-10-20-48-20-22,y_girlho+12+30-35],[x_girlho+l_girlho-60-10-20-48-20-22,y_girlho+12+30-35-20],[x_girlho+l_girlho-60-10-20-48-20-22-5,y_girlho+12+30-35-20],[x_girlho+l_girlho-60-10-20-48-20-22-15,y_girlho+12+30-35]],7)

                pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+22+5,y_girlho+12+30-35-20),(x_girlho+l_girlho-60-10-20-48-20-22-5,y_girlho+12+30-35-20),7)
                pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+22+5+3,y_girlho+12+30-35-20+4),(x_girlho+l_girlho-60-10-20-48-20-22-5-3,y_girlho+12+30-35-20+4),7)
                pygame.draw.line(snake_original,BLACK,(x_girlho+60+10+20+48+20+22+5+5,y_girlho+12+30-35-20+8),(x_girlho+l_girlho-60-10-20-48-20-22-5-5,y_girlho+12+30-35-20+8),7)



                #K-Canteen

                #horizontal,
                pygame.draw.line(snake_original,BLACK,(x_kcant+200,y_kcant+270),(x_kcant+360,y_kcant+270),4)

                pygame.draw.line(snake_original,BLACK,(x_kcant+200,y_kcant+50),(x_kcant+360,y_kcant+50),4)
           
                #vertical
                #pygame.draw.line(snake_original,(12,255,200),(115,110),(115,210),4)
                pygame.draw.line(snake_original,BLACK,(x_kcant+445,y_kcant+110),(x_kcant+445,y_kcant+210),4)
               
                pygame.draw.line(snake_original,BLACK,(x_kcant+360,y_kcant+50),(x_kcant+360,y_kcant+70),4)
                pygame.draw.line(snake_original,BLACK,(x_kcant+360,y_kcant+270),(x_kcant+360,y_kcant+250),4)
               
                pygame.draw.line(snake_original,BLACK,(x_kcant+200,y_kcant+50),(x_kcant+200,y_kcant+70),4)
                pygame.draw.line(snake_original,BLACK,(x_kcant+200,y_kcant+270),(x_kcant+200,y_kcant+250),4)
               
                #arcs right top
                pygame.draw.arc(snake_original, BLACK, [x_kcant+328, y_kcant+70, 60, 25],  0, pi / 2,7)
                pygame.draw.arc(snake_original, BLACK, [x_kcant+358, y_kcant+83, 60, 25],  0, pi / 2,7)
                pygame.draw.arc(snake_original, BLACK, [x_kcant+385, y_kcant+97,60, 25],  0, pi / 2,7)
               
                #arcs right bottom
                pygame.draw.arc(snake_original, BLACK, [x_kcant+385, y_kcant+200, 60, 25],   3*pi / 2,2*pi ,7)
                pygame.draw.arc(snake_original, BLACK, [x_kcant+358, y_kcant+212, 60, 25],   3*pi / 2,2*pi,7)
                pygame.draw.arc(snake_original, BLACK, [x_kcant+328, y_kcant+225,60, 25],   3*pi / 2,2*pi,7)
               
                #arcs left bottom
                pygame.draw.arc(snake_original, BLACK, [x_kcant+113, y_kcant+168, 60, 45],   pi,3*pi/2 ,7)
                pygame.draw.arc(snake_original, BLACK, [x_kcant+140, y_kcant+190, 60, 45],   pi,3*pi/2,7)
                pygame.draw.arc(snake_original, BLACK, [x_kcant+170, y_kcant+208,60, 45],   pi,3*pi/2,7)
               
                #arcs left top
                pygame.draw.arc(snake_original, BLACK, [x_kcant+170, y_kcant+68, 60, 45],   pi/2,pi ,7)
                pygame.draw.arc(snake_original, BLACK, [x_kcant+140, y_kcant+90, 60, 45],   pi/2,pi,7)
                pygame.draw.arc(snake_original, BLACK, [x_kcant+114, y_kcant+111,60, 45],   pi/2,pi,7)
               
                #steps
                pygame.draw.line(snake_original,BLACK,(x_kcant+112,y_kcant+140),(x_kcant+112,y_kcant+180),7)
                pygame.draw.line(snake_original,BLACK,(x_kcant+106,y_kcant+140),(x_kcant+106,y_kcant+180),7)
                pygame.draw.line(snake_original,BLACK,(x_kcant+100,y_kcant+140),(x_kcant+100,y_kcant+180),7)
                pygame.draw.line(snake_original,BLACK,(x_kcant+94,y_kcant+140),(x_kcant+94,y_kcant+180),7)

                #step sides
               
                pygame.draw.line(snake_original,BLACK,(x_kcant+116,y_kcant+135),(x_kcant+70,y_kcant+135),4)
                pygame.draw.line(snake_original,BLACK,(x_kcant+116,y_kcant+185),(x_kcant+70,y_kcant+185),4)
         

                #LAW CANTEEN    
                pygame.draw.lines(snake_original, (0,255,0), False, [(x_lcanteen,y_lcanteen),((x_lcanteen+65),(y_lcanteen)),((x_lcanteen+65),(y_lcanteen-20)),((x_lcanteen+100),(y_lcanteen-20)),((x_lcanteen+100),(y_lcanteen)),((x_lcanteen+190),(y_lcanteen)),((x_lcanteen+190),(y_lcanteen+100)),((x_lcanteen),(y_lcanteen+100)),((x_lcanteen),(y_lcanteen))],7)
                pygame.draw.lines(snake_original, (0,255,0), False, [(x_lcanteen+65,y_lcanteen),((x_lcanteen+65),(y_lcanteen+100)),((x_lcanteen+100),(y_lcanteen+100)),((x_lcanteen+100),(y_lcanteen))],7)
                    #outer
                pygame.draw.lines(snake_original, (0,255,255), False, [(x_lcanteen-10,y_lcanteen-10),((x_lcanteen+65-10),(y_lcanteen-10)),((x_lcanteen+65-10),(y_lcanteen-20-10)),((x_lcanteen+100+10),(y_lcanteen-20-10)),((x_lcanteen+100+10),(y_lcanteen-10)),((x_lcanteen+190+10),(y_lcanteen-10)),((x_lcanteen+190+10),(y_lcanteen+100+10)),((x_lcanteen-10),(y_lcanteen+100+10)),((x_lcanteen-10),(y_lcanteen-10))],7)

        		#Robocon Lab
                pygame.draw.lines(snake_original, (0,255,0), True, [(x_robo,y_robo),((x_robo+130),(y_robo+130)),((x_robo+90),(y_robo+200)),((x_robo+130),(y_robo+270)),((x_robo),(y_robo+400)),((x_robo-90),(y_robo+300)),((x_robo-40),(y_robo+260)),((x_robo-90),(y_robo+200)),((x_robo-40),(y_robo+140)),((x_robo-90),(y_robo+100))],7)
                pygame.draw.lines(snake_original, (255,0,255), True, [(x_robo,y_robo-10),((x_robo+130+10),(y_robo+130)),((x_robo+90+10),(y_robo+200)),((x_robo+130+10),(y_robo+270)),((x_robo),(y_robo+400+10)),((x_robo-90-10),(y_robo+300)),((x_robo-40-10),(y_robo+260)),((x_robo-90-10),(y_robo+200)),((x_robo-40-10),(y_robo+140)),((x_robo-90-10),(y_robo+100))],7)


        		#Boys hostel - B
                pygame.draw.lines(snake_original, (0,255,0), False, [(x_boyho,y_boyho),((x_boyho+32),(y_boyho-42)),((x_boyho+27),(y_boyho-47)),((x_boyho+57),(y_boyho-83)),((x_boyho+80),(y_boyho-75)),((x_boyho+90),(y_boyho-95)),((x_boyho+110),(y_boyho-95)),((x_boyho+120),(y_boyho-75)),((x_boyho+140),(y_boyho-83)),((x_boyho+160),(y_boyho-75))],7)
                pygame.draw.lines(snake_original, (0,255,0), False, [((x_boyho+160),(y_boyho-75)),((x_boyho+180),(y_boyho-75)),((x_boyho+200),(y_boyho-83)),((x_boyho+220),(y_boyho-75)),((x_boyho+230),(y_boyho-95)),((x_boyho+250),(y_boyho-95)),((x_boyho+260),(y_boyho-75)),((x_boyho+283),(y_boyho-83)),((x_boyho+313),(y_boyho-47)),((x_boyho+308),(y_boyho-42)),((x_boyho+340),(y_boyho))],7)

                pygame.draw.lines(snake_original, (0,255,0), False, [(x_boyho,y_boyho),((x_boyho+32),(y_boyho+42)),((x_boyho+27),(y_boyho+47)),((x_boyho+57),(y_boyho+83)),((x_boyho+80),(y_boyho+75)),((x_boyho+90),(y_boyho+95)),((x_boyho+110),(y_boyho+95)),((x_boyho+120),(y_boyho+75)),((x_boyho+140),(y_boyho+83)),((x_boyho+160),(y_boyho+75))],7)
                pygame.draw.lines(snake_original, (0,255,0), False, [((x_boyho+160),(y_boyho+75)),((x_boyho+160),(y_boyho+95)),((x_boyho+180),(y_boyho+95)),((x_boyho+180),(y_boyho+75)),((x_boyho+200),(y_boyho+83)),((x_boyho+220),(y_boyho+75)),((x_boyho+230),(y_boyho+95)),((x_boyho+250),(y_boyho+95)),((x_boyho+260),(y_boyho+75)),((x_boyho+283),(y_boyho+83)),((x_boyho+313),(y_boyho+47)),((x_boyho+308),(y_boyho+42)),((x_boyho+340),(y_boyho))],7)

                	#outer
                pygame.draw.lines(snake_original, (BLACK), False, [(x_boyho-10,y_boyho),((x_boyho+32-10),(y_boyho-42)),((x_boyho+27-10),(y_boyho-47)),((x_boyho+57),(y_boyho-83-10)),((x_boyho+80),(y_boyho-75-10)),((x_boyho+90),(y_boyho-95-10)),((x_boyho+110),(y_boyho-95-10)),((x_boyho+120),(y_boyho-75-10)),((x_boyho+140),(y_boyho-83-10)),((x_boyho+160),(y_boyho-75-10))],7)
                pygame.draw.lines(snake_original, (BLACK), False, [((x_boyho+160),(y_boyho-75-10)),((x_boyho+180),(y_boyho-75-10)),((x_boyho+200),(y_boyho-83-10)),((x_boyho+220),(y_boyho-75-10)),((x_boyho+230),(y_boyho-95-10)),((x_boyho+250),(y_boyho-95-10)),((x_boyho+260),(y_boyho-75-10)),((x_boyho+283),(y_boyho-83-10)),((x_boyho+313+10),(y_boyho-47)),((x_boyho+308+10),(y_boyho-42)),((x_boyho+340+10),(y_boyho))],7)

                pygame.draw.lines(snake_original, (BLACK), False, [(x_boyho-10,y_boyho),((x_boyho+32-10),(y_boyho+42)),((x_boyho+27-10),(y_boyho+47)),((x_boyho+57),(y_boyho+83+10)),((x_boyho+80),(y_boyho+75+10)),((x_boyho+90),(y_boyho+95+10)),((x_boyho+110),(y_boyho+95+10)),((x_boyho+120),(y_boyho+75+10)),((x_boyho+140),(y_boyho+83+10)),((x_boyho+160-10),(y_boyho+75+10))],7)
                pygame.draw.lines(snake_original, (BLACK), False, [((x_boyho+160-10),(y_boyho+75+10)),((x_boyho+160-10),(y_boyho+95+10)),((x_boyho+180+10),(y_boyho+95+10)),((x_boyho+180+10),(y_boyho+75+10)),((x_boyho+200),(y_boyho+83+10)),((x_boyho+220),(y_boyho+75+10)),((x_boyho+230),(y_boyho+95+10)),((x_boyho+250),(y_boyho+95+10)),((x_boyho+260),(y_boyho+75+10)),((x_boyho+283),(y_boyho+83+10)),((x_boyho+313+10),(y_boyho+47)),((x_boyho+308+10),(y_boyho+42)),((x_boyho+340+10),(y_boyho))],7)


        		#B-1 Hostel
                pygame.draw.lines(snake_original, (0,255,0), False, [(x_b1,y_b1),((x_b1+130),(y_b1)),((x_b1+130),(y_b1+10)),((x_b1+140),(y_b1+10)),((x_b1+140),(y_b1+40)),((x_b1+130),(y_b1+40)),((x_b1+130),(y_b1+50))
                        ,((x_b1+115),(y_b1+50)),((x_b1+115),(y_b1+70)),((x_b1+40),(y_b1+70)),((x_b1+40),(y_b1+80)),((x_b1+140),(y_b1+80)),((x_b1+140),(y_b1+120)),((x_b1+40),(y_b1+120)),((x_b1+40),(y_b1+130)),
                        ((x_b1+115),(y_b1+130)),((x_b1+115),(y_b1+150)),((x_b1+130),(y_b1+150)),((x_b1+130),(y_b1+160)),((x_b1+140),(y_b1+160)),((x_b1+140),(y_b1+190)),((x_b1+130),(y_b1+190)),((x_b1+130),(y_b1+200))
                        ,((x_b1),(y_b1+200))],7)

                pygame.draw.lines(snake_original, (0,255,0), False, [(x_b1,y_b1),((x_b1),(y_b1+10)),((x_b1-10),(y_b1+10)),((x_b1-10),(y_b1+40)),((x_b1),(y_b1+40)),((x_b1),(y_b1+50)),((x_b1-15),(y_b1+50)),((x_b1-15),
                        (y_b1+60)),((x_b1-25),(y_b1+60)),((x_b1-25),(y_b1+140)),((x_b1-15),(y_b1+140)),((x_b1-15),(y_b1+150)),((x_b1),(y_b1+150)),((x_b1),(y_b1+160)),((x_b1-10),(y_b1+160)),
                    ((x_b1-10),(y_b1+190)),((x_b1),(y_b1+190)),((x_b1),(y_b1+200))],7)

        		#Cricket ground green
                pygame.draw.ellipse(snake_original,red,(x_cric+25,y_cric+23,820,860))
                pygame.draw.ellipse(snake_original,white,(x_cric+23,y_cric+21,825,865),7)
                pygame.draw.ellipse(snake_original,green,(x_cric+50,y_cric+50,770,800))
                pygame.draw.rect(snake_original,(187,177,1),(x_cric+410,y_cric+430,25,90))

        		#Insti.Science
                pygame.draw.polygon(snake_original,white,((x_science+10,y_science+10),(x_science+190,y_science+10),(x_science+190,y_science+70),(x_science+200,y_science+70),(x_science+150,y_science+290),(x_science+10,y_science+290)),7)                 
                                                         #animation triangle



        		
        		#NIM
                pygame.draw.polygon(snake_original,white,((40+x_nim,10+y_nim),(180+x_nim,10+y_nim),(210+x_nim,40+y_nim),(360+x_nim,40+y_nim)
                                                       ,(390+x_nim,10+y_nim),(540+x_nim,10+y_nim),(570+x_nim,40+y_nim),(570+x_nim,190+y_nim),
                                                       (540+x_nim,210+y_nim),(540+x_nim,360+y_nim),
                                                       (570+x_nim,390+y_nim),(570+x_nim,540+y_nim),
                                                       (540+x_nim,570+y_nim),(40+x_nim,570+y_nim),
                                                       (10+x_nim,540+y_nim),(10+x_nim,390+y_nim),
                                                       (40+x_nim,360+y_nim),(40+x_nim,210+y_nim),
                                                       (10+x_nim,190+y_nim),(10+x_nim,40+y_nim)
                                                       ),7)
        		
        		#Pharma
           
                #upperhalf
                pygame.draw.polygon(snake_original,(12,255,200),((x_pharma+200,y_pharma+100),(x_pharma+260,y_pharma+100),(x_pharma+260,y_pharma+130),(x_pharma+310,y_pharma+80),
                                                       (x_pharma+320,y_pharma+90),(x_pharma+310,y_pharma+100),(x_pharma+360,y_pharma+150),(x_pharma+370,y_pharma+140),
                                                       (x_pharma+380,y_pharma+150),(x_pharma+330,y_pharma+200),(x_pharma+330,y_pharma+230),(x_pharma+390,y_pharma+230),
                                                       (x_pharma+390,y_pharma+260),(x_pharma+330,y_pharma+260),(x_pharma+330,y_pharma+290),(x_pharma+380,y_pharma+340),
                                                       (x_pharma+370,y_pharma+350),(x_pharma+360,y_pharma+340),(x_pharma+310,y_pharma+390),(x_pharma+320,y_pharma+400),
                                                       (x_pharma+310,y_pharma+410),
                                                       (x_pharma+300,y_pharma+400),(x_pharma+140,y_pharma+400),
                                                       (x_pharma+130,y_pharma+410),(x_pharma+120,y_pharma+400),(x_pharma+130,y_pharma+390),(x_pharma+80,y_pharma+340),
                                                       (x_pharma+70,y_pharma+350),(x_pharma+60,y_pharma+340),(x_pharma+110,y_pharma+290),(x_pharma+110,y_pharma+260),   
                                                       (x_pharma+50,y_pharma+260),(x_pharma+50,y_pharma+230),(x_pharma+110,y_pharma+230),(x_pharma+110,y_pharma+200),
                                                       (x_pharma+60,y_pharma+150),(x_pharma+70,y_pharma+140),(x_pharma+80,y_pharma+150),(x_pharma+130,y_pharma+100),
                                                       (x_pharma+120,y_pharma+90),(x_pharma+130,y_pharma+80),(x_pharma+180,y_pharma+130),(x_pharma+180,y_pharma+100),
                                                       ),7)  
               #centralpart
                pygame.draw.polygon(snake_original,white,((x_pharma+235,y_pharma+400),(x_pharma+235,y_pharma+440),(x_pharma+305,y_pharma+440),(x_pharma+305,y_pharma+490),
                                                       (x_pharma+235,y_pharma+490),(x_pharma+235,y_pharma+530),(x_pharma+235,y_pharma+530),(x_pharma+205,y_pharma+530),
                                                       (x_pharma+205,y_pharma+490),(x_pharma+135,y_pharma+490),
                                                       (x_pharma+135,y_pharma+440),(x_pharma+205,y_pharma+440),(x_pharma+205,y_pharma+400)
                                                        ),7)

               #lowerhalf
                pygame.draw.polygon(snake_original,white,((x_pharma+235,y_pharma+530),(x_pharma+295,y_pharma+530),(x_pharma+305,y_pharma+520),(x_pharma+315,y_pharma+530),
                                                        (x_pharma+255,y_pharma+590),(x_pharma+220,y_pharma+555),(x_pharma+185,y_pharma+590),(x_pharma+125,y_pharma+530)
                                                         ,(x_pharma+135,y_pharma+520),(x_pharma+145,y_pharma+530),  
                                                        ),7)
                #pharma Canteen
                pygame.draw.polygon(snake_original,white,((x_pcant+10,y_pcant+10),(x_pcant+80,y_pcant+10),(x_pcant+80,y_pcant+210),(x_pcant+10,y_pcant+210),
                                                         
                                                              ),7)                 #animation triangle
                pygame.draw.circle(snake_original,white,(x_pcant+20,y_pcant+225),10,7)
                pygame.draw.circle(snake_original,white,(x_pcant+70,y_pcant+225),10,7)
           
                pygame.draw.rect(snake_original,white,(x_pcant+30,y_pcant+210,30,30),7)

        
        		#football ground color
                pygame.draw.rect(snake_original,green,(x_fg,y_fg-200,b_fg+300,l_fg-100)) 
                pygame.draw.arc(snake_original, (100,150,210), [x_fg-200,y_fg-400,400,400],  3*pi/2, 2*pi,70)
                pygame.draw.circle(snake_original,(100,150,210),(x_fg,y_fg-200),200)
                pygame.draw.rect(snake_original,white,(x_fg+350,y_fg,500,800),4)
                pygame.draw.rect(snake_original,white,(x_fg+500,y_fg,200,100),7)
                pygame.draw.rect(snake_original,white,(x_fg+500,y_fg+700,200,100),7)
                pygame.draw.line(snake_original,white,(x_fg+350,y_fg+400),(x_fg+850,y_fg+400),7)
                pygame.draw.circle(snake_original,white,(x_fg+600,y_fg+400),50,7)   

       		    #Tennis courts
                pygame.draw.rect(snake_original,(64,161,76),(x_ten1,y_ten1,180,390))
                pygame.draw.rect(snake_original,white,(x_ten1,y_ten1,180,390),7)
                pygame.draw.rect(snake_original,white,(x_ten1+22,y_ten1,135,390),7)
                pygame.draw.rect(snake_original,white,(x_ten1+22,y_ten1+90,135,210),7)
                pygame.draw.line(snake_original,white,(x_ten1-5,y_ten1+195),(x_ten1+185,y_ten1+195),7)
                pygame.draw.line(snake_original,white,(x_ten1+90,y_ten1+90),(x_ten1+90,y_ten1+300),7)
                pygame.draw.line(snake_original,white,(x_ten1+90,y_ten1),(x_ten1+90,y_ten1+10),7)
                pygame.draw.line(snake_original,white,(x_ten1+90,y_ten1+390),(x_ten1+90,y_ten1+380),7)

                pygame.draw.rect(snake_original,(64,161,76),(x_ten2,y_ten2,180,390)) 
                pygame.draw.rect(snake_original,white,(x_ten2,y_ten2,180,390),7)
                pygame.draw.rect(snake_original,white,(x_ten2+22,y_ten2,135,390),7)
                pygame.draw.rect(snake_original,white,(x_ten2+22,y_ten2+90,135,210),7)
                pygame.draw.line(snake_original,white,(x_ten2-5,y_ten2+195),(x_ten2+185,y_ten2+195),7)
                pygame.draw.line(snake_original,white,(x_ten2+90,y_ten2+90),(x_ten2+90,y_ten2+300),7)
                pygame.draw.line(snake_original,white,(x_ten2+90,y_ten2),(x_ten2+90,y_ten2+10),7)
                pygame.draw.line(snake_original,white,(x_ten2+90,y_ten2+390),(x_ten2+90,y_ten2+380),7)


                pygame.draw.rect(snake_original,(64,161,76),(x_ten3,y_ten3,180,390)) 
                pygame.draw.rect(snake_original,white,(x_ten3,y_ten3,180,390),7)
                pygame.draw.rect(snake_original,white,(x_ten3+22,y_ten3,135,390),7)
                pygame.draw.rect(snake_original,white,(x_ten3+22,y_ten3+90,135,210),7)
                pygame.draw.line(snake_original,white,(x_ten3-5,y_ten3+195),(x_ten3+185,y_ten3+195),7)
                pygame.draw.line(snake_original,white,(x_ten3+90,y_ten3+90),(x_ten3+90,y_ten3+300),7)
                pygame.draw.line(snake_original,white,(x_ten3+90,y_ten3),(x_ten3+90,y_ten3+10),7)
                pygame.draw.line(snake_original,white,(x_ten3+90,y_ten3+390),(x_ten3+90,y_ten3+380),7)

        		#Basketball court1
                pygame.draw.rect(snake_original,(10,30,50),(x_bask1,y_bask1,180,390)) 

                #Basketball court2
                pygame.draw.rect(snake_original,(10,30,50),(x_bask2,y_bask2,180,390)) 
        		#volley1
                pygame.draw.rect(snake_original,(10,30,50),(x_vol1,y_vol1,180,390)) 
        		#volley2
                pygame.draw.rect(snake_original,(10,30,50),(x_vol2,y_vol2,180,390)) 
        		#Cricket pitch
                pygame.draw.rect(snake_original,(64,161,76),(x_cricpit,y_cricpit+80,50,250))

			    #Outer Boundary
                pygame.draw.rect(snake_original,(0,100,200),(x-100,y-600,5600,3600),10)


		        #Navigate from A Block

                if (200,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("A Block", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))                    

                    print("Block A Selected")
                    if(201,10,10,255)==pixel_dst:
                            print("A and Workshop")
                            col12=0
                            col19=0
                    if(202,10,10,255)==pixel_dst:
                            print("A and PG")
                            col12=0
                            col11_1=0
                            col09=0
                    if(203,10,10,255)==pixel_dst:
                            print("A and D")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col24=0

                    if(204,10,10,255)==pixel_dst:
                            print("A and K")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                    if(205,10,10,255)==pixel_dst:
                            print("A and C")
                            col12=0
                            col10=0
                            col23_1=0
                            col06=0

                    if(206,10,10,255)==pixel_dst:
                            print("A and B")
                            
                            colab=0

                    if(207,10,10,255)==pixel_dst:
                            print("A and LAW")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0

                    if(208,10,10,255)==pixel_dst:
                            print("A and girls hostel")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
#                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38_1=0


                    if(209,10,10,255)==pixel_dst:
                            print("A and law canteen")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0                    



                    if(210,10,10,255)==pixel_dst:
                            print("A and robo lab")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col45=0                                    
                    if(211,10,10,255)==pixel_dst:
                            print("A and boys hos")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0            
                            col44=0                    

                    if(212,10,10,255)==pixel_dst:
                            print("A and b1")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(213,10,10,255)==pixel_dst:
                            print("A and Cric")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                    if(214,10,10,255)==pixel_dst:
                            print("A and NIM")
                            col13=0
                            col15=0
                            col35=0
                            col36=0
                            col59=0
                            col58=0
                    if(215,10,10,255)==pixel_dst:
                            print("A and Pharma")
                            col13=0
                            col15=0
                            col35=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0
                    if(216,10,10,255)==pixel_dst:
                            print("A and Science")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                           
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(217,10,10,255)==pixel_dst:
                            print("A and Courts")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(218,10,10,255)==pixel_dst:
                            print("A and football")
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col33=0

        		#Navigation from Workshop
                if (201,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("W Block", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))                    

                    print("Workshop Selected")
                    if(200,10,10,255)==pixel_dst:
                            print("Workshop and A")
                            col12=0
                            col19=0
                    if(202,10,10,255)==pixel_dst:
                            print("Workshop and PG")
                            col19=0
                            col11_1=0
                            col09=0
                    if(203,10,10,255)==pixel_dst:
                            print("Workshop and D")

                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col24=0

                    if(204,10,10,255)==pixel_dst:
                            print("Workshop and K")

                            col18=0
                            col20_1=0
                            col21=0
                    if(205,10,10,255)==pixel_dst:
                            print("Workshop and C")
                            col19=0
                            col10=0
                            col23_1=0
                            col06=0

                    if(206,10,10,255)==pixel_dst:
                            print("Workshop and B")
                
                            col18=0
                            col17=0

                    if(207,10,10,255)==pixel_dst:
                            print("Workshop and LAW")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0

                    if(208,10,10,255)==pixel_dst:
                            print("Workshop and girls hostel")

                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col31_1=0
                            col38_1=0


                    if(209,10,10,255)==pixel_dst:
                            print("Workshop and law canteen")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0                    



                    if(210,10,10,255)==pixel_dst:
                            print("Workshop and robo lab")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                           
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col45=0                                    
                    if(211,10,10,255)==pixel_dst:

                            print("Workshop and boys hos")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0            
                            col44=0                    

                    if(212,10,10,255)==pixel_dst:
                            print("Workshop and b1")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                           
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(213,10,10,255)==pixel_dst:
                            print("Workshop and Cric")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                    if(214,10,10,255)==pixel_dst:
                            print("Workshop and NIM")
                            col18=0
                            col17=0
                            col16=0
                            col35=0
                            col36=0
                            col59=0
                            col58=0
                    if(215,10,10,255)==pixel_dst:
                            print("Workshop and Pharma")
                            col18=0
                            col17=0
                            col16=0
                            col35=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0
                    if(216,10,10,255)==pixel_dst:
                            print("Workshop and Science")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                           
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(217,10,10,255)==pixel_dst:
                            print("Workshop and Courts")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                           
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(218,10,10,255)==pixel_dst:
                            print("Workshop and football")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            
                            col32=0
                            col31=0
                            col33=0

         
        		#Navigation from PG
                if (202,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("PG Block", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                    
                    print("Block PG Selected")
            	#To D
                    if (203,10,10,255)==pixel_dst:

                            print("PG and D-block both Selected")

                            col08=10
                            col07_1=100
                            col23=100
                            col23_1=100
                            col23_2=100
                            col24=100
            	#To A block
                    if(200,10,10,255)==pixel_dst:
                            print("PG and A-block selected")
                            col09=0
                            col11_1=0
                            col12=0
            	#To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("PG and B block")
                            col19=0
                            col18=0
                            col17=0
                            col09=0
                            col11_1=0
           		#To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("PG and C")
                            col08=0
                            col23_1=0
                            col07_1=0
                            col06=0
            	#To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("PG and K")
                            col08=0
                            col07_1=0
                            col23_2=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col22=0
            	#to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("Pg and Workshop")
                            col09=0
                            col11_1=0
                            col19=0
            	#to                    
                    if(207,10,10,255)==pixel_dst:
                            print("Pg and LAW")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0

                    if(208,10,10,255)==pixel_dst:
                            print("Pg and girls hostel")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38_1=0
                    if(209,10,10,255)==pixel_dst:
                            print("Pg and law canteen")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0
                    if(210,10,10,255)==pixel_dst:
                            print("Pg and robolab")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col41=0
                            col45=0

                    if(211,10,10,255)==pixel_dst:
                            print("Pg and boys hostel")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0
                            col44=0

                    if(212,10,10,255)==pixel_dst:
                            print("Pg and b1 hostel")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0
                            


                    if(213,10,10,255)==pixel_dst:
                            print("Pg and cric")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col41=0
                            col40=0
                    if(214,10,10,255)==pixel_dst:
                            print("Pg and NIM")
                            col09=0
                            col11_1=0
                            col12=0
                            col13=0
                            col15=0
                            col35=0
                            col36=0
                            col59=0
                            col58=0

                    if(215,10,10,255)==pixel_dst:
                            print("Pg and pharma")
                            col09=0
                            col11_1=0
                            col12=0
                            col13=0
                            col15=0
                            col35=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0
                    if(216,10,10,255)==pixel_dst:
                            print("Pg and science")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                          
                    if(217,10,10,255)==pixel_dst:
                            print("Pg and tennis courts")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0

                    if(218,10,10,255)==pixel_dst:
                            print("Pg and football")
                            col09=0
                            col11_1=0
                            col19=0
                            col18=0
                            col20_1=0
                            col20=0


        		#Navigation from D Block

                if (203,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("D Block", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))                    


                    print("D Selected")
                    if(200,10,10,255)==pixel_dst:
                            print("D and A")
                            col24=0
                            col23_2=0
                            col22=0
                            col21=0
                            col20_1=0
                            col18=0
                            col19=0
                            col12=0

                    if(201,10,10,255)==pixel_dst:
                            print("D and Workshop")
                            col24=0
                            col23_2=0
                            col22=0
                            col21=0
                            col20_1=0
                            col18=0


                    if(202,10,10,255)==pixel_dst:
                            print("D and PG")
                            col24=0
                            col23_2=0
                            col23=0
                            col23_1=0
                            col07_1=0
                            col08=0

                    if(204,10,10,255)==pixel_dst:
                            print("D and K")

                            col24=0
                            col23_2=0
                            col22=0
                            
                    if(205,10,10,255)==pixel_dst:
                            print("D and C")
                            colcd=0

                    if(206,10,10,255)==pixel_dst:
                            print("D and B")
                
                            col24=0
                            col23_2=0
                            col22=0
                            col21=0
                            col20_1=0
                            col17=0

                    if(207,10,10,255)==pixel_dst:
                            print("D and LAW")

                            col24=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0

                    if(208,10,10,255)==pixel_dst:
                            print("D and girls hostel")


                            col24=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38_1=0


                    if(209,10,10,255)==pixel_dst:
                            print("D and law canteen")

                            col25=0
                            col28=0
                            col42=0
                            col43=0                    



                    if(210,10,10,255)==pixel_dst:
                            print("D and robo lab")

                            col25=0
                            col28=0
                            col42=0                        
                            col41=0
                            col45=0                                    

                    if(211,10,10,255)==pixel_dst:

                            print("D and boys hos")

                            col25=0
                            col28=0
                            col42=0
                            col43=0            
                            col44=0                    

                    if(212,10,10,255)==pixel_dst:
                            print("D and b1")

                            col25=0
                            col28=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(213,10,10,255)==pixel_dst:
                            print("D and Cric")

                            col25=0
                            col28=0
                            col42=0                        
                            col41=0
                            col40=0
                    if(214,10,10,255)==pixel_dst:
                            print("D and NIM")
                            col24=0
                            col23_2=0
                            col32=0
                            col33=0
                            col34=0
                            col36=0
                            col59=0
                            col58=0
                    if(215,10,10,255)==pixel_dst:
                            print("D and Pharma")
                            col24=0
                            col23_2=0
                            col32=0
                            col33=0
                            col34=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0
                    if(216,10,10,255)==pixel_dst:
                            print("D and Science")

                            col24=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(217,10,10,255)==pixel_dst:
                            print("D and Courts")

                            col24=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(218,10,10,255)==pixel_dst:
                            print("D and football")

                            col24=0
                            col23_2=0
                            col32=0
                            col31=0
                            col33=0
                            

        		#Navigate from K canteen

                if (204,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("K Block", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))                    

                    print("Block K Selected")
                    
                    if(200,10,10,255)==pixel_dst:
                            print("K and A")
                            
                            col21=0
                            col20_1=0
                            col18=0
                            col19=0
                            col12=0


                    if(201,10,10,255)==pixel_dst:
                            print("K and Workshop")
                            col21=0
                            col20_1=0
                            col18=0
                    if(202,10,10,255)==pixel_dst:
                            print("K and PG")
                            col21=0
                            col20_1=0
                            col18=0
                            col19=0
                            col11_1=0
                            col09=0
                    if(203,10,10,255)==pixel_dst:
                            print("K and D")
                            col22=0
                            col23_2=0
                            col24=0
                    if(205,10,10,255)==pixel_dst:
                            print("K and C")
                            col22=0
                            col23_2=0
                            col23=0
                            col23_1=0
                            col06=0

                    if(206,10,10,255)==pixel_dst:
                            print("K and B")
                            
                            col21=0
                            col20_1=0
                            col17=0

                    if(207,10,10,255)==pixel_dst:
                            print("K and LAW")

                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0

                    if(208,10,10,255)==pixel_dst:
                            print("K and girls hostel")
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38_1=0


                    if(209,10,10,255)==pixel_dst:
                            print("K and law canteen")
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0                    



                    if(210,10,10,255)==pixel_dst:
                            print("K and robo lab")
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col45=0                                    
                    if(211,10,10,255)==pixel_dst:
                            print("K and boys hos")
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0            
                            col44=0                    

                    if(212,10,10,255)==pixel_dst:
                            print("K and b1")
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(213,10,10,255)==pixel_dst:
                            print("K and Cric")
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                    if(214,10,10,255)==pixel_dst:
                            print("K and NIM")
                            col21=0
                            col20_1=0
                            col20=0
                            col34=0
                            col36=0
                            col59=0
                            col58=0

                    if(215,10,10,255)==pixel_dst:
                            print("K and Pharma")
                            col21=0
                            col20_1=0
                            col20=0
                            col34=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0
                    if(216,10,10,255)==pixel_dst:
                            print("K and Science")

                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(217,10,10,255)==pixel_dst:
                            print("K and Courts")
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(218,10,10,255)==pixel_dst:
                            print("K and football")
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col33=0

        		#Navigation from C Block
                if (205,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("C Block", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))                    

                    print("C Selected")
                    if(200,10,10,255)==pixel_dst:
                            print("C and A")
                            col06=0
                            col07_1=0
                            col08=0
                            col09=0
                            col11_1=0
                            col12=0

                    if(201,10,10,255)==pixel_dst:
                            print("C and Workshop")
                            col06=0
                            col23_1=0
                            col10=0
                            col19=0


                    if(202,10,10,255)==pixel_dst:
                            print("C and PG")
                            col08=0
                            col07_1=0
                            col23_1=0
                            col06=0
                    if(203,10,10,255)==pixel_dst:
                            print("C and D")

                            colcd=0

                    if(204,10,10,255)==pixel_dst:
                            print("C and K")

                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col22=0

                    if(206,10,10,255)==pixel_dst:
                            print("C and B")
                
                            col06=0
                            col23=0
                            col23_1=0
                            col23_2=0
                            col22=0
                            col21=0
                            col20_1=0
                            col17=0


                    if(207,10,10,255)==pixel_dst:
                            print("C and LAW")
                            
                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0

                    if(208,10,10,255)==pixel_dst:
                            print("C and girls hostel")

                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38_1=0


                    if(209,10,10,255)==pixel_dst:
                            print("C and law canteen")
                            col05=0
                            col26=0
                            col28=0

                            col42=0
                            col43=0                    



                    if(210,10,10,255)==pixel_dst:
                            print("C and robo lab")
                            col05=0
                            col26=0
                            col28=0
                            col42=0                        
                            col41=0
                            col45=0                                    
                    if(211,10,10,255)==pixel_dst:

                            print("C and boys hos")
                            col05=0
                            col26=0
                            col28=0
                            col42=0
                            col43=0            
                            col44=0                    

                    if(212,10,10,255)==pixel_dst:
                            print("C and b1")
                            col05=0
                            col26=0
                            col28=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(213,10,10,255)==pixel_dst:
                            print("C and Cric")
                            col05=0
                            col26=0
                            col28=0
                            col42=0                        
                            col41=0
                            col40=0
                    if(214,10,10,255)==pixel_dst:
                            print("C and NIM")
                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col33=0
                            col34=0
                            col36=0
                            col59=0
                            col58=0


                    if(215,10,10,255)==pixel_dst:
                            print("C and Pharma")
                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col33=0
                            col34=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0
                    if(216,10,10,255)==pixel_dst:
                            print("C and Science")

                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(217,10,10,255)==pixel_dst:
                            print("C and Courts")
                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(218,10,10,255)==pixel_dst:
                            print("C and football")
                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col33=0


        		#Navigate from B Block

                if (206,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("B Block ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))

                    print("Block B Selected")
                    
                    if(200,10,10,255)==pixel_dst:
                            print("B and A")
                            
                            colab=0

                    if(201,10,10,255)==pixel_dst:
                            print("B and Workshop")
                            col17=0
                            col18=0

                    if(202,10,10,255)==pixel_dst:
                            print("B and PG")
                            col17=0
                            col18=0
                            col19=0
                            col11_1=0
                            col09=0
                    if(203,10,10,255)==pixel_dst:
                            print("B and D")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col24=0

                    if(204,10,10,255)==pixel_dst:
                            print("B and K")
                            col17=0
                            col20_1=0
                            col21=0


                    if(205,10,10,255)==pixel_dst:
                            print("B and C")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col23=0
                            col23_1=0
                            col06=0


                    if(207,10,10,255)==pixel_dst:
                            print("B and LAW")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0

                    if(208,10,10,255)==pixel_dst:
                            print("B and girls hostel")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38_1=0


                    if(209,10,10,255)==pixel_dst:
                            print("B and law canteen")
                            col17=0
                            col20_1=0
                            col21=0                    
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0                    



                    if(210,10,10,255)==pixel_dst:
                            print("B and robo lab")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col45=0                                    
                    if(211,10,10,255)==pixel_dst:
                            print("B and boys hos")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0
                            col43=0            
                            col44=0                    

                    if(212,10,10,255)==pixel_dst:
                            print("B and b1")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(213,10,10,255)==pixel_dst:
                            print("B and Cric")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                    if(214,10,10,255)==pixel_dst:
                            print("B and NIM")
                            col16=0
                            col35=0
                            col36=0
                            col59=0
                            col58=0

                    if(215,10,10,255)==pixel_dst:
                            print("B and Pharma")

                            col16=0
                            col35=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0
                    if(216,10,10,255)==pixel_dst:
                            print("B and Science")

                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(217,10,10,255)==pixel_dst:
                            print("B and Courts")
                            col17=0
                            col20_1=0
                            col21=0                    
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col30=0
                            col29=0
                            col42=0                        
                            col41=0
                            col40=0
                            col48=0
                            col47=0                              
                    if(218,10,10,255)==pixel_dst:
                            print("B and football")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col33=0


        #Navigate from NIM Block

                if (214,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("NIM ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))

                    print("Block NIM Selected")
                    
                    if(200,10,10,255)==pixel_dst:
                            print("NIM and A")
                            
                            col13=0
                            col15=0
                            col35=0
                            col36=0
                            col59=0
                            col58=0

                    if(201,10,10,255)==pixel_dst:
                            print("NIM and Workshop")
                            col18=0
                            col17=0
                            col16=0
                            col35=0
                            col36=0
                            col59=0
                            col58=0

                    if(202,10,10,255)==pixel_dst:
                            print("NIM and PG")
                            col09=0
                            col11_1=0
                            col12=0
                            col13=0
                            col15=0
                            col35=0
                            col36=0
                            col59=0
                            col58=0
                    if(203,10,10,255)==pixel_dst:
                            print("NIM and D")
                            col24=0
                            col23_2=0
                            col32=0
                            col33=0
                            col34=0
                            col36=0
                            col59=0
                            col58=0

                    if(204,10,10,255)==pixel_dst:
                            print("NIM and K")
                            col21=0
                            col20_1=0
                            col20=0
                            col34=0
                            col36=0
                            col59=0
                            col58=0


                    if(205,10,10,255)==pixel_dst:
                            print("NIM and C")
                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col33=0
                            col34=0
                            col36=0
                            col59=0
                            col58=0
                    
                    if(206,10,10,255)==pixel_dst:
                            print("NIM and B")
                            col16=0
                            col35=0
                            col36=0
                            col59=0
                            col58=0



                    if(207,10,10,255)==pixel_dst:
                            print("NIM and LAW")
                            col30=0
                            col31_1=0
                            col38=0
                            col37=0
                            col59=0
                            col58=0

                    if(208,10,10,255)==pixel_dst:
                            print("NIM and girls hostel")

                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col58=0



                    if(209,10,10,255)==pixel_dst:
                            print("NIM and law canteen")
                            col39=0
                            col40=0
                            col41=0
                            col43=0                    
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col58=0



                    if(210,10,10,255)==pixel_dst:
                            print("NIM and robo lab")

                            col39=0
                            col40=0
                            col45=0

                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col58=0


                    if(211,10,10,255)==pixel_dst:
                            print("NIM and boys hos")
                            col39=0
                            col40=0
                            col41=0
                            col43=0                    
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col58=0
                            col44=0

                    if(212,10,10,255)==pixel_dst:
                            print("NIM and b1")
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col58=0
                            col39=0
                            col48=0
                            col47=0

                    if(213,10,10,255)==pixel_dst:
                            print("NIM and Cric")
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col58=0
                            col39=0

                    if(215,10,10,255)==pixel_dst:
                            print("NIM and Pharma")

                            col58=0
                            col57=0
                            col56=0

                    if(216,10,10,255)==pixel_dst:
                            print("NIM and Science")

                            col58=0
                            col57=0
                            col55=0
                            col54=0
                            col54_1=0

                            col51=0
                            col52=0
                            col53=0

                    if(217,10,10,255)==pixel_dst:
                            print("NIM and Courts")
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col58=0
                            col39=0
                            col48=0
                            col47=0
                    if(218,10,10,255)==pixel_dst:
                            print("NIM and football")
                            col37=0
                            col59=0
                            col58=0
                            


        #Navigate from Science Block

                if (216,10,10,255)==pixel_src:

                    font = pygame.font.Font(None, 36)
                    text = font.render("Science Insti. ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                    
                    print("Science Selected")
                    
                    if(200,10,10,255)==pixel_dst:
                            print("science and A")
                            
                            col12=0
                            col19=0
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(201,10,10,255)==pixel_dst:
                            print("sci and Workshop")
                            col18=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(202,10,10,255)==pixel_dst:
                            print("sci and PG")
                            col08=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0
                    if(203,10,10,255)==pixel_dst:
                            print("sci and D")

                            col24=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(204,10,10,255)==pixel_dst:
                            print("sci and K")
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0


                    if(205,10,10,255)==pixel_dst:
                            print("sci and C")
                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                    if(206,10,10,255)==pixel_dst:
                            print("sci and B")
                            col17=0
                            col20_1=0
                            col21=0
                            col22=0
                            col23_2=0
                            col32=0
                            col31=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0



                    if(207,10,10,255)==pixel_dst:
                            print("sci and LAW")

                            col30=0
                            col31_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0


                    if(208,10,10,255)==pixel_dst:
                            print("sci and girls hostel")

                            col38_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0



                    if(209,10,10,255)==pixel_dst:
                            print("sci and law canteen")

                            col38_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0


                            col39=0
                            col40=0
                            col41=0
                            col43=0                    



                    if(210,10,10,255)==pixel_dst:
                            print("sci and robo lab")

                            col38_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0


                            col39=0
                            col40=0
                            col45=0



                    if(211,10,10,255)==pixel_dst:
                            print("sci and boys hos")


                            col38_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0

                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col39=0                    

                    if(212,10,10,255)==pixel_dst:
                            print("sci and b1")
                            col38_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0
                            col39=0                    
                            col47=0                    
                            col48=0                    

                    if(213,10,10,255)==pixel_dst:
                            print("sci and Cric")
                            col38_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0
                            col39=0                    

                    if(214,10,10,255)==pixel_dst:
                            print("sci and NIM")


                            col58=0
                            col57=0
                            col55=0
                            col54=0
                            col54_1=0

                            col51=0
                            col52=0
                            col53=0



                    if(215,10,10,255)==pixel_dst:
                            print("sci and Pharma")

                            col55=0
                            col54=0
                            col54_1=0

                            col51=0
                            col52=0
                            col53=0

                    if(217,10,10,255)==pixel_dst:
                            print("sci and Courts")
                            col38_1=0
                            col38=0
                            col49=0
                            col50=0
                            col51=0
                            col52=0
                            col53=0
                            col39=0                    
                            col47=0                    
                            col48=0                    

                    if(218,10,10,255)==pixel_dst:
                            print("sci and football")

                            col51=0
                            col52=0
                            col53=0

                            col50=0
                            col49=0

        #Anshuman's Code
                if (207,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Institute of Law ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                            
                    print("Block PG Selected")
                    #To A
                    if (200,10,10,255)==pixel_dst:

                            print("law and A-block both Selected")

                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("law and D-block selected")
                            col09=0
                            col11_1=0
                            col12=0
            #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("law and B block")
                            
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col17=0
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("law and C")
                            col28=0
                            col29=0
                            col26=0
                            col27=0
                            col05=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("law and K")
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                        
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("law and Workshop")
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                            col18=0
                            col21=0
                            col20_1=0              
                    if(202,10,10,255)==pixel_dst:
                            print("law and pg")
                            col30=0
                            col31=0
                            col32=0
                            col23=0
                            col07_1=0
                            col08=0
                           
                    if(208,10,10,255)==pixel_dst:
                            print("law and girls hostel")
                            col30=0
                            col31=0
                            col31_1=0
                            col38_1=0

                    if(209,10,10,255)==pixel_dst:
                            print("law and law canteen")
                            
                            col29=0
                            col42=0
                            col43=0
                    if(210,10,10,255)==pixel_dst:
                            print("law and robolab")
                            
                            col29=0
                            col42=0
                            col41=0
                            col45=0

                    if(211,10,10,255)==pixel_dst:
                            print("law and boys hostel")
                            
                            col29=0
                            col42=0
                            col43=0
                            col44=0

                    if(212,10,10,255)==pixel_dst:
                            print("law and b1 hostel")
                            
                            col29=0
                            col42=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0
                            


                    if(213,10,10,255)==pixel_dst:
                            print("law and cric")
                            
                            col29=0
                            col42=0
                            col41=0
                            col40=0
                    if(214,10,10,255)==pixel_dst:
                            print("law and NIM")
                            col29=0
                            col42=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0

                    if(215,10,10,255)==pixel_dst:
                            print("law and pharma")
                            col29=0
                            col42=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                    
                    if(216,10,10,255)==pixel_dst:
                            print("law and science")
                            col29=0
                            col42=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0
                            col53=0
                            col55=0
                            col54=0
                            col51=0
                            col52=0

                          
                    if(217,10,10,255)==pixel_dst:
                            print("law and tennis courts")
                            
                            col29=0
                            col42=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0

                    if(218,10,10,255)==pixel_dst:
                            print("law and football")
                            col30=0
                            col31=0
                            col33=0
                                    

                          
                #Navigation from Law Canteen
                if (209,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Canteen de Law ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                            
                    print("Canteen de Law")
                    #To A
                    if (200,10,10,255)==pixel_dst:

                            print("law canteen and A-block both Selected")
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("law canteen and D-block selected")
                            
                            col42=0
                            col43=0
                            col09=0
                            col11_1=0
                            col12=0
            #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("law canteen and B block")
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col17=0
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("law canteen and C")
                            
                            col42=0
                            col43=0
                            col28=0
                            col29=0
                            col26=0
                            col27=0
                            col05=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("law canteen and K")
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                        
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("law canteen and Workshop")
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                            col18=0
                            col21=0
                            col20_1=0              
                    if(202,10,10,255)==pixel_dst:
                            print("law canteen and pg")
                            
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col31=0
                            col32=0
                            col23=0
                            col07_1=0
                            col08=0
                           
                    if(208,10,10,255)==pixel_dst:
                            print("law canteen and girls hostel")
                            col41=0
                            col42=0
                            col43=0
                            col40=0
                            col39=0

                    if(207,10,10,255)==pixel_dst:
                            print("law and law canteen")
                            
                            col29=0
                            col42=0
                            col43=0
                    if(210,10,10,255)==pixel_dst:
                            print("lawcanteen and robolab")
                            
                            
                            col43=0
                            col41=0
                            col45=0

                    if(211,10,10,255)==pixel_dst:
                            print("law canteen and boys hostel")
                            
                            
                            col44=0

                    if(212,10,10,255)==pixel_dst:
                            print("law canteen and b1 hostel")
                            
                            
                            col43=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0
                            


                    if(213,10,10,255)==pixel_dst:
                            print("law canteen and cric")
                            
                            col43=0
                            col41=0
                            col40=0
                    
                    if(214,10,10,255)==pixel_dst:
                            print("law canteen and NIM")
                           
                            
                            col43=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0

                    if(215,10,10,255)==pixel_dst:
                            print("law canteen and pharma")
                            
                            col43=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                    
                    if(216,10,10,255)==pixel_dst:
                            print("law canteen and science")
                            
                            col43=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0
                            col53=0
                            col55=0
                            col54=0
                            col51=0
                            col52=0

                          
                    if(217,10,10,255)==pixel_dst:
                            print("law canteen and tennis courts")
                            col43=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0

                    if(218,10,10,255)==pixel_dst:
                            print("law canteen and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col43=0

                          
        		#Navigation from Boys Hostel
                if (211,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Boys Hostel ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                    
                    print("Boys Hostel")
                    #To A
                    if (200,10,10,255)==pixel_dst:

                            print("Boys Hostel and A-block both Selected")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("Boys Hostel and D-block selected")
                            col44=0
                            col42=0
                            col43=0
                            col09=0
                            col11_1=0
                            col12=0
            #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("Boys Hostel and B block")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col17=0
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("Boys Hostel and C")
                            col44=0
                            col42=0
                            col43=0
                            col28=0
                            col29=0
                            col26=0
                            col27=0
                            col05=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("Boys Hostel and K")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                        
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("Boys Hostel and Workshop")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                            col18=0
                            col21=0
                            col20_1=0              
                    if(202,10,10,255)==pixel_dst:
                            print("Boys Hostel and pg")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col31=0
                            col32=0
                            col23=0
                            col07_1=0
                            col08=0
                           
                    if(208,10,10,255)==pixel_dst:
                            print("Boys Hostel and girls hostel")
                            col44=0
                            col41=0
                            col42=0
                            col43=0
                            col40=0
                            col39=0

                    if(207,10,10,255)==pixel_dst:
                            print("law and boys hostel")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                    if(210,10,10,255)==pixel_dst:
                            print("Boys Hostel and robolab")
                            
                            col44=0
                            col43=0
                            col41=0
                            col45=0

                    if(209,10,10,255)==pixel_dst:
                            print("Boys Hostel and boys hostel")
                            
                            
                            col44=0

                    if(212,10,10,255)==pixel_dst:
                            print("Boys Hostel and b1 hostel")
                                    
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0
                            


                    if(213,10,10,255)==pixel_dst:
                            print("Boys Hostel and cric")
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                    
                    if(214,10,10,255)==pixel_dst:
                            print("Boys Hostel and NIM")
                           
                            col44=0 
                            col43=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0

                    if(215,10,10,255)==pixel_dst:
                            print("Boys Hostel and pharma")
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                    
                    if(216,10,10,255)==pixel_dst:
                            print("Boys Hostel and science")
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0
                            col53=0
                            col55=0
                            col54=0
                            col51=0
                            col52=0

                          
                    if(217,10,10,255)==pixel_dst:
                            print("Boys Hostel and tennis courts")
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0

                    if(218,10,10,255)==pixel_dst:
                            print("Boys Hostel and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col43=0
                            col44=0 

        		#Navigation from Boys Hostel
                if (211,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Boys Hostel ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                    
                    print("Boys Hostel")
                    #To A
                    if (200,10,10,255)==pixel_dst:

                            print("Boys Hostel and A-block both Selected")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("Boys Hostel and D-block selected")
                            col44=0
                            col42=0
                            col43=0
                            col09=0
                            col11_1=0
                            col12=0
            #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("Boys Hostel and B block")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col17=0
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("Boys Hostel and C")
                            col44=0
                            col42=0
                            col43=0
                            col28=0
                            col29=0
                            col26=0
                            col27=0
                            col05=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("Boys Hostel and K")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                        
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("Boys Hostel and Workshop")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                            col18=0
                            col21=0
                            col20_1=0              
                    if(202,10,10,255)==pixel_dst:
                            print("Boys Hostel and pg")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                            col30=0
                            col31=0
                            col32=0
                            col23=0
                            col07_1=0
                            col08=0
                           
                    if(208,10,10,255)==pixel_dst:
                            print("Boys Hostel and girls hostel")
                            col44=0
                            col41=0
                            col43=0
                            col40=0
                            col39=0

                    if(207,10,10,255)==pixel_dst:
                            print("law and boys hostel")
                            col44=0
                            col29=0
                            col42=0
                            col43=0
                    if(210,10,10,255)==pixel_dst:
                            print("Boys Hostel and robolab")
                            
                            col44=0
                            col43=0
                            col41=0
                            col45=0

                    if(209,10,10,255)==pixel_dst:
                            print("Boys Hostel and law canteen")
                            
                            
                            col44=0

                    if(212,10,10,255)==pixel_dst:
                            print("Boys Hostel and b1 hostel")
                            
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0
                            


                    if(213,10,10,255)==pixel_dst:
                            print("Boys Hostel and cric")
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                    
                    if(214,10,10,255)==pixel_dst:
                            print("Boys Hostel and NIM")
                           
                            col44=0 
                            col43=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0

                    if(215,10,10,255)==pixel_dst:
                            print("Boys Hostel and pharma")
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                    
                    if(216,10,10,255)==pixel_dst:
                            print("Boys Hostel and science")
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0
                            col53=0
                            col55=0
                            col54=0
                            col51=0
                            col52=0

                          
                    if(217,10,10,255)==pixel_dst:
                            print("Boys Hostel and tennis courts")
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col47=0
                            col48=0

                    if(218,10,10,255)==pixel_dst:
                            print("Boys Hostel and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col43=0
                            col44=0 
                #Navigation from Robocon
                if (210,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Robocon ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                            
                    print("Robocon")
                #To A
                    if (200,10,10,255)==pixel_dst:

                            print("Robocon and A-block both Selected")
                            col41=0
                            col29=0
                            col42=0
                            col45=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("Robocon and D-block selected")
                            col45=0
                            col42=0
                            col41=0
                            col09=0
                            col11_1=0
                            col12=0
            #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("Robocon and B block")
                            col45=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col17=0
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("Robocon and C")
                            col41=0
                            col42=0
                            col45=0
                            col28=0
                            col29=0
                            col26=0
                            col27=0
                            col05=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("Robocon and K")
                            col41=0
                            col29=0
                            col42=0
                            col45=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                        
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("Robocon and Workshop")
                            col45=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                            col18=0
                            col21=0
                            col20_1=0              
                    if(202,10,10,255)==pixel_dst:
                            print("Robocon and pg")
                            col45=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col32=0
                            col23=0
                            col07_1=0
                            col08=0
                           
                    if(208,10,10,255)==pixel_dst:
                            print("Robocon and girls hostel")
                            
                            col45=0
                            col40=0
                            col39B=0

                    if(207,10,10,255)==pixel_dst:
                            print("law and Robocon")
                            col45=0
                            col29=0
                            col42=0
                            col41=0
                    if(211,10,10,255)==pixel_dst:
                            print("Robocon and Boys Hostel")
                            
                            col44=0
                            col43=0
                            col41=0
                            col45=0

                    if(209,10,10,255)==pixel_dst:
                            print("Robocon and law canteen")
                            
                            col41=0
                            col45=0
                            col43=0

                    if(212,10,10,255)==pixel_dst:
                            print("Robocon and b1 hostel")
                            
                            col45=0
                            col40=0
                            col47=0
                            col48=0
                            


                    if(213,10,10,255)==pixel_dst:
                            print("Robocon and cric")
                            col45=0
                            col40=0
                    
                    if(214,10,10,255)==pixel_dst:
                            print("Robocon and NIM")
                           
                             
                            
                            col45=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0

                    if(215,10,10,255)==pixel_dst:
                            print("Robocon and pharma")
                            
                            
                            col45=0
                            col40=0
                            col39=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                    
                    if(216,10,10,255)==pixel_dst:
                            print("Robocon and science")
                            
                            
                            col45=0
                            col40=0
                            col39=0
                            col38=20
                            col37=0
                            col59=0
                            col53=0
                            col55=0
                            col54=0
                            col51=0
                            col52=0

                          
                    if(217,10,10,255)==pixel_dst:
                            print("Robocon and tennis courts")
                            
                            
                            col45=0
                            col40=0
                            col47=0
                            col48=0

                    if(218,10,10,255)==pixel_dst:
                            print("Robocon and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col45=0
                            col41=0 
       			 #Navigation from Girls Hostel
                if (208,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Girls Hostel ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                    
                    print("Girls Hostel")
            	#To A
                    if (200,10,10,255)==pixel_dst:

                            print("Girls Hostel and A-block both Selected")
                            col39=0
                            col41=0
                            col29=0
                            col42=0
                            col40=0
                            col39B=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("Girls Hostel and D-block selected")
                            
                            col39=0
                            col40=0
                            col39B=0
                            col42=0
                            col41=0
                            col09=0
                            col11_1=0
                            col12=0
            #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("Girls Hostel and B block")
                            col39=0
                            col40=0
                            col39B=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col17=0
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("Girls Hostel and C")
                            col39=0
                            col41=0
                            col42=0
                            col40=0
                            col39B=0
                            col28=0
                            col29=0
                            col26=0
                            col27=0
                            col05=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("Girls Hostel and K")
                            col39=0
                            col41=0
                            col29=0
                            col42=0
                            col40=0
                            col39B=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                        
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("Girls Hostel and Workshop")
                            col39=0
                            col40=0
                            col39B=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                            col18=0
                            col21=0
                            col20_1=0              
                    if(202,10,10,255)==pixel_dst:
                            print("Girls Hostel and pg")
                            col39=0
                            col40=0
                            col39B=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col32=0
                            col23=0
                            col07_1=0
                            col08=0
                           
                    if(210,10,10,255)==pixel_dst:
                            print("Robocon and girls hostel")
                            col39=0
                            col45=0
                            col40=0
                            col39B=0

                    if(207,10,10,255)==pixel_dst:
                            print("law and Girls Hostel")
                            col39=0
                            col40=0
                            col39B=0
                            col29=0
                            col42=0
                            col41=0
                    if(211,10,10,255)==pixel_dst:
                            print("Girls Hostel and Boys Hostel")
                            col39=0
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col39B=0
                            
                    if(209,10,10,255)==pixel_dst:
                            print("Girls Hostel and law canteen")
                            col39=0
                            col41=0
                            col40=0
                            col39B=0
                            col43=0

                    if(212,10,10,255)==pixel_dst:
                            print("Girls Hostel and b1 hostel")
                            
                            
                            col39B=0
                            col47=0
                            col48=0
                            col39=0


                    if(213,10,10,255)==pixel_dst:
                            print("Girls Hostel and cric")
                            
                            col39=0
                            
                    if(214,10,10,255)==pixel_dst:
                            print("Girls Hostel and NIM")
                           
                             
                            
                            col39B=0
                            col38=0
                            col37=0
                            col59=0

                    if(215,10,10,255)==pixel_dst:
                            print("Girls Hostel and pharma")
                            
                            
                            col39B=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                    
                    if(216,10,10,255)==pixel_dst:
                            print("Girls Hostel and science")
                            
                            col39B=0
                            col38=20
                            col37=0
                            col59=0
                            col53=0
                            col55=0
                            col54=0
                            col51=0
                            col52=0

                          
                    if(217,10,10,255)==pixel_dst:
                            print("Girls Hostel and tennis courts")
                            
                            col39B=0
                            col47=0
                            col48=0

                    if(218,10,10,255)==pixel_dst:
                            print("Girls Hostel and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col40=0
                            col41=0
                            col39B=0 

        		#Navigation from Girls Hostel
                if (208,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Girls Hostel ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                    
                    print("Girls Hostel")
                    #To A
                    if (200,10,10,255)==pixel_dst:

                            print("Girls Hostel and A-block both Selected")
                            col39=0
                            col41=0
                            col29=0
                            col42=0
                            col40=0
                            col39B=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("Girls Hostel and D-block selected")
                            
                            col39=0
                            col40=0
                            col39B=0
                            col42=0
                            col41=0
                            col09=0
                            col11_1=0
                            col12=0
            #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("Girls Hostel and B block")
                            col39=0
                            col40=0
                            col39B=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col17=0
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("Girls Hostel and C")
                            col39=0
                            col41=0
                            col42=0
                            col40=0
                            col39B=0
                            col28=0
                            col29=0
                            col26=0
                            col27=0
                            col05=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("Girls Hostel and K")
                            col39=0
                            col41=0
                            col29=0
                            col42=0
                            col40=0
                            col39B=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                        
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("Girls Hostel and Workshop")
                            col39=0
                            col40=0
                            col39B=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                            col18=0
                            col21=0
                            col20_1=0              
                    if(202,10,10,255)==pixel_dst:
                            print("Girls Hostel and pg")
                            col39=0
                            col40=0
                            col39B=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col32=0
                            col23=0
                            col07_1=0
                            col08=0
                           
                    if(210,10,10,255)==pixel_dst:
                            print("Robocon and girls hostel")
                            col39=0
                            col45=0
                            col40=0
                            col39B=0

                    if(207,10,10,255)==pixel_dst:
                            print("law and Girls Hostel")
                            col39=0
                            col40=0
                            col39B=0
                            col29=0
                            col42=0
                            col41=0
                    if(211,10,10,255)==pixel_dst:
                            print("Girls Hostel and Boys Hostel")
                            col39=0
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            col39B=0
                            
                    if(209,10,10,255)==pixel_dst:
                            print("Girls Hostel and law canteen")
                            col39=0
                            col41=0
                            col40=0
                            col39B=0
                            col43=0

                    if(212,10,10,255)==pixel_dst:
                            print("Girls Hostel and b1 hostel")
                            
                            
                            col39B=0
                            col47=0
                            col48=0
                            col39=0


                    if(213,10,10,255)==pixel_dst:
                            print("Girls Hostel and cric")
                            
                            col39=0
                            
                    if(214,10,10,255)==pixel_dst:
                            print("Girls Hostel and NIM")
                           
                             
                            
                            col39B=0
                            col38=0
                            col37=0
                            col59=0

                    if(215,10,10,255)==pixel_dst:
                            print("Girls Hostel and pharma")
                            
                            
                            col39B=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                    
                    if(216,10,10,255)==pixel_dst:
                            print("Girls Hostel and science")
                            
                            col39B=0
                            col38=20
                            col37=0
                            col59=0
                            col53=0
                            col55=0
                            col54=0
                            col51=0
                            col52=0

                          
                    if(217,10,10,255)==pixel_dst:
                            print("Girls Hostel and tennis courts")
                            
                            col39B=0
                            col47=0
                            col48=0

                    if(218,10,10,255)==pixel_dst:
                            print("Girls Hostel and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col40=0
                            col41=0
                            col39B=0 
        		#Navigation from Cricket Ground
                if (213,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Cricket Ground ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                    
                    print("Cricket Ground")
            	#To A
                    if (200,10,10,255)==pixel_dst:

                            print("Cricket Ground and A-block both Selected")
                            col41=0
                            col29=0
                            col42=0
                            col40=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("Cricket Ground and D-block selected")
                            
                            col40=0
                            col42=0
                            col41=0
                            col09=0
                            col11_1=0
                            col12=0
            #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("Cricket Ground and B block")
                            col40=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col17=0
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("Cricket Ground and C")
                            col41=0
                            col42=0
                            col40=0
                            col28=0
                            col29=0
                            col26=0
                            col27=0
                            col05=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("Cricket Ground and K")
                            col41=0
                            col29=0
                            col42=0
                            col40=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                        
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("Cricket Ground and Workshop")
                            col40=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                            col18=0
                            col21=0
                            col20_1=0              
                    if(202,10,10,255)==pixel_dst:
                            print("Cricket Ground and pg")
                            col40=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col32=0
                            col23=0
                            col07_1=0
                            col08=0
                           
                    if(210,10,10,255)==pixel_dst:
                            print("Robocon and Cricket Ground")
                            col39=0
                            col45=0
                            col40=0
                            
                    if(207,10,10,255)==pixel_dst:
                            print("Cricket Ground and Law")
                            
                            col40=0
                            col29=0
                            col42=0
                            col41=0
                    if(211,10,10,255)==pixel_dst:
                            print("Cricket Ground and Boys Hostel")
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            
                    if(209,10,10,255)==pixel_dst:
                            print("Cricket Ground and law canteen")
                            col41=0
                            col40=0
                            col43=0

                    if(212,10,10,255)==pixel_dst:
                            print("Cricket Ground and b1 hostel")
                            
                            
                            
                            col47=0
                            col48=0
                            


                    if(208,10,10,255)==pixel_dst:
                            print("Girls Hostel and cric")
                            
                            col39=0
                            
                    if(214,10,10,255)==pixel_dst:
                            print("Cricket Ground and NIM")
                           
                            col39=0 
                            col39B=0
                            col38=0
                            col37=0
                            col59=0

                    if(215,10,10,255)==pixel_dst:
                            print("Cricket Ground and pharma")
                            col39=0
                            col39B=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                    
                    if(216,10,10,255)==pixel_dst:
                            print("Cricket Ground and science")
                            col39=0
                            col39B=0
                            col38=20
                            col37=0
                            col59=0
                            col53=0
                            col55=0
                            col54=0
                            col51=0
                            col52=0

                          
                    if(217,10,10,255)==pixel_dst:
                            print("Cricket Ground and tennis courts")
                            
                            col48=0
                            col49=0

                    if(218,10,10,255)==pixel_dst:
                            print("Cricket Ground and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col40=0
                            col41=0
        		#Navigation from Tennis
                if (217,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Cricket Ground ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))
                    
                    print("Cricket Ground")
            	#To A
                    if (200,10,10,255)==pixel_dst:

                            print("Tennis and A-block both Selected")
                            col48=0
                            col49=0
                            col41=0
                            col29=0
                            col42=0
                            col40=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("Tennis and D-block selected")
                            col48=0
                            col49=0
                            col40=0
                            col42=0
                            col41=0
                            col09=0
                            col11_1=0
                            col12=0
            #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("Tennis and B block")
                            col48=0
                            col49=0
                            col40=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col32_1=0
                            col33=0
                            col20_1=0
                            col20=0
                            col17=0
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("Tennis and C")
                            col48=0
                            col49=0
                            col41=0
                            col42=0
                            col40=0
                            col28=0
                            col29=0
                            col26=0
                            col27=0
                            col05=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("Tennis and K")
                            col48=0
                            col49=0
                            col41=0
                            col29=0
                            col42=0
                            col40=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                        
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("Tennis and Workshop")
                            col48=0
                            col49=0
                            col40=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col22=0
                            col32=0
                            col18=0
                            col21=0
                            col20_1=0              
                    if(202,10,10,255)==pixel_dst:
                            print("Tennis and pg")
                            col40=0
                            col29=0
                            col42=0
                            col41=0
                            col30=0
                            col31=0
                            col32=0
                            col23=0
                            col07_1=0
                            col08=0
                            col48=0
                            col49=0
                    if(210,10,10,255)==pixel_dst:
                            print("Robocon and Tennis")
                            col39=0
                            col45=0
                            col40=0
                            col48=0
                            col49=0
                    if(207,10,10,255)==pixel_dst:
                            print("Tennis and Law")
                            col48=0
                            col49=0
                            col40=0
                            col29=0
                            col42=0
                            col41=0
                    if(211,10,10,255)==pixel_dst:
                            print("Tennis and Boys Hostel")
                            col48=0
                            col49=0
                            col44=0
                            col43=0
                            col41=0
                            col40=0
                            
                    if(209,10,10,255)==pixel_dst:
                            print("Tennis and law canteen")
                            col41=0
                            col40=0
                            col43=0
                            col48=0
                            col49=0
                    


                    if(208,10,10,255)==pixel_dst:
                            print("Tennis and Girls Hostel")
                            
                            col39=0
                            col48=0
                            col49=0
                    if(214,10,10,255)==pixel_dst:
                            print("Tennis Ground and NIM")
                            col48=0
                            col49=0
                            col39=0 
                            col39B=0
                            col38=0
                            col37=0
                            col59=0

                    if(215,10,10,255)==pixel_dst:
                            print("Tennis Ground and pharma")
                            col39=0
                            col39B=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                            col48=0
                            col49=0
                    
                    if(216,10,10,255)==pixel_dst:
                            print("Tennis Ground and science")
                            col39=0
                            col39B=0
                            col38=20
                            col37=0
                            col59=0
                            col53=0
                            col55=0
                            col54=0
                            col51=0
                            col52=0
                            col48=0
                            col49=0

                          
                    if(213,10,10,255)==pixel_dst:
                            print("Tennis and Cricket Ground")
                            
                            col48=0
                            col49=0

                    if(218,10,10,255)==pixel_dst:
                            print("Tennis and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col40=0
                            col41=0
                            col48=0
                            col49=0

                if (218,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("football ", 1, (255,255,255))
                    screen.blit(text, (x_src,y_src))
                    
                    print("football")            
                    if(217,10,10,255)==pixel_dst:
                            print("football and tennis")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col40=0
                            col41=0
                            col48=0
                            col49=0
            
                    if(213,10,10,255)==pixel_dst:
                            print("Cricket Ground and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col40=0
                            col41=0       

                    if(208,10,10,255)==pixel_dst:
                            print("Girls hostel and football")
                            col30=0
                            col31=0
                            col33=0
                            col29=0
                            col42=0
                            col40=0
                            col41=0       
                            col39=0
         
                    if (200,10,10,255)==pixel_dst:

                            print("football and A-block both Selected")
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col12=0
            #To D block
                    if(203,10,10,255)==pixel_dst:
                            print("football and D-block selected")
                            col33=0
                            col32=0
                            col24=0
                                #To B Block
                    if(206,10,10,255)==pixel_dst:
                            print("football and B block")
                            col20_1=0
                            col20=0
                            col17=0
                            
                            
            #To C-block
                    if(205,10,10,255)==pixel_dst:
                            print("football and C")
                            col33=0
                            col32=0
                            col23=0
                            col06=0
            #To Kcanteen
                    if(204,10,10,255)==pixel_dst:
                            print("football and K")
                            col21=0
                            col20=0
                            
            #to workshop
                    if(201,10,10,255)==pixel_dst:
                            print("football and Workshop")
                            col20_1=0
                            col20=0
                            col18=0
                    if(202,10,10,255)==pixel_dst:
                            print("football and pg")
                            col20_1=0
                            col20=0
                            col18=0
                            col19=0
                            col11_1=0
                            col09=0
                            
                    if(210,10,10,255)==pixel_dst:
                            print("football and Robocon")
                            col33=0
                            col31=0
                            col30=0
                            col41=0
                            col42=0
                            col29=0
                            col45=0
                    if(207,10,10,255)==pixel_dst:
                            print("football and Law")
                            col33=0
                            col31=0
                            col30=0

                    if(211,10,10,255)==pixel_dst:
                            print("football and Boys Hostel")
                            col33=0
                            col31=0
                            col30=0
                            col43=0
                            col42=0
                            col29=0
                            col44=0

                    if(209,10,10,255)==pixel_dst:
                            print("football and law canteen")
                            col33=0
                            col31=0
                            col30=0
                            col43=0
                            col42=0
                            col29=0

                    
                    if(214,10,10,255)==pixel_dst:
                            print("football and NIM")
                            col34=0
                            col36=0
                            col59=0 
                            
                    if(215,10,10,255)==pixel_dst:
                            print("football and pharma")
                            col34=0
                            col36=0
                            col59=0 
                            col56=0
                            col57=0

                    if(216,10,10,255)==pixel_dst:
                            print("football and science")
                            col34=0
                            col36=0
                            col59=0 
                            col55=0
                            col54=0
                            col51=0
                            col52=0                    

        #Pharma navigate
                if (215,10,10,255)==pixel_src:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Pharma ", 1, (0,255,0))
                    screen.blit(text, (x_src,y_src))

                    print("Block Pharma Selected")
                            
                    if(200,10,10,255)==pixel_dst:
                            print("Pharma and A")
                            
                            col13=0
                            col15=0
                            col35=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0

                    if(201,10,10,255)==pixel_dst:
                            print("Pharma and Workshop")
                            col18=0
                            col17=0
                            col16=0
                            col35=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0

                    if(202,10,10,255)==pixel_dst:
                            print("Pharma and PG")
                            col09=0
                            col11_1=0
                            col12=0
                            col13=0
                            col15=0
                            col35=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0

                    if(203,10,10,255)==pixel_dst:
                            print("Pharma and D")
                            col24=0
                            col23_2=0
                            col32=0
                            col33=0
                            col34=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0

                    if(204,10,10,255)==pixel_dst:
                            print("Pharma and K")
                            col21=0
                            col20_1=0
                            col20=0
                            col34=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0


                    if(205,10,10,255)==pixel_dst:
                            print("Pharma and C")
                            col06=0
                            col23_1=0
                            col23=0
                            col23_2=0
                            col32=0
                            col33=0
                            col34=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0

                    if(206,10,10,255)==pixel_dst:
                            print("Pharma and B")
                            col16=0
                            col35=0
                            col36=0
                            col59=0
                            col57=0
                            col56=0



                    if(207,10,10,255)==pixel_dst:
                            print("Pharma and LAW")
                            col30=0
                            col31_1=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0

                    if(208,10,10,255)==pixel_dst:
                            print("Pharma and girls hostel")

                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0



                    if(209,10,10,255)==pixel_dst:
                            print("Pharma and law canteen")
                            col39=0
                            col40=0
                            col41=0
                            col43=0                    
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0



                    if(210,10,10,255)==pixel_dst:
                            print("Pharma and robo lab")

                            col39=0
                            col40=0
                            col45=0

                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0


                    if(211,10,10,255)==pixel_dst:
                            print("Pharma and boys hos")
                            col39=0
                            col40=0
                            col41=0
                            col43=0                    
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                            col44=0

                    if(212,10,10,255)==pixel_dst:
                            print("Pharma and b1")
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                            col39=0
                            col48=0
                            col47=0

                    if(213,10,10,255)==pixel_dst:
                            print("Pharma and Cric")
                            
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col57=0
                            col56=0
                            col39=0

                    if(214,10,10,255)==pixel_dst:
                            print("Pharma and NIM")

                            col58=0
                            col57=0
                            col56=0

                    if(216,10,10,255)==pixel_dst:
                            print("Pharma and Science")

                            col56=0
                            col55=0
                            col54=0
                            col54_1=0
                            col51=0
                            col52=0
                            col53=0

                    if(217,10,10,255)==pixel_dst:
                            print("Pharma and Courts")
                            
                            col38_1=0
                            col38=0
                            col37=0
                            col59=0
                            col58=0
                            col39=0
                            col48=0
                            col47=0
                            col57=0
                            col56=0

                    if(218,10,10,255)==pixel_dst:
                            print("Pharma and football")
                            
                            col37=0
                            col59=0
                            col58=0
                            col57=0
                            col56=0



        



                
                #----------------------------------------------------------------------

                #-----------------------------ROADS ------------------------------

                pygame.draw.rect(snake_original,(col04,col04,0),(x_4,y_4,610,40))

                pygame.draw.rect(snake_original,(col26,col26,0),(x_26-290,y_26,300,40))
                pygame.draw.rect(snake_original,(col28,col28,0),(x_28,y_28,590,40))        

                pygame.draw.rect(snake_original,(col05,col05,0),(x_5+100,y_5+40,40,235))
                pygame.draw.rect(snake_original,(col06,col06,0),(x_6+100,y_6-40,40,245))

                pygame.draw.rect(snake_original,(col08,col08,0),(x_8,y_8,40,185))
                pygame.draw.rect(snake_original,(col09,col09,0),(x_9,y_9,40,315))

                pygame.draw.rect(snake_original,(col11,col11,0),(x_11-40,y_11,440,40))
                pygame.draw.rect(snake_original,(col11_1,col11_1,0),(x_11_1-40,y_11_1,160,40))
                

                pygame.draw.rect(snake_original,(col13,col13,0),(x_13+25,y_13-30,40,300))
                pygame.draw.rect(snake_original,(col12,col12,0),(x_12+25,y_12+60,40,300)) 
                
                
                pygame.draw.rect(snake_original,(col10,col10,0),(x_10+70,y_10,40,450))

                pygame.draw.rect(snake_original,(col16,col16,0),(x_16,y_16-30,40,300))
                pygame.draw.rect(snake_original,(col17,col17,0),(x_17,y_17+60,40,300)) 

                pygame.draw.rect(snake_original,(col19,col19,0),(x_19+50,y_19,180,40))
                pygame.draw.rect(snake_original,(col18,col18,0),(x_18+70,y_18,160,40))
                
                pygame.draw.rect(snake_original,(col20,col20,0),(x_20-30,y_20,530,40))
                pygame.draw.rect(snake_original,(col20_1,col20_1,0),(x_20_1-30,y_20_1,70,40))
         
                pygame.draw.rect(snake_original,(col21,col21,0),(x_21+70,y_21-30,40,220))
                pygame.draw.rect(snake_original,(col22,col22,0),(x_22+70,y_22,40,220))
                
                
                pygame.draw.rect(snake_original,(col23_1,col23_1,0),(x_23_1+110,y_23_1,90,40))
                pygame.draw.rect(snake_original,(col23,col23,0),(x_23+10,y_23,260,40))
                pygame.draw.rect(snake_original,(col23_2,col23_2,0),(x_23_2+270,y_23_2,120,40))        

                pygame.draw.rect(snake_original,(col29,col29,0),(x_29+120,y_29-100,40,240))        

                pygame.draw.rect(snake_original,(col32,col32,0),(x_32+90,y_32,b_ab+300,40))        
                pygame.draw.rect(snake_original,(col31,col31,0),(x_31+90,y_31,40,110))        
                pygame.draw.rect(snake_original,(col31_1,col31_1,0),(x_31_1+90,y_31_1,l_fg+120,40))        

                pygame.draw.rect(snake_original,(col34,col34,0),(x_34+120,y_34,40,550))        
                pygame.draw.rect(snake_original,(col33,col33,0),(x_33+90,y_33-110,40,500))


                pygame.draw.rect(snake_original,(col30,col30,0),(x_30+90,y_30,40,210))


                pygame.draw.rect(snake_original,(col24,col24,0),(x_24,y_24+40,40,280))
                pygame.draw.rect(snake_original,(col25,col25,0),(x_25,y_25+80,40,240))

        
                pygame.draw.rect(snake_original,(col07_1,col07_1,0),(x_7_1-10,y_7_1,130,40))
                pygame.draw.rect(snake_original,(col07,col07,0),(x_7-40,y_7,440,40))

                        
                pygame.draw.rect(snake_original,(col14,col14,0),(x_14-60,y_14,600,40))
                
                pygame.draw.rect(snake_original,(col15,col15,0),(x_15-10,y_15,380,40))
                pygame.draw.rect(snake_original,(col35,col35,0),(x_35,y_35,600,40))
               
                pygame.draw.rect(snake_original,(col36,col36,0),(x_36,y_36,1260,40))

                pygame.draw.rect(snake_original,(col59,col59,0),(x_59+20,y_59,400,40))

                pygame.draw.rect(snake_original,(col57,col57,0),(x_57+20,y_57,400,40))

                pygame.draw.rect(snake_original,(col56,col56,0),(x_56+20,y_56,340,40))
                pygame.draw.rect(snake_original,(col56,col56,0),(x_56+360,y_56,340,40))
                
        
                pygame.draw.rect(snake_original,(col38,col38,0),(x_38+200,y_38,40,480))
                pygame.draw.rect(snake_original,(col38_1,col38_1,0),(x_38_1+200,y_38_1+40,40,120))

                pygame.draw.rect(snake_original,(col37,col37,0),(x_37+200,y_37,40,920))

                pygame.draw.rect(snake_original,(col49,col49,0),(x_49+200,y_49,450,40))
                pygame.draw.rect(snake_original,(col50,col50,0),(x_50+200,y_50,450,40))

                pygame.draw.rect(snake_original,(col53,col53,0),(x_53-50,y_53+100,40,240))

                pygame.draw.rect(snake_original,(col52,col52,0),(x_52-50,y_52,40,240))

                pygame.draw.rect(snake_original,(col54,col54,0),(x_54-50,y_54+50,40,150))
                pygame.draw.rect(snake_original,(col54_1,col54_1,0),(x_54_1-50,y_54_1+50,150,40))

                pygame.draw.rect(snake_original,(col55,col55,0),(x_55-50,y_55+80,40,690))
                
                pygame.draw.rect(snake_original,(col39,col39,0),(x_39+200,y_39+80,40,270))  

                pygame.draw.rect(snake_original,(col48,col48,0),(x_48+200,y_48+80,40,270))  
                pygame.draw.rect(snake_original,(col47,col47,0),(x_47+200,y_47+80,40,970))          

                pygame.draw.rect(snake_original,(col42,col42,0),(x_42,y_42,340,40))  
                
                pygame.draw.rect(snake_original,(col41,col41,0),(x_41,y_41,400,40))  
                
                pygame.draw.rect(snake_original,(col40,col40,0),(x_40,y_40,760,40))  

                pygame.draw.rect(snake_original,(col60,col60,0),(x_60,y_60-200,40,700))        
                 
                pygame.draw.rect(snake_original,(col45,col45,0),(x_45,y_45,40,200))
                
                pygame.draw.rect(snake_original,(col45_1,col45_1,0),(x_45_1,y_45_1,150,40))

                pygame.draw.rect(snake_original,(col46,col46,0),(x_46,y_46,40,400))
                
                pygame.draw.rect(snake_original,(col46_1,col46_1,0),(x_46_1,y_46_1,150,40))
                
                pygame.draw.rect(snake_original,(col43,col43,0),(x_43-40,y_43,40,200))
                
                pygame.draw.rect(snake_original,(col44,col44,0),(x_44-40,y_44,40,200))
                
                pygame.draw.rect(snake_original,(colab,colab,0),(x_ab1-50,y_ab1+100,b_ab+100,40))
                pygame.draw.rect(snake_original,(colcd,colcd,0),(x_cd1-30,y_cd1+100,b_ab+60,40))

                #-----------------------------hotspots-----------------------------
        		
        		#A        
                pygame.draw.circle(snake_original,(200,10,10),(x_12-50,y_12+30),20)
         		
         		#workshop 
                pygame.draw.circle(snake_original,(201,10,10),(x_12+190,y_12+390),20)

         		#pg       
                pygame.draw.circle(snake_original,(202,10,10),(x_pg+l_pg-200,y_pg+b_pg-100),20)
            	
            	#d
                pygame.draw.circle(snake_original,(203,10,10),(x_dblock+200,y_dblock+200),20)
           		
           		#k
                pygame.draw.circle(snake_original,(204,10,10),(x_kcant+100,y_kcant+100),20)
        		
        		#c block
                pygame.draw.circle(snake_original,(205,10,10),(x_cblock+100,y_cblock+100),20)
        		
        		#b
                pygame.draw.circle(snake_original,(206,10,10),(x_bblock+200,y_bblock+200),20)  
        		
        		#law block
                pygame.draw.circle(snake_original,(207,10,10),(x_lblock+150,y_lblock+150),20)  
        		
        		#girls hostel
                pygame.draw.circle(snake_original,(208,10,10),(x_girlho+200,y_girlho+100),20)  
        		
        		#law canteen
                pygame.draw.circle(snake_original,(209,10,10),(x_lcanteen+100,y_lcanteen+100),20)
        		
        		#robolab        
                pygame.draw.circle(snake_original,(210,10,10),(x_robo,y_robo+200),20)  
        		
        		#boys hostel B
                pygame.draw.circle(snake_original,(211,10,10),(x_boyho+200,y_boyho+50),20)
        		
        		#b1 hostel
                pygame.draw.circle(snake_original,(212,10,10),(x_b1+100,y_b1+100),20)
        		
        		#cric ground
                pygame.draw.circle(snake_original,(213,10,10),(x_cric+150,y_cric+500),20)  
       			
       			#nim
                pygame.draw.circle(snake_original,(214,10,10),(x_nim+300,y_nim+150),20)  
        		
        		#pharma
                pygame.draw.circle(snake_original,(215,10,10),(x_pharma+250,y_pharma+150),20)  
        		
        		#science
                pygame.draw.circle(snake_original,(216,10,10),(x_science+50,y_science+180),20)  
        		
        		#courts
                pygame.draw.circle(snake_original,(217,10,10),(x_ten1+100,y_ten1-50),20)  
        		
        		#footballground
                pygame.draw.circle(snake_original,(218,10,10),(x_fg+50,y_fg+400),20) 
        


        #-----------------------------------------------------------------------------------------------------------------------------------------------        
        


                snake = pygame.transform.rotozoom(snake_original, angle, zoom)
                newrect = snake.get_rect() # store new surface rect
                # put new surface rect center on same spot as old surface rect center
                snakex += oldrect.centerx - newrect.centerx
                snakey += oldrect.centery - newrect.centery
            # paint the snake    
            compass=pygame.image.load("compass.png")
            nirma=pygame.image.load("nirma_1.jpg")        

            screen.blit(snake, (round(snakex,0)-2250, round(snakey,0)-1750))    
            screen.blit(compass,(x_compass,y_compass))
            screen.blit(nirma,(x_compass+300,y_compass))


            pygame.display.flip()


if __name__=='__main__':
       
    screen=pygame.display.set_mode((1240,600))
    Game().main(screen)
