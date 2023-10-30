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
                pygame.image.load('image/IMG_0614.png') , pygame.image.load('image/IMG_0586.png') ,
                pygame.image.load('image/IMG_0583.png')]  
    img_hanabi = [ pygame.image.load('image/IMG_0592.png'),  pygame.image.load('image/IMG_0598.png'),   
               pygame.image.load('image/IMG_0615.png') , pygame.image.load('image/IMG_0587.png') ]  
    img_koukaon = [ pygame.image.load('image/IMG_0593.png'),  pygame.image.load('image/IMG_0599.png'),   
              pygame.image.load('image/IMG_0616.png') , pygame.image.load('image/IMG_0581.png') ]  
    
    img_fukidashi_1 = [ pygame.image.load('image/IMG_05941.png'),  pygame.image.load('image/IMG_05942.png'),   
              pygame.image.load('image/IMG_05943.png') , pygame.image.load('image/IMG_05944.png') ,
              pygame.image.load('image/IMG_0594.png') ]  
    img_fukidashi_2 = [ pygame.image.load('image/IMG_06001.png'),  pygame.image.load('image/IMG_06002.png'),   
              pygame.image.load('image/IMG_0600.png') ] 
    img_fukidashi_3 = [ pygame.image.load('image/IMG_0617.png') ,pygame.image.load('image/IMG_06161.png')] 
    img_fukidashi_4 = [ pygame.image.load('image/IMG_0584.png') ]
    img_alice_dekimashita = pygame.image.load('image/IMG_06141.png')
    img_sensei_te = pygame.image.load("image/IMG_06142.png")
    tmr = 0

    scene = 1
    ac = 100
    sc = 1.0
    

    pygame.init()
    pygame.display.set_caption("アリスの花火")
    screen = pygame.display.set_mode((1280, 980))
    
    #透明を有効にしたsurface
    scr =pygame.Surface((1280,980),flags=pygame.SRCALPHA)

    #フォントの用意
    font1 = pygame.font.SysFont('meiryo', 40)   
    clock = pygame.time.Clock()

    #while key[pygame.K_UP] <1:
    #    tmr=0
        
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
                if ttmr < 15: 
                    ttmr=ttmr +1
                    ac= ac -3
                   
                else:
                    if  i<44: i = i + 1
                    screen.blit(img_fukidashi_2[int(i/15)], [0,1100-atemp])

        elif tmr < 225:  
                j = 20
                atemp= ac*ttmr
                if tmr%5== 0:
                    j = -20
                    
                screen.blit(img_bg[1], [0,1100-atemp +j])                   
                screen.blit(img_char[1], [0, 1100-atemp +j])             
                screen.blit(img_fukidashi_2[int(i/15)], [0,1100-atemp +j])
                screen.blit(img_koukaon[1], [0,1100-atemp +j]) 
  
                # 半透明のfillが有効
                scr.fill((255,255,255,115+(tmr-220)*10))
               # ベースのsurfaceに貼り付け
                screen.blit(scr,(0,0))  
                
        elif tmr < 235: 
                      
                atemp= ac*ttmr
                screen.blit(img_bg[1], [0,1100-atemp])                   
                screen.blit(img_char[1], [0, 1100-atemp])             
                screen.blit(img_fukidashi_2[int(i/15)], [0,1100-atemp])
                screen.blit(img_koukaon[1], [0,1100-atemp])                     

                # 半透明のfillが有効
                scr.fill((255,255,255,115+(tmr-220)*10))
               # ベースのsurfaceに貼り付け
                screen.blit(scr,(0,0))  
                    
#        if scene == 3:
        elif tmr == 235:
                #このシーンの動きの初期化
                ac=120
                atemp=0
                ttmr=0
        elif tmr <250:        
 
                # 半透明のfillが有効
                scr.fill((255,255,255,255))
               # ベースのsurfaceに貼り付け
                screen.blit(scr,(0,0))  
               
        elif tmr < 270:

                atemp= ac*ttmr
                if ttmr < 15: 
                    ttmr=ttmr +1
                    ac= ac -3
                screen.blit(img_bg[2], [0,0])                   
                screen.blit(img_char[2], [0,0]) 

                screen.blit(img_koukaon[2], [150,0])  
                if tmr%2 == 0:
                    screen.blit(img_hanabi[2], [0,0])   
                
                # 半透明のfillが有効
                scr.fill((255,255,255,255-ttmr*17))
               # ベースのsurfaceに貼り付け
                screen.blit(scr,(0,0))      
                    
                    
                    

        elif tmr == 270:
                  #このシーンの動きの初期化
                  ac=120
                  atemp=0
                  ttmr=0               
        elif tmr < 300:

                atemp= ac*ttmr
                screen.blit(img_bg[2], [0,0-atemp])                   
                #screen.blit(img_char[2], [0,0-atemp]) 
                screen.blit(img_alice_dekimashita,[0,0-atemp]) 
                if tmr%2 == 0:
                    screen.blit(img_hanabi[2], [0,0-atemp])                 
                #screen.blit(img_koukaon[2], [0,0-atemp]) 
                
                if ttmr < 15: 
                    ttmr=ttmr +1
                    ac= ac -3

        elif tmr ==300:
                ttmr =0

        elif tmr ==330:
                screen.blit(img_fukidashi_3[0], [-800,-200])   
        
        elif tmr <360:
                i = 5    
            
        elif tmr <390:       

                       screen.blit(img_bg[2], [0,0-atemp])                   
                       #screen.blit(img_char[2], [0,0-atemp]) 
                       screen.blit(img_alice_dekimashita,[0,0-atemp]) 
                       screen.blit(img_hanabi[2], [0,0-atemp])                 
                       #screen.blit(img_koukaon[2], [0,0-atemp]) 

                       if i <20 : i= i +3
                       screen.blit(img_sensei_te, [0,0-atemp+80-i+60 ]) 
                       screen.blit(img_fukidashi_3[1], [180,300-atemp]) 
                       screen.blit(img_fukidashi_3[0], [-800,-200])   
        elif tmr ==390:
                       ttmr =0
                       scr.fill((255,255,255,255))
                       # ベースのsurfaceに貼り付け
                       screen.blit(scr,(0,0))
        elif tmr <460:       
                       if ttmr<30 : ttmr = ttmr +1
                       #bg = pygame.transform.scale(img_bg[3], (1688-ttmr*10, 2463-ttmr*10))
                       screen.blit(img_bg[3], [0,ttmr*32-960] ) 
                       #char4 = pygame.transform.scale(img_char[4], (1688-ttmr*10, 2463-ttmr*10))
                       #screen.blit(img_char[4], [0,ttmr*32-960]) 
                       #char3 = pygame.transform.scale(img_char[3], (1688-ttmr*10, 2463-ttmr*10))
                       screen.blit(img_char[3], [0,ttmr*32-960]) 

                       #fukidashi = pygame.transform.scale(img_fukidashi_4[0], (1688-ttmr*10, 2463-ttmr*10))
                       screen.blit(img_fukidashi_4[0],[0,(tmr-390)%2*2]) 

                       #kouka = pygame.transform.scale(img_koukaon[3],(1688-ttmr*10, 2463-ttmr*10))
                       screen.blit(img_koukaon[3], [(tmr-390)%5*2 -20,ttmr*32-960])                        
        

        else:
                pygame.quit()
                sys.exit()

        #カウンタ表示                
        #text1 = font1.render("TMR:"+str(tmr)+" TTMR:"+str(ttmr)+" AC:"+str(ac), True, (255,0,0))
        #screen.blit(text1, (0,0))
        
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



