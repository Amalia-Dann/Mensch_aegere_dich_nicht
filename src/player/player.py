class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getFigure(self):
        figure_list = [0,0,0,0]
        return figure_list

    def winner(self, figure_list):
        for i in range(4):
            if figure_list[i] >=41 and figure_list[i] <=44:
                return True
            else:
                return False

# pl1=  [fiel_list[0], sp2, sp3, sp4]
#  var1 = pl1[0]
# pl1[0] = var1 + dice
# pl1[0] = field_list[0+dice]
