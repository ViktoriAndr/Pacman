class Map:
    def __init__(self):
        with open("map.txt") as f:
            self.map = f.read().splitlines()
        self.height = len(self.map)
        self.width = len(self.map[0])

        self.portal_point = []
        self.home_point = []

        for i in range(0, self.height):
            for j in range(self.width):
                if self.map[i][j] == '!':
                    self.portal_point.append([j, i])
                if self.map[i][j] == '&':
                    self.home_point.append([j, i])
                    self.home_point.append([j+0.5, i-0.5])
                    self.home_point.append([j+0.5, i])
                    self.home_point.append([j, i-0.5])
                    self.home_point.append([j-0.5, i])
                    self.home_point.append([j-0.5, i-0.5])



