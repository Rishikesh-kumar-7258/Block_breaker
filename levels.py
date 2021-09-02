from Classes.bubbles import Bubble

def test(row_count, col_count, score_height, color, size):
    l = []
    bubble = Bubble(size[0], size[1], color)  
    bubble.x = 200
    bubble.y = 200
    l.append(bubble)

    return l


def level1(row_count, col_count, score_height, color, size):
    for i in range(row_count):
        for j in range(col_count):
            if ((i+j)&1) : continue
            bubble = Bubble(size[0], size[1], color)
            bubble.rect.x = j*(size[0]+5) + 10
            bubble.rect.y = i*(size[1]+5) + score_height + 2


def level2(row_count, col_count, score_height, color, size):
    for i in range(row_count // 2):
        spaces = col_count / 2  - 2*i
        bl = col_count / 4 + i
        for j in range(col_count):
            if (bl <= 0 and spaces > 0):
                spaces -= 1
                continue
            else:
                bubble = Bubble(size[0], size[1], color)
                bubble.rect.x = j*(size[0]+5) + 10
                bubble.rect.y = i*(size[1]+5) + score_height + 2
                bl -= 1
    
    for i in range(0, row_count // 2):
        spaces = col_count // 2  - 2 * (row_count // 2 - i)
        bl = col_count / 4 + (row_count // 2 - i)
        for j in range(col_count):
            if (bl <= 0 and spaces > 0):
                spaces -= 1
                continue
            else:
                bubble = Bubble(size[0], size[1], color)
                bubble.rect.x = j*(size[0]+5) + 10
                bubble.rect.y = i*(size[1]+5) + row_count // 2 * size[0] - size[0] / 2 - 4
                bl -= 1


def level3(row_count, col_count, score_height, color, size):
    for i in range(row_count):
        for j in range(col_count):
            bubble = Bubble(size[0], size[1], color)
            bubble.rect.x = j*(size[0]+5) + 10
            bubble.rect.y = i*(size[1]+5) + score_height + 2