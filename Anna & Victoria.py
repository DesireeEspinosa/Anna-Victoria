from pygame import *
import sys

init()
mixer.init()
screen = display.set_mode((1000,600))
mixer.music.load("Mysterious2.mp3")
mixer.music.play(-1, 0.0)

def Inicio(escena):
    fondo = transform.scale(image.load("INTRO1.jpg"), (1000,600))
    while True:
        screen.fill((255,255,255)) 
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_p: return 2            
        screen.blit(fondo, (0,0))
        display.flip()

def Game(escena):
    dialogo = transform.scale(image.load("dialogo_1.jpg"), (1000,600))
    while True:
        screen.fill((255,255,255))   
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1: return 3 
        screen.blit(dialogo, (0,0))
        display.flip()
        
def Escenario1(escena):
    fondo = transform.scale(image.load("escenario1_1.jpg"), (1000,600))
    tocadiscos = transform.scale(image.load("1.tocadiscos.png"), (99,75))
    cartas = transform.scale(image.load("2.Cartas.png"), (44,65.5))
    sombrero = transform.scale(image.load("3.Sombrero.png"), (108,64))
    libro = transform.scale(image.load("4.Libro.png"), (85,71))
    pulsera = transform.scale(image.load("5.Pulsera.png"), (37,22))
    while True:
        screen.fill((255,255,255))  
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1: return 4
        screen.blit(fondo, (0,0))
        screen.blit(tocadiscos, (265.5,28))
        screen.blit(cartas, (457,305))
        screen.blit(sombrero, (661,144))
        screen.blit(libro, (614,77.56))
        screen.blit(pulsera, (395,420))
        display.flip()
        
def Escenario1_2(escena):
    fondo = transform.scale(image.load("escenario1_2.jpg"), (1000,600))
    tocadiscosON = transform.scale(image.load("1.tocadiscos_luz.png"),(109,85))
    tocadiscosOFF = transform.scale(image.load("1.tocadiscos.png"), (99,75))
    cartasON = transform.scale(image.load("2.Cartas_luz.png"), (52,75.5))
    cartasOFF = transform.scale(image.load("2.Cartas.png"), (44,65.5))
    sombreroON = transform.scale(image.load("3.Sombrero_luz.png"), (118,74))
    sombreroOFF = transform.scale(image.load("3.Sombrero.png"), (108,64))
    libroON = transform.scale(image.load("4.Libro_luz.png"), (95,81))
    libroOFF = transform.scale(image.load("4.Libro.png"), (85,71))
    pulseraON = transform.scale(image.load("5.Pulsera_luz.png"), (64,40))
    pulseraOFF = transform.scale(image.load("5.Pulsera.png"), (37,22))
    notaTocadiscos = transform.scale(image.load("tocadiscos_nota.png"), (715,700))
    notaSombrero = transform.scale(image.load("sombrero_nota.png"), (760,760))
    notaPulsera = transform.scale(image.load("pulsera_nota.png"), (740,760))
    checklist = [0, 0, 0, 0, 0]
    cuentaObjetos = 0
    while True:
        screen.fill((255,255,255))  
        screen.blit(fondo, (0,0))
        x, y = mouse.get_pos()
        #ON y OFF de los objetos:
        tocadiscosRect = Rect(265.5,28,99,75)
        cartasRect = Rect(457,305,44,65.5)
        sombreroRect = Rect(661,144,108,64)
        libroRect = Rect(614,77.5,85,71)
        pulseraRect = Rect(395,420,37,22)
        screen.blit(tocadiscosON,(265.5,28)) if tocadiscosRect.collidepoint((x,y)) else screen.blit(tocadiscosOFF, (265.5,28))
        screen.blit(cartasON,(457,305)) if cartasRect.collidepoint((x,y)) else screen.blit(cartasOFF, (457,305))
        screen.blit(sombreroON,(661,144)) if sombreroRect.collidepoint((x,y)) else screen.blit(sombreroOFF, (661,144))
        screen.blit(libroON,(614,77.5)) if libroRect.collidepoint((x,y)) else screen.blit(libroOFF, (614,77.5))
        screen.blit(pulseraON,(395,420)) if pulseraRect.collidepoint((x,y)) else screen.blit(pulseraOFF, (395,420))
        if tocadiscosRect.collidepoint((x,y)) and mouse.get_pressed()[0]: screen.blit(notaTocadiscos,(120,-30))
        if sombreroRect.collidepoint((x,y)) and mouse.get_pressed()[0]: screen.blit(notaSombrero,(120,-30))
        if pulseraRect.collidepoint((x,y)) and mouse.get_pressed()[0]: screen.blit(notaPulsera,(120,-30))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                x, y = mouse.get_pos()
                if tocadiscosRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
                if cartasRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
                if sombreroRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
                if libroRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
                if pulseraRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
        if cuentaObjetos == 5: return 5
        display.flip()
        
def Escenario2(escena):
    fondo = transform.scale(image.load("escenario2_1.jpg"), (1000,600))
    osoON = transform.scale(image.load("1.oso_luz.png"),(62,85))
    osoOFF = transform.scale(image.load("1.oso.png"), (52,75))
    relojON = transform.scale(image.load("2.Reloj_luz.png"), (64,76))
    relojOFF = transform.scale(image.load("2.Reloj.png"), (54,66))
    camaraON = transform.scale(image.load("3.Camara_luz.png"), (67,55))
    camaraOFF = transform.scale(image.load("3.Camara.png"), (57,45))
    perfumeON = transform.scale(image.load("4.Perfume_luz.png"), (44,45))
    perfumeOFF = transform.scale(image.load("4.Perfume.png"), (34,35))
    cristalesON = transform.scale(image.load("5.Cristales_luz.png"), (66,50))
    cristalesOFF = transform.scale(image.load("5.Cristales.png"), (56,40))
    notaOso = transform.scale(image.load("oso_nota.png"), (740,780))
    notaCamara = transform.scale(image.load("camara_nota.png"), (740,760))
    checklist = [0, 0, 0, 0, 0]
    cuentaObjetos = 0
    while True:
        screen.fill((255,255,255))  
        screen.blit(fondo, (0,0))
        x, y = mouse.get_pos()
        osoRect = Rect(455,406,52,75)
        relojRect = Rect(48,520,54,66)
        camaraRect = Rect(150,434.5,57,45)
        perfumeRect = Rect(42,72.9,34,35)
        cristalesRect = Rect(400,440,56,40)
        screen.blit(osoON,(455,406)) if osoRect.collidepoint((x,y)) else screen.blit(osoOFF, (455,406))
        screen.blit(relojON,(48,520)) if relojRect.collidepoint((x,y)) else screen.blit(relojOFF, (48,520))
        screen.blit(camaraON,(150,434.5)) if camaraRect.collidepoint((x,y)) else screen.blit(camaraOFF, (150,434.5))
        screen.blit(perfumeON,(42,72.9)) if perfumeRect.collidepoint((x,y)) else screen.blit(perfumeOFF, (42,72.9))
        screen.blit(cristalesON,(400,440)) if cristalesRect.collidepoint((x,y)) else screen.blit(cristalesOFF, (400,440))
        if osoRect.collidepoint((x,y)) and mouse.get_pressed()[0]:
            screen.blit(notaOso,(120,-50))
        if camaraRect.collidepoint((x,y)) and mouse.get_pressed()[0]:
            screen.blit(notaCamara,(120,-80))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                x, y = mouse.get_pos()
                if osoRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
                if relojRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
                if camaraRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
                if perfumeRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
                if cristalesRect.collidepoint((x,y)):
                    checklist[0] = 1
                    cuentaObjetos += 1
        if cuentaObjetos == 5: return 6
        display.flip()
        
def Final(escena):
    fondo = transform.scale(image.load("finalFONDO_layout.jpg"), (1000,600))
    while True:
        screen.fill((255,255,255))           
        screen.blit(fondo, (0,0))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1: return 7
        display.flip()
        
def Fade(escena): 
    fade = Surface((1000, 600))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        display.update()
        time.delay(5)
        mixer.music.stop()

escena = 1 
while True:
    if escena==1:
        escena = Inicio(escena)
    elif escena==2:
        escena = Game(escena)
    elif escena==3:
        escena = Escenario1(escena)
    elif escena==4:
        escena = Escenario1_2(escena)
    elif escena==5:
        escena = Escenario2(escena)
    elif escena==6:
        escena = Final(escena)
    elif escena==7:
        escena = Fade(escena)