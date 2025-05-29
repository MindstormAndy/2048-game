import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((950,700), pygame.RESIZABLE)

pygame.display.set_caption("2048")

black = 0, 0, 0
white = 255, 255, 255
background = 202, 191, 177
edges = 188,173,159
font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()

image_dict = {
    2: pygame.image.load("images//2.png","2"),
    4: pygame.image.load("images//4.png","4"),
    8: pygame.image.load("images//8.png","8"),
    16: pygame.image.load("images//16.png","16"),
    32: pygame.image.load("images//32.png","32"),
    64: pygame.image.load("images//64.png","64"),
    128: pygame.image.load("images//128.png","128"),
    256: pygame.image.load("images//256.png","256"),
    512: pygame.image.load("images//512.png","512"),
    1024: pygame.image.load("images//1024.png","1024"),
    2048: pygame.image.load("images//2048.png","2048"),
    4096: pygame.image.load("images//4096.png","4096"),
    8192: pygame.image.load("images//8192.png","8192")
}

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for i in range(self.size)] for j in range(self.size)]
        self.score = 0
        self.gameover = False
        self.won = False

        space1 = (random.randint(0,self.size-1), random.randint(0,self.size-1))
        space2 = (random.randint(0,self.size-1), random.randint(0,self.size-1))

        while space2 == space1:
            space2 = (random.randint(0,self.size-1), random.randint(0,self.size-1))

        self.spawn_tile(space1[0],space1[1])
        self.spawn_tile(space2[0],space2[1])

    def spawn_tile(self, row, column):
        if random.randint(0,9) == 0:
            self.grid[row][column] = 4
        else:
            self.grid[row][column] = 2

    def left_pressed(self):
        prev = -1
        changed = False
        for row in range(len(self.grid)):
            for curr in range(len(self.grid[row])):
                if prev == -1:
                    if self.grid[row][curr] != 0:
                        prev = curr
                    continue
                if self.grid[row][curr] == self.grid[row][prev]:
                    self.grid[row][prev] = 2 * self.grid[row][curr]
                    self.grid[row][curr] = 0
                    prev = -1
                    changed = True
                else:
                    if self.grid[row][curr] != 0:
                        prev = curr
            prev = -1
        
        for row in range(len(self.grid)):
            temp = []
            for element in range(len(self.grid[row])):
                if self.grid[row][element] != 0:
                    temp.append(self.grid[row][element])
            while len(temp) < len(self.grid[row]):
                temp.append(0)
            if self.grid[row] != list(temp):
                self.grid[row] = list(temp)
                changed = True
        if changed:
            self.spawn_new_tile()

    def up_pressed(self):
        prev = -1
        changed = False
        for col in range(len(self.grid)):
            for curr in range(len(self.grid[col])):
                if prev == -1:
                    if self.grid[curr][col] != 0:
                        prev = curr
                    continue
                if self.grid[curr][col] == self.grid[prev][col]:
                    self.grid[prev][col] = 2 * self.grid[curr][col]
                    self.grid[curr][col] = 0
                    prev = -1
                    changed = True
                else:
                    if self.grid[curr][col] != 0:
                        prev = curr
            prev = -1
        for col in range(len(self.grid)):
            temp = []
            for element in range(len(self.grid[col])):
                if self.grid[element][col] != 0:
                    temp.append(self.grid[element][col])
            while len(temp) < len(self.grid[col]):
                temp.append(0)
            for row in range(len(self.grid[col])):
                if self.grid[row][col] != temp[row]:
                    self.grid[row][col] = temp[row]
                    changed = True

        if changed:
            self.spawn_new_tile()

    def down_pressed(self):
        prev = -1
        changed = False
        for col in range(len(self.grid)):
            for curr in range(len(self.grid[col])-1,-1,-1):
                if prev == -1:
                    if self.grid[curr][col] != 0:
                        prev = curr
                    continue
                if self.grid[curr][col] == self.grid[prev][col]:
                    self.grid[prev][col] = 2 * self.grid[curr][col]
                    self.grid[curr][col] = 0
                    prev = -1
                    changed = True
                else:
                    if self.grid[curr][col] != 0:
                        prev = curr
            prev = -1
        for col in range(len(self.grid)):
            temp = []
            for element in range(len(self.grid[col])-1,-1,-1):
                if self.grid[element][col] != 0:
                    temp.insert(0,self.grid[element][col])
            while len(temp) < len(self.grid[col]):
                temp.insert(0,0)
            for row in range(len(self.grid[col])):
                if self.grid[row][col] != temp[row]:
                    self.grid[row][col] = temp[row]
                    changed = True
        if changed:
            self.spawn_new_tile()
        
    def right_pressed(self):
        prev = -1
        changed = False
        for row in range(len(self.grid)):
            for curr in range(len(self.grid[row])-1,-1,-1):
                if prev == -1:
                    if self.grid[row][curr] != 0:
                        prev = curr
                    continue
                if self.grid[row][curr] == self.grid[row][prev]:
                    self.grid[row][prev] = 2 * self.grid[row][curr]
                    self.grid[row][curr] = 0
                    prev = -1
                    changed = True
                else:
                    if self.grid[row][curr] != 0:
                        prev = curr
            prev = -1
        
        for row in range(len(self.grid)):
            temp = []
            for element in range(len(self.grid[row])-1,-1,-1):
                if self.grid[row][element] != 0:
                    temp.insert(0,self.grid[row][element])
            while len(temp) < len(self.grid[row]):
                temp.insert(0,0)
            if self.grid[row] != list(temp):
                self.grid[row] = list(temp)
                changed = True
        if changed:
            self.spawn_new_tile()
        
    def spawn_new_tile(self):
        new_tile = (random.randint(0,self.size-1), random.randint(0,self.size-1))
        while self.grid[new_tile[0]][new_tile[1]] != 0:
            new_tile = (random.randint(0,self.size-1), random.randint(0,self.size-1))
        self.spawn_tile(new_tile[0],new_tile[1])
        
        if not any(0 in r for r in self.grid):
            self.gameover = True
            prev = -1
            for row in range(len(self.grid)):
                for curr in range(len(self.grid[row])):
                    if prev == -1:
                        prev = curr
                        continue
                    if self.grid[row][curr] == self.grid[row][prev]:
                        self.gameover = False
                        prev = -1
                        break
                    else:
                        prev = curr
                prev = -1
            prev = -1
            for col in range(len(self.grid)):
                for curr in range(len(self.grid[col])):
                    if prev == -1:
                        prev = curr
                        continue
                    if self.grid[curr][col] == self.grid[prev][col]:
                        self.gameover = False
                        prev = -1
                        break
                    else:
                        prev = curr
                prev = -1
        
        if any(2048 in rw for rw in self.grid):
            self.won = True
        
            

    def display_tile(self,number,x,y):
        screen.blit(image_dict[number],(x,y))
        

size_chosen = False
size = 0
board = Board(4)

while True:
    if not size_chosen:
        option2 = pygame.Rect(35,200,120,120)
        option3 = pygame.Rect(225,200,120,120)
        option4 = pygame.Rect(415,200,120,120)
        option5 = pygame.Rect(605,200,120,120)
        option6 = pygame.Rect(795,200,120,120)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option2.collidepoint(mouse_pos):
                    board = Board(2)
                    size_chosen = True
                if option3.collidepoint(mouse_pos):
                    board = Board(3)
                    size_chosen = True
                if option4.collidepoint(mouse_pos):
                    board = Board(4)
                    size_chosen = True
                if option5.collidepoint(mouse_pos):
                    board = Board(5)
                    size_chosen = True
                if option6.collidepoint(mouse_pos):
                    board = Board(6)
                    size_chosen = True
        screen.fill(white)
        txtsurf = font.render("Welcome to 2048! Choose the size of the board:", True, black)
        screen.blit(txtsurf, (25,50))

        pygame.draw.rect(screen, black, option2, 10)
        pygame.draw.rect(screen, black, option3, 10)
        pygame.draw.rect(screen, black, option4, 10)
        pygame.draw.rect(screen, black, option5, 10)
        pygame.draw.rect(screen, black, option6, 10)
        txtsurf = font.render("2x2", True, black)
        screen.blit(txtsurf, (75,240))
        txtsurf = font.render("3x3", True, black)
        screen.blit(txtsurf, (265,240))
        txtsurf = font.render("4x4", True, black)
        screen.blit(txtsurf, (455,240))
        txtsurf = font.render("5x5", True, black)
        screen.blit(txtsurf, (645,240))
        txtsurf = font.render("6x6", True, black)
        screen.blit(txtsurf, (835,240))





        pygame.display.flip()
        clock.tick(60)
    elif size_chosen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT or event.key == pygame.K_a and not board.gameover:
                    board.left_pressed()
                if event.key == pygame.K_UP or event.key == pygame.K_w and not board.gameover:
                    board.up_pressed()
                if event.key == pygame.K_DOWN or event.key == pygame.K_s and not board.gameover:
                    board.down_pressed()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d and not board.gameover:
                    board.right_pressed()
                if event.key == pygame.K_r:
                    board = Board(board.size)
                if event.key == pygame.K_q:
                    size_chosen = False

                    
        screen.fill(white)
        pygame.draw.rect(screen, background, (50, 50, board.size*100, board.size*100))
        

        for i in range(len(board.grid)):
            for j in range(len(board.grid[i])):
                value = board.grid[i][j]
                if value != 0:
                    board.display_tile(value, j*100+50, i*100+50)

        for y in range(50, board.size*100+150, 100):
            pygame.draw.line(screen, edges, (50, y), (board.size*100+50, y), 5)
        for x in range(50, board.size*100+150, 100):
            pygame.draw.line(screen, edges, (x, 50), (x, board.size*100+50), 5)

        if board.gameover:
            txtsurf = font.render("Game Over!", True, black)
            screen.blit(txtsurf, (10,5))

        if board.won and not board.gameover:
            txtsurf = font.render("You Won! (but you can keep playing)", True, black)
            screen.blit(txtsurf, (10,5))
        
        txtsurf = font.render("Controls:", True, black)
        screen.blit(txtsurf, (700,50))
        txtsurf = font.render("W or ↑: Up", True, black)
        screen.blit(txtsurf, (700,80))
        txtsurf = font.render("A or ←: Left", True, black)
        screen.blit(txtsurf, (700,110))
        txtsurf = font.render("S or ↓: Down", True, black)
        screen.blit(txtsurf, (700,140))
        txtsurf = font.render("D or →: Right", True, black)
        screen.blit(txtsurf, (700,170))
        txtsurf = font.render("R: Reset game", True, black)
        screen.blit(txtsurf, (700,200))
        txtsurf = font.render("Q: Return to menu", True, black)
        screen.blit(txtsurf, (700,230))
        txtsurf = font.render("esc: Quit game", True, black)
        screen.blit(txtsurf, (700,260))

        
        pygame.display.flip()
        clock.tick(60)

