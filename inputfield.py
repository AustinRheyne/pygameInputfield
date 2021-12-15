import pygame

pygame.font.init()

class InputField:
    def __init__(self, screen, pos, size, color, textColor):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        self.screen = screen
        self.textColor = textColor
        self.focused = False
        self.caps = False

        self.text = ""
        self.txt_box = self.font.render(self.text, False, textColor)
        self.canType = True
        self.width = size[0]

        self.shift_versions = {
            '1' : '!',
            '2' : '@',
            '3' : '#',
            '4' : '$',
            '5' : '%',
            '6' : '^',
            '7' : '&',
            '8' : '*',
            '9' : '(',
            '0' : ')',
            '`' : '~',
            '-' : '_',
            '=' : '+',
            ',' : '<',
            '.' : ">",
            '/' : '?',
            ';' : ':',
            "'" : '"',
            '[' : '{',
            ']' : '}',
            '\\' : '|'
        }

    def draw(self):

        if self.font.size(self.text)[0]  >= self.width:
            self.canType = False
            print("TOO LONG!")
        else:
            self.canType = True

        # Draw the input field to the screen after calculations
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.txt_box, (self.rect.x, self.rect.centery))
