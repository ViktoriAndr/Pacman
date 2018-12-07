from Map import Map


class Wall:
    def __init__(self):
        self.map = Map()
        self.wall_point = []
        for i in range(self.map.height):
            for j in range(self.map.width):
                if self.map.map[i][j] == '#' or self.map.map[i][j] == 'X':
                    self.wall_point.append([j, i])


'''
                    if (i != self.map.height or j != self.map.width) and \
                            (i != 0 or j != 0):
                        self.wall_point.append([j+0.5, i])
                        self.wall_point.append([j, i+0.5])
                        self.wall_point.append([j+0.5, i+0.5])
                        self.wall_point.append([j-0.5, i-0.5])
                        self.wall_point.append([j + 0.5, i - 0.5])
                        self.wall_point.append([j - 0.5, i + 0.5])
                        self.wall_point.append([j-0.5, i])
                        self.wall_point.append([j, i-0.5])
                    elif i == self.map.height or j == self.map.width:
                        self.wall_point.append([j - 0.5, i - 0.5])
                        self.wall_point.append([j - 0.5, i])
                        self.wall_point.append([j, i - 0.5])
                    elif i == 0 or j == 0:
                        self.wall_point.append([j + 0.5, i])
                        self.wall_point.append([j, i + 0.5])
                        self.wall_point.append([j + 0.5, i + 0.5])
                        '''

