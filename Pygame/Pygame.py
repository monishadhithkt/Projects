import pygame

pygame.init()

WIDTH = 700
HEIGHT = 700
FPS = 90
COLS = 10
ROWS = 6
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (165, 42, 42)

s = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

# Load sounds outside the Ball class
bounce_sound = pygame.mixer.Sound("Breakout_bounce.wav")
hit_sound = pygame.mixer.Sound("Breakout_hit.wav")


class Bricks():
    def __init__(self):
        self.width = int(WIDTH / COLS)
        self.height = int(HEIGHT / (ROWS * 6))

    def create_bricks(self):
        self.row_bricks = []
        for rows in range(ROWS):
            self.col_bricks = []
            for cols in range(COLS):
                self.x = self.width * cols
                self.y = self.height * rows
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                self.col_bricks.append(self.rect)
            self.row_bricks.append(self.col_bricks)

    def draw_bricks(self):
        for row in self.row_bricks:
            for col in row:
                pygame.draw.rect(s, BLUE, col)
                pygame.draw.rect(s, BLACK, col, 2)


class Paddle():
    def __init__(self):
        self.width = int(WIDTH / COLS)
        self.height = int(HEIGHT / (ROWS * 6))
        self.x = int(WIDTH / 2) - int(self.width / 2)
        self.y = HEIGHT - 50
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_paddle(self):
        pygame.draw.rect(s, WHITE, self.rect)

    def move_paddle(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 5:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] and self.rect.right < WIDTH - 5:
            self.rect.x += self.speed


class Ball():
    def __init__(self, x, y):
        self.game_status = 0
        self.x = x
        self.y = y
        self.radius = 10
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.dx = 3
        self.dy = -3

    def draw_ball(self):
        pygame.draw.circle(s, RED, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)

    def move_ball(self):
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.dx *= -1
            bounce_sound.play()
        if self.rect.top < 0:
            self.dy *= -1
            bounce_sound.play()
        if self.rect.bottom > HEIGHT:
            self.game_status = -1

        if self.rect.colliderect(paddle) and self.dy > 0:
            self.dy *= -1
            bounce_sound.play()

        all_done = True
        row_num = 0
        for rows in bricks.row_bricks:
            col_num = 0
            for col in rows:
                if self.rect.colliderect(col):
                    hit_sound.play()
                    if abs(self.rect.bottom - col.top) < 5 and self.dy > 0:
                        self.dy *= -1
                    if abs(self.rect.top - col.bottom) < 5 and self.dy < 0:
                        self.dy *= -1
                    if abs(self.rect.left - col.right) < 5 and self.dx < 0:
                        self.dx *= -1
                    if abs(self.rect.right - col.left) < 5 and self.dx > 0:
                        self.dx *= -1
                    bricks.row_bricks[row_num][col_num] = pygame.Rect(0, 0, 0, 0)

                if bricks.row_bricks[row_num][col_num] != pygame.Rect(0, 0, 0, 0):
                    all_done = False

                col_num += 1
            row_num += 1

        self.rect.x += self.dx
        self.rect.y += self.dy

        if all_done:
            self.game_status = 1

        return self.game_status


paddle = Paddle()
bricks = Bricks()
ball = Ball(paddle.x + int(paddle.width / 2), paddle.y - 12)
bricks.create_bricks()

run = True
while run:
    clock.tick(FPS)
    s.fill(BLACK)
    paddle.draw_paddle()
    paddle.move_paddle()
    bricks.draw_bricks()
    ball.draw_ball()
    ball.game_status = ball.move_ball()

    if ball.game_status == 1:
        s.fill(BLACK)
        font = pygame.font.SysFont("Arial", 75)
        text = font.render("You Won ", True, BROWN)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        s.blit(text, text_rect)
    if ball.game_status == -1:
        s.fill(BLACK)
        font = pygame.font.SysFont(None, 75)
        text = font.render("Game Over", False, RED)
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        s.blit(text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
