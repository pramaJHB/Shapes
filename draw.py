

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    try:
        shape_list = ['pyramid', 'square', 'triangle', 'diamond', 'rhombus', 'rectangle']
        shape = input('Shape?: ').lower()
        if shape.lower() in shape_list:
            return shape
        else:
            return get_shape()
    except:
        return get_shape()


# TODO: Step 1 - get height (it must be int!)
def get_height():
    try:
        height = int(input('Height?: '))
        if 0 < height <= 80:
            return height
        else:
            return get_height()
    except ValueError:
        return get_height()


# TODO: Step 2
def draw_pyramid(height, outline):
    #print('pyramid')
    if outline == True and height > 2:
        for i in range(0, height - 1):
            print(' ' * (height - i - 1) + '*', end='')
            if i >= 1:
                print(' ' * (2 * i - 1) + '*', end='')
            print("")
        for i in range(height - 1, height):
            print('*' * (height * 2 - 1), end='')
        print('')
    else:
        for i in range(0, height):
            print(' ' * (height - i - 1) + '*' * (i * 2 + 1))
  


# TODO: Step 3
def draw_square(height, outline):
    #print('square')
    if outline == True and height > 2:
        for i in range(0, height - (height - 1)):
            print('*' * height)
        for i in range(height - (height - 1), height - 1):
            print('*' + ' ' * (height - 2) + '*')
        for i in range(height - 1, height):
            print('*' * height)
    else:
        for i in range(0, height):
            print('*' * height)


# TODO: Step 4
def draw_triangle(height, outline):
    #print('triangle')
    if outline == True and height > 2:
        for i in range(0, height - (height - 2)):
            print('*' * (i + 1))
        for i in range(height - (height - 2), height - 1):
            print('*' + ' ' * (i - 1) + '*')
        for i in range(height - 1, height):
            print('*' * height)
    else:
        for i in range(0, height):
            print('*' * (i + 1))


def draw_diamond(height, outline):
    #print('diamond')
    if outline == True:
        for i in range(0, height):
            print(' ' * (height - i - 1) + '*', end='')
            if i >= 1:
                print(' ' * (2 * i - 1) + '*', end='')
            print('')
        for i in range(1, height - 1):
            print(' ' * i + '*', end='')
            print(' ' * ((height * 2) - (i * 2) - 3) + '*', end='')
            print('')
        print(' ' * (height -1) + '*')
    else:
        for i in range(0, height):
            print(' ' * (height - i - 1) + '*' * (2 * i + 1))
        for i in range(0, height - 1):
            print(' ' * (i + 1) + '*' * ((height * 2) - (2 * i) - 3))


def draw_rhombus(height, outline):
    #print('rhombus')
    if outline == True:
        print(' ' * (height - 1) + '*' * height)
        for i in range(1, height - 1):
            print(' ' * (height - i - 1) + '*', end='')
            print(' ' * (height - 2) + '*', end='')
            print('')
        print('*' * height)
    else:
        for i in range(0, height):
            print(' ' * (height - i -1) + '*' * height)

def draw_rectangle(height, outline):
    #print('rectangle')
    if outline == True:
        print('*' * height * 4)
        for i in range(1, height - 1):
            print('*' + ' ' * (height * 4 - 2) + '*')
        print('*' * height * 4)
    else:
        for i in range(0, height):
            print('*' * height * 4)



# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == 'pyramid':
        draw_pyramid(height, outline)
    if shape == 'square':
        draw_square(height, outline)
    if shape == 'triangle':
        draw_triangle(height, outline)
    if shape == 'diamond':
        draw_diamond(height, outline)
    if shape == 'rhombus':
        draw_rhombus(height, outline)
    if shape == 'rectangle':
        draw_rectangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = input('Outline only? (y/n):')
    if outline == 'y':
        return True
    if outline == 'n':
        return False
    if outline == '':
        return False
    else:
        get_outline()


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

