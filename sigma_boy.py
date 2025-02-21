import pygame 
import random
pygame.init ()
pygame.mixer.init()
pygame.mixer.music.load("Skillet - Monster.mp3")
pygame.mixer.music.play(-1)
player_image = pygame.image.load("sigma.jpg")
player_image = pygame.transform.scale(player_image,(50,50))
player = pygame.Rect(52,92,50,50)

player_image2 = pygame.image.load("image.jpg")
player_image2 = pygame.transform.scale(player_image2,(150,150))
player2 = pygame.Rect(182,192,50,50)

window = pygame.display.set_mode((700,552))
fon = pygame.image.load("fon.jpg")
font = pygame.font.Font (None,36)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        

    window.blit(fon,(0,0))
    window.blit(text,(200,200))
    window.blit(player_image,(player.x,player.y))
    window.blit(player_image2,(player2.x,player2.y))


    if player.colliderect(player2):
        player2.x = random.randint(0,200)
        player2.y = random.randint(0,200)



    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        player.y += 3
    if keys[pygame.K_d]:
        player.x += 3
    if keys[pygame.K_w]:
        player.y -= 3
    if keys[pygame.K_a]:
        player.x -= 3

    if keys[pygame.K_k] and player2.y < 320:
        player2.y += 3
    if keys[pygame.K_l] and player2.x < 450:
        player2.x += 3
    if keys[pygame.K_i] and player2.y > 0:
        player2.y -= 3
    if keys[pygame.K_j] and player2.x > 0:
        player2.x -= 3
    if player2.y < -50:
        player2.y = 450

    pygame.display.update()
    pygame.time.Clock().tick(60)

 
