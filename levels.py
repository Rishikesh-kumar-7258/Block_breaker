from ball import Ball

def level1(row_count, col_count, size, bubbles , all_sprites, score_height, color):
    for i in range(row_count):
        for j in range(col_count-1):
            bubble = Ball(size, size, color)
            bubble.rect.x = j*(size+5) + 10
            bubble.rect.y = i*(size+5) + score_height + 2
            bubbles.add(bubble)
            all_sprites.add(bubble)