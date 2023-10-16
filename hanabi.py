import sys
import random
import cv2
import numpy as np
import pygame
 

def main(): # メイン

    #img_bg = pygame.image.load('image/IMG_0558.png')   
    #img_char= pygame.image.load('image/IMG_0557.png')                             # -1はAlphaを含んだ形式(0:グレー, 1:カラー)

    img_bg = [ pygame.image.load('image/IMG_0590.png'),  pygame.image.load('image/IMG_0596.png'), 
              pygame.image.load('image/IMG_0613.png') , pygame.image.load('image/IMG_0580.png') ]  
    img_char = [ pygame.image.load('image/IMG_0591.png'),  pygame.image.load('image/IMG_0597.png'),   
                pygame.image.load('image/IMG_0614.png') , pygame.image.load('image/IMG_0575.png') ]  
    img_hanabi = [ pygame.image.load('image/IMG_0592.png'),  pygame.image.load('image/IMG_0598.png'),   
               pygame.image.load('image/IMG_0615.png') , pygame.image.load('image/IMG_0587.png') ]  
    img_koukaon = [ pygame.image.load('image/IMG_0593.png'),  pygame.image.load('image/IMG_0599.png'),   
              pygame.image.load('image/IMG_0615.png') , pygame.image.load('image/IMG_0581.png') ]  
    
    img_fukidashi_1 = [ pygame.image.load('image/IMG_05941.png'),  pygame.image.load('image/IMG_05942.png'),   
              pygame.image.load('image/IMG_05943.png') , pygame.image.load('image/IMG_05944.png') ,
              pygame.image.load('image/IMG_0594.png') ]  
    img_fukidashi_2 = [ pygame.image.load('image/IMG_06001.png'),  pygame.image.load('image/IMG_06002.png'),   
              pygame.image.load('image/IMG_0600.png') ] 
    img_fukidashi_3 = [ pygame.image.load('image/IMG_0617.png') ] 
    img_alice_dekimashita = pygame.image.load('image/IMG_06141.png')
    img_sensei_te = pygame.image.load("image/IMG_06142.png")
    tmr = 0

    scene = 1
    ac = 100
    sc = 1.0
    

    pygame.init()
    pygame.display.set_caption("アリスの花火")
    screen = pygame.display.set_mode((1280, 980))
    #フォントの用意
    font1 = pygame.font.SysFont('meiryo', 40)   
    clock = pygame.time.Clock()

    while True:
#        screen.fill((0,0,0))

        tmr = tmr +1 

        #ゲームスタートからの経過時間でのイベントを記述
        
#       if scene == 1:
        if tmr <= 30:
                screen.blit(img_bg[0], [0,0])
                #このシーンの動きの初期化
                ac=100
                atemp=0
                ttmr=0
                i = 0     
                j = 0
        elif tmr <= 120:
                atemp= ac*ttmr 
                screen.blit(img_bg[0], [0,0])
                screen.blit(img_char[0], [0, 800-atemp]) 
                
                if ttmr < 19: 
                    ttmr=ttmr +1
                    ac= ac -3
                if tmr >=60:
                    if tmr <70:
                        screen.blit(img_fukidashi_1[0], [0,0])
                    elif tmr <90:
                        screen.blit(img_fukidashi_1[1], [0,0])
                    elif tmr <105:
                        screen.blit(img_fukidashi_1[2], [0,0])
                    else:
                        screen.blit(img_fukidashi_1[3], [0,0])                    
                    
   
        elif tmr < 150:
                screen.blit(img_bg[0], [0,0])
                screen.blit(img_char[0], [0, 800-atemp])     
                screen.blit(img_fukidashi_1[4], [0,0])


#       if scene == 2:
        elif tmr == 150:
                #このシーンの動きの初期化
                ac=120
                atemp=0
                ttmr=0
                i=0
                
        elif tmr < 220:  
                atemp= ac*ttmr
                screen.blit(img_bg[1], [0,1100-atemp])                   
                screen.blit(img_char[1], [0, 1100-atemp])             
                if ttmr < 17: 
                    ttmr=ttmr +1
                    ac= ac -3
                   
                else:
                    if  i<44: i = i + 1
                    screen.blit(img_fukidashi_2[int(i/15)], [0,1100-atemp])

        elif tmr < 250:  
                atemp= ac*ttmr
                screen.blit(img_bg[1], [0,1100-atemp])                   
                screen.blit(img_char[1], [0, 1100-atemp])             
                screen.blit(img_fukidashi_2[int(i/15)], [0,1100-atemp])
                screen.blit(img_koukaon[1], [0,1100-atemp])                     
                    
#        if scene == 3:
        elif tmr == 250:
                #このシーンの動きの初期化
                ac=120
                atemp=0
                ttmr=0
        elif tmr < 270:

                atemp= ac*ttmr
                screen.blit(img_bg[2], [0,0-atemp])                   
                screen.blit(img_char[2], [0,0-atemp]) 
                screen.blit(img_hanabi[2], [0,0-atemp])                 
                screen.blit(img_koukaon[2], [0,0-atemp])                   
        elif tmr < 290:

                atemp= ac*ttmr
                screen.blit(img_bg[2], [0,0-atemp])                   
                #screen.blit(img_char[2], [0,0-atemp]) 
                screen.blit(img_alice_dekimashita,[0,0-atemp]) 
                screen.blit(img_hanabi[2], [0,0-atemp])                 
                #screen.blit(img_koukaon[2], [0,0-atemp]) 
                
                if ttmr < 19: 
                    ttmr=ttmr +1
                    ac= ac -3

        elif tmr ==280:
                ttmr =0

        elif tmr ==290:
                screen.blit(img_fukidashi_3[0], [0,0])   
        
        elif tmr <340:
                ttmr=5     
            
        elif tmr <410:       
                if ttmr < 19: 
                       ttmr=ttmr +1
                       ac= ac -3
                       screen.blit(img_bg[2], [0,0-atemp])                   
                       #screen.blit(img_char[2], [0,0-atemp]) 
                       screen.blit(img_alice_dekimashita,[0,0-atemp]) 
                       screen.blit(img_hanabi[2], [0,0-atemp])                 
                       #screen.blit(img_koukaon[2], [0,0-atemp]) 
                       screen.blit(img_fukidashi_3[0], [0,0])   
                       screen.blit(img_sensei_te, [0,0-atemp+80]) 
        

        else:
                pygame.quit()
                sys.exit()

        #カウンタ表示                
        text1 = font1.render("TMR:"+str(tmr)+" TTMR:"+str(ttmr)+" AC:"+str(ac), True, (255,0,0))
        screen.blit(text1, (0,0))
        
        #ウィンドクローズで強制終了
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((1280, 980), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((1280, 980))

        # 星のスクロール

        pygame.display.update()
        clock.tick(50)

if __name__ == '__main__':
    main()



