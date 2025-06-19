import random


def hangman():
    word_list = ["Giannis", "Lebron", "Harden", "Curry", "Durant", "Morant", "Booker", "Doncic", "Butler"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["", "________      ",                                                               
              "|      |      ",                                                               
              "|      0      ",                                                               
              "|     /|\     ",                                                               
              "|     / \     ",                                                               
              "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('ハングマンへようこそ')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("文字を予想してね")
        if guess in remaining_letters:character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('あなたの勝ち!' )
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('あなたの負け! 正解は {}'.format(word))

hangman()
                                                              34,9         末尾


          
                                                              1,13         先頭

