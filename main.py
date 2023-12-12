# Importar librerías 
import pygame, sys
from pygame import mixer #agregar sonidos 
import random
import math
from boton import Boton
import threading

#Inicializar pygame 
pygame.init()

#Crear pantalla 
pantalla = pygame.display.set_mode((1200, 700))

# Titulo e Icono
pygame.display.set_caption("Guerra Espacial")
icono = pygame.image.load("astronauta.png") 
pygame.display.set_icon(icono)

# Fondo 
fondo = pygame.image.load("fondo2vol2.jpg")
fondo_menu = pygame.image.load("fondo_menu2.jpg")

# Agregar música
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3) # Número del 0 al 1
mixer.music.play(-1)

# Variables del Jugador
img_jugador = pygame.image.load("astronave.png")



# Variables del enemigo
img_enemigo = []


# Variables de la bala
img_bala = pygame.image.load("bala.png")
img_bala_nave = pygame.image.load("bala_nave.png")
# Se quiere que el enemigo aparezca en un lugar random



# Puntaje
fuente = pygame.font.Font('Fastest.ttf', 32) # Nombre de una fuente y luego el tamañp



# Texto final de juego
fuente_final = pygame.font.Font('Fastest.ttf', 40)

# Fución texto final
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (300, 300)) # Que aparezca al centro de la pantalla

# Función mostrar puntaje
def mostrar_puntaje(x, y, puntaje):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255)) # render de renderizar: imprimir o mostrar en pantalla. Texto, antialias = True, color en RGB
    pantalla.blit(texto, (x, y))

# Función que construya la posición del personaje
def jugador(x, y):
    # Si quiero que el jugador se mueva:
    pantalla.blit(img_jugador, (x, y)) # Se tienen valores que van cambiando dinámicamente





# Función dispara bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 100)) # Hacer que la bala aprezca a la mitad de la nave

# Función dispara bala nave enemiga 
def disparar_bala_nave(x, y):
    global bala_nave_visible
    bala_nave_visible = True
    pantalla.blit(img_bala_nave, (x + 16, y + 100)) # Hacer que la bala aprezca a la mitad de la nave enemiga


# Función detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2)) # math.pow() es para un exponente
    if distancia < 27:
        return True
    else:
        return False
    
# Función detectar colisiones
def hay_colision_nave(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2)) # math.pow() es para un exponente
    if distancia < 120:
        return True
    else:
        return False
    

#FUNCIONES PARA CADA VENTANA 

#Funcion jugar: niveles 
def jugar():

    while True:
        pantalla.blit(fondo_menu, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        texto_jugar = fuente.render("Selecciona un nivel", True, (255, 255, 255))
        texto_jugar_rect = texto_jugar.get_rect(center=(600, 100))

        boton_basico = Boton(pos=(600, 250), texto='Basico', fuente=pygame.font.Font('Fastest.ttf', 60), color_base="White", color_sombra="Green")
        boton_medio = Boton(pos=(600, 350), texto='Medio', fuente=pygame.font.Font('Fastest.ttf', 60), color_base="White", color_sombra="Green")
        boton_avanzado = Boton(pos=(600, 450), texto='Avanzado', fuente=pygame.font.Font('Fastest.ttf', 60), color_base="White", color_sombra="Green")
        boton_atras = Boton(pos=(600, 600), texto='Atrás', fuente=pygame.font.Font('Fastest.ttf', 40), color_base="White", color_sombra="Green")
        
        pantalla.blit(texto_jugar, texto_jugar_rect)

        for boton in [boton_basico, boton_medio, boton_avanzado, boton_atras]:
            boton.update(pantalla)

        for evento in pygame.event.get():

                # Evento para cerrar programa
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_basico.check(menu_mouse_pos):
                        basico()
                    if boton_medio.check(menu_mouse_pos):
                        medio()
                    if boton_avanzado.check(menu_mouse_pos):
                        avanzado()
                    if boton_atras.check(menu_mouse_pos):
                        menu()
        
        pygame.display.update()


#Función nivel basico
def basico():

    # Determinar posición del jugador
    jugador_x = 568 # A la mitad. Esquina superiro izquierda = 0
    jugador_y = 600
    jugador_x_cambio = 0

    # Variables del enemigo
    img_enemigo = []
    enemigo_x = []
    enemigo_y = []
    enemigo_x_cambio = []
    enemigo_y_cambio = []
    cantidad_enemigos = 8

    for e in range(cantidad_enemigos):
        img_enemigo.append(pygame.image.load("ovnienemigo.png"))
        enemigo_x.append(random.randint(0, 636))
        enemigo_y.append(random.randint(50, 200))
        enemigo_x_cambio.append(0.5)
        enemigo_y_cambio.append(50)

    global bala_visible
    bala_x = 0
    bala_y = 600
    bala_x_cambio = 0
    bala_y_cambio = 3
    bala_visible = False

    # Función enemigo
    def enemigo(x, y, ene):
        pantalla.blit(img_enemigo[ene], (x, y))
        
    # Puntaje
    puntaje = 0

    # Ponerle coordenadas al puntaje
    texto_x = 10
    texto_y = 10


    # LOOP DEL JUEGO

    while True:
        # Cambiar fondo con imagen de fondo
        pantalla.blit(fondo, (0, 0))
        menu_mouse_pos = pygame.mouse.get_pos()


        back_boton = Boton(pos=(1100,30), texto='Atrás', fuente=pygame.font.Font('Fastest.ttf', 40), color_base="White", color_sombra="Green")
        back_boton.update(pantalla)

        # EVENTOS 
        for evento in pygame.event.get():

            # Evento para cerrar programa
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                    if back_boton.check(menu_mouse_pos):
                        menu()
            
            # Evento para controlar movimiento del jugador
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador_x_cambio = -1
                if evento.key == pygame.K_RIGHT:
                    jugador_x_cambio = 1
                if evento.key == pygame.K_SPACE:
                    sonido_bala = mixer.Sound('disparo.mp3')
                    sonido_bala.play()
                    if not bala_visible:
                        bala_x = jugador_x
                        disparar_bala(bala_x, bala_y)

            # Evento soltar flechas
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    jugador_x_cambio = 0

        # Ubicación del jugador 
        jugador_x += jugador_x_cambio


        # Mantener dentro de bordes al jugador
        if jugador_x <= 0:
            jugador_x = 0
        elif jugador_x >= 1136:
            jugador_x = 1136


        # Modificar ubiación del enemigo
        for e in range(cantidad_enemigos):

            # Fin del juego
            if enemigo_y[e] > 600: # Si algún enemigo ha alcanzado un altura superior a 500
                for k in range(cantidad_enemigos): # Sacar a los otros de la pantalla
                    enemigo_y[k] = 1000
                texto_final()
                break


            enemigo_x[e] += enemigo_x_cambio[e]
                
            # Mantener dentro de bordes al enemigo
            if enemigo_x[e] <= 0:
                enemigo_x_cambio[e] = 1 # Si toca el borde izquierdo cambia el movimiento a la derecha
                enemigo_y[e] += enemigo_y_cambio[e]
            elif enemigo_x[e] >= 1136:
                enemigo_x_cambio[e] = -1 # Si toca el borde derecho cambia el movimiento a la izquierda
                enemigo_y[e] += enemigo_y_cambio[e]

            # Verificación de colisión
            colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
            if colision:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.play()
                bala_y = 500
                bala_visible = False  # Para lanzar una bala nueva
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)

            enemigo(enemigo_x[e], enemigo_y[e], e)

        # Movimiento bala: para que sea persistente en cada iteración
        if bala_y <= -64: # Cuando la bala haya desaparecido completamente de la vista
            bala_y = 500
            bala_visible = False

        if bala_visible:
            disparar_bala(bala_x, bala_y)
            bala_y -= bala_y_cambio # La bala va subiendo

    

        # Mostrar pantalla y jugador 
        jugador(jugador_x, jugador_y)
        mostrar_puntaje(texto_x, texto_y, puntaje)

        

        # Actualizar pantalla  
        pygame.display.update()


#Función nivel medio
def medio():
    # Determinar posición del jugador
    jugador_x = 568 # A la mitad. Esquina superiro izquierda = 0
    jugador_y = 600
    jugador_x_cambio = 0

    # Variables del enemigo
    img_enemigo = []
    enemigo_x = []
    enemigo_y = []
    enemigo_x_cambio = []
    enemigo_y_cambio = []
    cantidad_enemigos = 8

    # Variables de los asteroides
    img_asteroide = []
    asteroide_x = []
    asteroide_y = []
    asteroide_x_cambio = []
    asteroide_y_cambio = []
    cantidad_asteroides = 3


    for e in range(cantidad_enemigos):
        img_enemigo.append(pygame.image.load("ovnienemigo.png"))
        enemigo_x.append(random.randint(0, 636))
        enemigo_y.append(random.randint(50, 200))
        enemigo_x_cambio.append(1) # se mueven mas rapido 
        enemigo_y_cambio.append(60)

    for a in range(cantidad_asteroides):
        img_asteroide.append(pygame.image.load("asteroide.png"))
        asteroide_x.append(random.randint(0, 1136))
        asteroide_y.append(random.randint(50, 200))
        asteroide_y_cambio.append(random.uniform(0.1, 0.2))



    global bala_visible
    bala_x = 0
    bala_y = 600
    bala_x_cambio = 0
    bala_y_cambio = 3
    bala_visible = False



    # Función enemigo
    def enemigo(x, y, ene):
        pantalla.blit(img_enemigo[ene], (x, y))

    # Función enemigo
    def asteroide(x, y, a):
        pantalla.blit(img_asteroide[a], (x, y))

        
    # Puntaje
    puntaje = 0

    # Ponerle coordenadas al puntaje
    texto_x = 10
    texto_y = 10


    # LOOP DEL JUEGO

    while True:
        # Cambiar fondo con imagen de fondo
        pantalla.blit(fondo, (0, 0))
        menu_mouse_pos = pygame.mouse.get_pos()


        back_boton = Boton(pos=(1100,30), texto='Atrás', fuente=pygame.font.Font('Fastest.ttf', 40), color_base="White", color_sombra="Green")
        back_boton.update(pantalla)

        # EVENTOS 
        for evento in pygame.event.get():

            # Evento para cerrar programa
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                    if back_boton.check(menu_mouse_pos):
                        menu()
            
            # Evento para controlar movimiento del jugador
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador_x_cambio = -1
                if evento.key == pygame.K_RIGHT:
                    jugador_x_cambio = 1
                if evento.key == pygame.K_SPACE:
                    sonido_bala = mixer.Sound('disparo.mp3')
                    sonido_bala.play()
                    if not bala_visible:
                        bala_x = jugador_x
                        disparar_bala(bala_x, bala_y)

            # Evento soltar flechas
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    jugador_x_cambio = 0

        # Ubicación del jugador 
        jugador_x += jugador_x_cambio


        # Mantener dentro de bordes al jugador
        if jugador_x <= 0:
            jugador_x = 0
        elif jugador_x >= 1136:
            jugador_x = 1136


        # Modificar ubiación del enemigo
        for e in range(cantidad_enemigos):

            # Fin del juego
            if enemigo_y[e] > 600: # Si algún enemigo ha alcanzado un altura superior a 500
                for k in range(cantidad_enemigos): # Sacar a los otros de la pantalla
                    enemigo_y[k] = 1000
                texto_final()
                break


            enemigo_x[e] += enemigo_x_cambio[e]
                
            # Mantener dentro de bordes al enemigo
            if enemigo_x[e] <= 0:
                enemigo_x_cambio[e] = 1 # Si toca el borde izquierdo cambia el movimiento a la derecha
                enemigo_y[e] += enemigo_y_cambio[e]
            elif enemigo_x[e] >= 1136:
                enemigo_x_cambio[e] = -1 # Si toca el borde derecho cambia el movimiento a la izquierda
                enemigo_y[e] += enemigo_y_cambio[e]

            # Verificación de colisión
            colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
            if colision:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.play()
                bala_y = 500
                bala_visible = False  # Para lanzar una bala nueva
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)

            enemigo(enemigo_x[e], enemigo_y[e], e)

        
        # Modificar ubicación del asteroide
        for a in range(cantidad_asteroides):

            # Fin del juego
            if asteroide_y[a] > 600: # Si algún enemigo ha alcanzado un altura superior a 500
                for k in range(cantidad_asteroides): # Sacar a los otros de la pantalla
                    asteroide_y[k] = 1000
                texto_final()
                break


            asteroide_y[a] += asteroide_y_cambio[a]


            # Verificación de colisión
            colision = hay_colision(asteroide_x[a], asteroide_y[a], bala_x, bala_y)
            if colision:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.play()
                bala_y = 500
                bala_visible = False  # Para lanzar una bala nueva
                puntaje += 1
                asteroide_x[a] = random.randint(0, 736)
                asteroide_y[a] = random.randint(50, 200)

            asteroide(asteroide_x[a], asteroide_y[a], a)



        # Movimiento bala: para que sea persistente en cada iteración
        if bala_y <= -64: # Cuando la bala haya desaparecido completamente de la vista
            bala_y = 500
            bala_visible = False
    

        if bala_visible:
            disparar_bala(bala_x, bala_y)
            bala_y -= bala_y_cambio # La bala va subiendo


        # Mostrar pantalla y jugador 
        jugador(jugador_x, jugador_y)
        mostrar_puntaje(texto_x, texto_y, puntaje)

        

        # Actualizar pantalla  
        pygame.display.update()

#Función nivel avanzado
def avanzado():
    # Determinar posición del jugador
    jugador_x = 568 # A la mitad. Esquina superiro izquierda = 0
    jugador_y = 600
    jugador_x_cambio = 0

    # Variables del enemigo
    img_enemigo = []
    enemigo_x = []
    enemigo_y = []
    enemigo_x_cambio = []
    enemigo_y_cambio = []
    cantidad_enemigos = 8

    # Variables de los asteroides
    img_asteroide = []
    asteroide_x = []
    asteroide_y = []
    asteroide_x_cambio = []
    asteroide_y_cambio = []
    cantidad_asteroides = 3

    # Variables de la nave enemiga
    img_nave = pygame.image.load("astronave_mala.png")
    nave_x = random.randint(0, 1136)
    nave_y = random.randint(50, 200)
    nave_x_cambio = 1


    for e in range(cantidad_enemigos):
        img_enemigo.append(pygame.image.load("ovnienemigo.png"))
        enemigo_x.append(random.randint(0, 636))
        enemigo_y.append(random.randint(50, 200))
        enemigo_x_cambio.append(1) # se mueven mas rapido 
        enemigo_y_cambio.append(60)

    for a in range(cantidad_asteroides):
        img_asteroide.append(pygame.image.load("asteroide.png"))
        asteroide_x.append(random.randint(0, 1136))
        asteroide_y.append(random.randint(50, 200))
        asteroide_y_cambio.append(random.uniform(0.1, 0.2))



    global bala_visible
    bala_x = 0
    bala_y = 600
    bala_x_cambio = 0
    bala_y_cambio = 3
    bala_visible = False

    #Bala de los enemigos 
    global bala_nave_visible
    bala_nave_x = 0
    bala_nave_y = 20
    bala_nave_x_cambio = 0
    bala_nave_y_cambio = 3
    bala_nave_visible = False

    # Función enemigo
    def enemigo(x, y, ene):
        pantalla.blit(img_enemigo[ene], (x, y))

    # Función enemigo
    def asteroide(x, y, a):
        pantalla.blit(img_asteroide[a], (x, y))

    # Función nave enemiga 
    def nave(x, y):
        pantalla.blit(img_nave, (x, y))
        
    # Puntaje
    puntaje = 0

    # Ponerle coordenadas al puntaje
    texto_x = 10
    texto_y = 10


    # LOOP DEL JUEGO

    while True:
        # Cambiar fondo con imagen de fondo
        pantalla.blit(fondo, (0, 0))
        menu_mouse_pos = pygame.mouse.get_pos()


        back_boton = Boton(pos=(1100,30), texto='Atrás', fuente=pygame.font.Font('Fastest.ttf', 40), color_base="White", color_sombra="Green")
        back_boton.update(pantalla)

        # EVENTOS 
        for evento in pygame.event.get():

            # Evento para cerrar programa
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                    if back_boton.check(menu_mouse_pos):
                        menu()
            
            # Evento para controlar movimiento del jugador
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador_x_cambio = -1
                if evento.key == pygame.K_RIGHT:
                    jugador_x_cambio = 1
                if evento.key == pygame.K_SPACE:
                    sonido_bala = mixer.Sound('disparo.mp3')
                    sonido_bala.play()
                    if not bala_visible:
                        bala_x = jugador_x
                        disparar_bala(bala_x, bala_y)

            # Evento soltar flechas
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    jugador_x_cambio = 0

        # Ubicación del jugador 
        jugador_x += jugador_x_cambio


        # Mantener dentro de bordes al jugador
        if jugador_x <= 0:
            jugador_x = 0
        elif jugador_x >= 1136:
            jugador_x = 1136


        # Modificar ubiación del enemigo
        for e in range(cantidad_enemigos):

            # Fin del juego
            if enemigo_y[e] > 600: # Si algún enemigo ha alcanzado un altura superior a 500
                for k in range(cantidad_enemigos): # Sacar a los otros de la pantalla
                    enemigo_y[k] = 1000
                texto_final()
                break


            enemigo_x[e] += enemigo_x_cambio[e]
                
            # Mantener dentro de bordes al enemigo
            if enemigo_x[e] <= 0:
                enemigo_x_cambio[e] = 1 # Si toca el borde izquierdo cambia el movimiento a la derecha
                enemigo_y[e] += enemigo_y_cambio[e]
            elif enemigo_x[e] >= 1136:
                enemigo_x_cambio[e] = -1 # Si toca el borde derecho cambia el movimiento a la izquierda
                enemigo_y[e] += enemigo_y_cambio[e]

            # Verificación de colisión
            colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
            if colision:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.play()
                bala_y = 500
                bala_visible = False  # Para lanzar una bala nueva
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)

            enemigo(enemigo_x[e], enemigo_y[e], e)

        
        # Modificar ubicación del asteroide
        for a in range(cantidad_asteroides):

            # Fin del juego
            if asteroide_y[a] > 600: # Si algún enemigo ha alcanzado un altura superior a 500
                for k in range(cantidad_asteroides): # Sacar a los otros de la pantalla
                    asteroide_y[k] = 1000
                texto_final()
                break


            asteroide_y[a] += asteroide_y_cambio[a]


            # Verificación de colisión
            colision = hay_colision(asteroide_x[a], asteroide_y[a], bala_x, bala_y)
            if colision:
                sonido_colision = mixer.Sound('Golpe.mp3')
                sonido_colision.play()
                bala_y = 500
                bala_visible = False  # Para lanzar una bala nueva
                puntaje += 1
                asteroide_x[a] = random.randint(0, 736)
                asteroide_y[a] = random.randint(50, 200)

            asteroide(asteroide_x[a], asteroide_y[a], a)
                
        # Modificar ubiación de la nave enemiga

        if not bala_nave_visible:
            bala_nave_x = nave_x
            bala_nave_y = nave_y
            disparar_bala_nave(bala_nave_x, bala_nave_y)

        nave_x += nave_x_cambio
                
        # Mantener dentro de bordes al enemigo
        if nave_x <= 0:
            nave_x_cambio = 1 # Si toca el borde izquierdo cambia el movimiento a la derecha
        elif nave_x >= 1136:
            nave_x_cambio = -1 # Si toca el borde derecho cambia el movimiento a la izquierda


        # Detectar colision entre la bala del enemigo y el jugador 
        colision_nave = hay_colision_nave(jugador_x, jugador_y, bala_nave_x, bala_nave_y)
        if colision_nave:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()

            # Fin del juego
            texto_final()
            break


            
        nave(nave_x, nave_y)

        if bala_nave_y >= 500: # Cuando la bala haya desaparecido completamente de la vista
            bala_nave_y = nave_y
            bala_nave_visible = False

        if bala_nave_visible:
            disparar_bala_nave(bala_nave_x, bala_nave_y)
            bala_nave_y += bala_nave_y_cambio # La bala va bajando

        # Movimiento bala: para que sea persistente en cada iteración
        if bala_y <= -64: # Cuando la bala haya desaparecido completamente de la vista
            bala_y = 500
            bala_visible = False
    

        if bala_visible:
            disparar_bala(bala_x, bala_y)
            bala_y -= bala_y_cambio # La bala va subiendo


        # Mostrar pantalla y jugador 
        jugador(jugador_x, jugador_y)
        mostrar_puntaje(texto_x, texto_y, puntaje)

        

        # Actualizar pantalla  
        pygame.display.update()


# Función menu 
def menu():


    while True:
        pantalla.blit(fondo_menu, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        texto_menu = fuente.render("Menu principal", True, (255, 255, 255))
        texto_menu_rect = texto_menu.get_rect(center=(600, 100))

        boton_jugar = Boton(pos=(600, 250), texto='Jugar', fuente=pygame.font.Font('Fastest.ttf', 70), color_base="White", color_sombra="Green")

        boton_salir = Boton(pos=(600, 400), texto='Salir', fuente=pygame.font.Font('Fastest.ttf', 70), color_base="White", color_sombra="Green")
        
        pantalla.blit(texto_menu, texto_menu_rect)

        for boton in [boton_jugar, boton_salir]:
            boton.update(pantalla)

        for evento in pygame.event.get():

                # Evento para cerrar programa
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_jugar.check(menu_mouse_pos):
                        jugar()
                    if boton_salir.check(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()
        
        pygame.display.update()


menu()