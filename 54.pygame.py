import pygame

### init -> data-data game/menjalankan engine
pygame.init()

## membuat display surface objek
window_x = 500
window_y = 500
window = pygame.display.set_mode((window_x,window_y))
## variabel running game
isRun = True

## objek game
# posisi / cordinate
x = 250
y = 250

# size / ukuran
lebar = 20
panjang = 20

speed = 2


### input user, database input -> keyboard,mouse,stik,dll
while isRun:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    keys = pygame.key.get_pressed()
    
    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    # ambil ke kanan
    if keys[pygame.K_RIGHT] and x < window_x-lebar:
        x += speed
    # ambil ke bawah
    if keys[pygame.K_DOWN] and y < window_y-panjang:
        y += speed
    # ambil ke atas 
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    ### update aset ->letakan menu atau hal-hal lain
    window.fill(color='white')
    pygame.draw.rect(window,(21,99,235),(x,y,lebar,panjang)) # **kwargs tidak bisa di afterwards kan oleh *args
    ### render ke display -> menampilakan ke layar
    pygame.display.update()


pygame.quit()




