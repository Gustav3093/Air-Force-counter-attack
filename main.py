import pygame
import random

#Inicializar pygame
pygame.init()

#crear pantalla
screen = pygame.display.set_mode((1250,720))

#Cambiar titulo e icono

pygame.display.set_caption("Air Force Counter Attack")
icono = pygame.image.load("fighter-jet.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Space background.png")

#jugador
img_jugador = pygame.image.load("jet (1).png")
jugador_x = 586
jugador_y = 656
jugador_x_cambio = 0

#variables del enemigo
img_enemigo = pygame.image.load("enemigo.png")
enemigo_x = random.randint(0,500)
enemigo_y = random.randint(50, 800)
enemigo_x_cambio = 4
enemigo_y_cambio = 50

#variables del bala
img_bala = pygame.image.load("Bullet.png")
bala_x = 0
bala_y = 656
bala_x_cambio = 0
bala_y_cambio = 7
bala_visible = False


# funcion del jugador
def jugador(x,y):
    screen.blit(img_jugador, (x,y))

#funcion del enemigo
def enemigo(x,y):
    screen.blit(img_enemigo, (x,y))

# Disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    screen.blit(img_bala, (x + 16,y + 10))


#loop del juego
se_ejecuta = True
while se_ejecuta:
    #imagen de fondo
    screen.blit(fondo, (0,0))


    #EVENTO CERRAR
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    #CONTROLES ACTIVADOS
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -4
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 4
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)


    #CONTROLES DESACTIVADOS
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #Modificar ubicaciones del jugador
    jugador_x += jugador_x_cambio

    # Manetener en los bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 1195:
        jugador_x = 1195

    # Modificar ubicaciones del enemigo
    enemigo_x += enemigo_x_cambio

    # Manetener en los bordes al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 4
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 1195:
        enemigo_x_cambio = -4
        enemigo_y += enemigo_y_cambio

    #Movimiento bala
    if bala_y <= -32:
        bala_y = 656
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio



    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # Actualizar
    pygame.display.update()

