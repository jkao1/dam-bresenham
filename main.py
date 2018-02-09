XRES = 500
YRES = 500
MAX_COLOR = 255
DEFAULT_COLOR = [255] * 3
DEFAULT_LINE_COLOR = [0] * 3

def new_screen(width = XRES, height = YRES):
    return [[DEFAULT_COLOR[:] for _ in range(width)] for _ in range(height)]

def plot(screen, x, y, color = DEFAULT_LINE_COLOR):
    screen[y][x] = color

def draw_line(screen, x0, y0, x1, y1):
    A = y1 - y0
    B = x0 - x1
    x = x0
    y = y0
    slope = A / (-1.0 * B)
    if slope >= 0 and slope <= 1: # octant 1
        d = 2*A + B
        while x <= x1 and y <= y1:
            plot(screen, x, y)
            if d > 0:
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

def screen_to_string(screen):
    return ' '.join([' '.join(' '.join([str(x) for x in color]) for color in row) for row in screen])

def save_ppm(screen, fname = 'foo.ppm'):
    with open(fname, 'w') as f:
        ppm = 'P3\n{} {} {}\n{}\n'.format(
            len(screen[0]),
            len(screen),
            MAX_COLOR,
            screen_to_string(screen)
        )
        f.write(ppm)

def main():
    screen = new_screen()
    draw_line(screen, 0, 0, 200, 100)
    save_ppm(screen)

if __name__ == '__main__':
    main()
