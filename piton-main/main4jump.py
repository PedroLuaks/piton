import pygame
import os

#Inicializando o Pygame
pygame.init()
#Definindo o tamanho da janela padrão

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) # Janela redimensionável
pygame.display.set_caption("Mover Imagem com Setas")
#Definindo a cor de fundo

BG_COLOR = (193, 0, 40) #cor de fundo (um tom escuro)
#Carregar a imagem
image_file = "player.png" # Coloque o nome correto da sua imagem aqui
if os.path.exists(image_file):
    img = pygame.Image.load(image_file).convert_alpha() 
    img_rect = img.get_rect(center=(WIDTH // 2, HEIGHT // 2)) # Centraliza a imagenm
else:
    print("Imagem não encontradal")

SPEED = 2
JUMP_STRENGTH = 20 
GRAVITY = 0.3 
JUMPING =  False 
VELOCITY_Y = 0 

def centralize_image():
    global img_rect, WIDTH, HEIGHT
    img_rect.center (WIDTH // 2, HEIGHT // 2) #Centraliza a imagem no centro da tela
#Variáveis para controle de redimensionamento
last_width, last_height = WIDTH, HEIGHT
#Limite de movimento para que o personagem não sala da tela
def limit_movement():
    global img_rect, WIDTH, HEIGHT
#Limita a posição da imagem para não sair da tela
    if img_rect.left < 0:
        img_rect.left = 0
    if img_rect.right > WIDTH:
        img_rect.right = WIDTH

        #Função para realizar o pula
def jump():
    global VELOCITY_Y, JUMPING
    if not JUMPING:
        VELOCITY_Y = -JUMP_STRENGTH 
        JUMPING = True


def update_jump():
    global VELOCITY_Y, JUMPING, img_rect
    if JUMPING:
        VELOCITY_Y += GRAVITY 
        img_rect.y += VELOCITY_Y

        if img_rect.bottom > HEIGHT:
            img_rect.bottom-HEIGHT#Garante que o personagem não passe do chão
            JUMPING = False
            VELOCITY_Y = 0  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False

    current_width, current_height = screen.get_size()

    if current_width - last_width or current_height != last_height:
        WIDTH, HEIGHT = current_width, current_height
        centralize_image() 
        last_width, last_height = current_width, current_height

    keys = pygame.key.get_pressed()

    # Movimentação da imagem
    if keys[pygame.K_LEFT]:
        img_rect.x -= SPEED # Move para a esquerda
    if keys[pygame.K_RIGHT]:
        img_rect.x += SPEED # Move para a direita
    if keys [pygame.K_UP]:
        img_rect.y -= SPEED # Move para cima
    if keys [pygame.K_DOWN]:
        img_rect.y += SPEED # Move para baixo
    
    #Pulo (tecla Space)
    if keys [pygame.K_SPACE]:
        jump() #Ativa o pulo
   
    # Limita o movimento para não sair da tela
    limit_movement()
   
    #Atualiza a física do pulo
    update_jump()
   
    #Preencher o fundo
    screen.fill(BG_COLOR)
    
    #Desenhar a imagem na tela
    screen.blit(img, img_rect.topleft)
   
    # Atualizar a tela
   
    pygame.display.flip()
   
    #Finalizar o Pygame
pygame.quit()