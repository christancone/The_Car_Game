import pygame as pg

class car(object):
    def __init__(self, x, y, h, w):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((255, 255, 0))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


def main():
    pg.init()

    dis_h = 500
    dis_w = 400

    sc = pg.display.set_mode((dis_w, dis_h))

    pg.display.set_caption("The car game")
    
    font = pg.font.Font("freesansbold.ttf", 15)

    text = font.render("Engine ", True, (255, 255, 255))

    textRect = text.get_rect()
    textRect.center = (40, dis_h-15)

    clock = pg.time.Clock()

    car_x = dis_w / 2
    car_y = dis_h / 2
    car_h = 20
    car_w = 10

    close = False
    while not close:
        engine = (255, 0, 0)
        for e in pg.event.get():
            if e.type == pg.QUIT:
                close = True
    
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] or keys[pg.K_RIGHT] or keys[pg.K_DOWN] or keys[pg.K_LEFT]:
            engine = (0, 255, 0)
        if keys[pg.K_RIGHT] or keys[pg.K_LEFT]:
            car_h = 10
            car_w = 20
        elif keys[pg.K_UP] or keys[pg.K_DOWN]:
            car_h = 20
            car_w = 10

        if  keys[pg.K_UP]:
            car_y -= 1
        elif  keys[pg.K_RIGHT]:
            car_x += 1

        elif  keys[pg.K_DOWN]:
            car_y += 1   
        elif  keys[pg.K_LEFT]:
            car_x -= 1   
    
        sc.fill((0, 0, 0))
        sc.blit(text, textRect)
        pg.draw.circle(sc, engine, (100, dis_h - 15), 5)
        car(car_x, car_y, car_h, car_w).draw(sc)
        pg.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
