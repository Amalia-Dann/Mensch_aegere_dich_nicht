class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.currentPosition = [self.x_pos, self.y_pos]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):		#puts button on the screen
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def updatePosition(self, newPos):
        self.x_pos = newPos[0]
        self.y_pos = newPos[1]

        self.rect.center = (self.x_pos, self.y_pos)
        self.text_rect.center = (self.x_pos, self.y_pos)

        #self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        #self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def getPosition(self):
        return self.currentPosition

    def checkForInput(self, position):		#checks if the mouse is on the button -> so presst the button
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):		#checks also if the mouse is on the button but only print the text on the button in another color to visualize it
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

