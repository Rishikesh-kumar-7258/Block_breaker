from Classes.bubbles import Bubble

def level1(row_count, col_count, bubbles , all_sprites, score_height, color, size):
    for i in range(row_count):
        for j in range(col_count):
            bubble = Bubble(size[0], size[1], color)
            bubble.rect.x = j*(size[0]+5) + 10
            bubble.rect.y = i*(size[1]+5) + score_height + 2
            bubbles.add(bubble)
            all_sprites.add(bubble)

def level2(row_count, col_count, bubbles , all_sprites, score_height, color, size):
    for i in range(row_count):
        spaces = (col_count // 2) - (2 * i)
        temp = (col_count - spaces) // 2
        invert = False
        for j in range(col_count):
            if temp <= 0 and spaces >= 0 and invert:
                spaces += 1
            if temp <= 0 and spaces > 0 :
                spaces -= 1
                # if spaces == 0 : invert = True
                continue
            bubble = Bubble(size[0], size[1], color)
            bubble.rect.x = j*(size[0]+5) + 10
            bubble.rect.y = i*(size[1] + 5) + score_height + 2
            bubbles.add(bubble)
            all_sprites.add(bubble)
            temp -= 1