import pygame
from inputfield import InputField

pygame.init()
pygame.display.set_caption("Input Box Test")
screen = pygame.display.set_mode((900,900))

myTextBox = InputField(screen, (0,0), (400,200), (255,255,255), (0,0,0))

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if myTextBox.rect.left < x < myTextBox.rect.right and myTextBox.rect.top < y < myTextBox.rect.bottom:
                    myTextBox.focused = True
                    print('FOCUSED!')
                else:
                    myTextBox.focused = False
                    print("NOT FOCUSED!")
                    
        if myTextBox.focused:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    myTextBox.text = myTextBox.text[:-1]
                elif event.key == pygame.K_SPACE:
                    myTextBox.text += " "
                elif event.key == pygame.K_LSHIFT:
                    myTextBox.caps = True
                elif event.key == pygame.K_RETURN:
                    myTextBox.text += '\n'
                else:
                    if myTextBox.canType:
                        if myTextBox.caps:
                            if pygame.key.name(event.key) in myTextBox.shift_versions:
                                myTextBox.text += myTextBox.shift_versions[pygame.key.name(event.key)]
                            else:
                                myTextBox.text += pygame.key.name(event.key).upper()
                        else:
                            myTextBox.text += pygame.key.name(event.key)
            
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    myTextBox.caps = False

                myTextBox.txt_box = myTextBox.font.render(myTextBox.text, False, myTextBox.textColor)


    myTextBox.draw()

    pygame.display.flip()
pygame.quit()
