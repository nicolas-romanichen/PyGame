import pygame


pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 72)

txt = font.render("Helloo", True, "black")
                #Texto, Fonte arredondada, Cor

txt_center = txt.get_rect(center=(400, 300))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    
    #Conteudo
    screen.blit(txt, txt_center)

    pygame.display.flip()
    clock.tick(60) #limita a 60fps

pygame.quit() #usuario clica no X para fechar a janela
