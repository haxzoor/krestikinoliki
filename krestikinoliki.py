def print_board(board):
    for i in range(0, 25, 5):
        row = ["{:>2}".format(cell) for cell in board[i:i + 5]]
        print(" | ".join(row))
        if i < 20:
            print("-" * 29)

def check_winner(board):
    # Проверка строк, столбцов и диагоналей
    for i in range(5):
        if all(board[i + j * (1 if i == 0 else 5)] == board[i] for j in range(5)) and board[i] in ['X', 'O']:
            return True

    # Проверка диагоналей
    if all(board[i * 6] == board[0] for i in range(5)) or all(board[i * 4 + 4] == board[4] for i in range(1, 6)):
        return True

    return False

def is_board_full(board):
    return all(cell in ['X', 'O'] for cell in board)

def reset_board():
    return [str(i + 1) for i in range(25)]

def main():
    while True:
        board = reset_board()
        current_player = 'X'

        while True:
            print_board(board)
            print(f"\nХод игрока {current_player}")

            try:
                move = int(input("Выберите номер клетки для хода (1-25): "))
                if board[move - 1] not in ['X', 'O']:
                    board[move - 1] = current_player
                else:
                    print("Эта клетка уже занята. Попробуйте снова.")
                    continue
            except (ValueError, IndexError):
                print("Введите корректное число от 1 до 25.")
                continue

            if check_winner(board):
                print_board(board)
                4
                
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
