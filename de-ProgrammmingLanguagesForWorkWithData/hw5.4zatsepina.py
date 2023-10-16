import random

class Cell:
    def __init__(self, position):
        self.position = position
        self.content = position

    def is_empty(self):
        return type(self.content) == int

    def put_mark(self, mark):
        if self.is_empty():
            self.content = mark
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def show(self):
        for i in range(0, 9, 3):
            print(f"  {self.cells[i].content} | {self.cells[i + 1].content} |"
                  f" {self.cells[i + 2].content} ")

    def is_full(self):
        return all(not cell.is_empty() for cell in self.cells)

    def check_win(self, mark):
        for i in range(0, 9, 3):
            if all(self.cells[i + j].content == mark for j in range(3)):
                return True
        for i in range(3):
            if all(self.cells[i + j * 3].content == mark for j in range(3)):
                return True
        if self.cells[0].content == self.cells[4].content == self.cells[8].content:
            return True
        if self.cells[2].content == self.cells[4].content == self.cells[6].content:
            return True
        return False


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def move(self, board, cell_number):
        if 1 <= cell_number <= 9:
            cell = board.cells[cell_number - 1]
            if cell.put_mark(self.mark):
                return True
        return False


def game_for_two():
    board = Board()
    player1 = Player(input("Кто за Х? "), "X")
    player2 = Player(input("Кто за О? "), "O")
    current_player = player1

    while True:
        board.show()
        cell_number = int(input(f"\n{current_player.name}, ходит: "))
        if current_player.move(board, cell_number):
            if board.check_win(current_player.mark):
                board.show()
                print(f"{current_player.name} выиграл")
                break
            elif board.is_full():
                board.show()
                print("Ничья")
                break
            else:
                current_player = player2 if current_player == player1 else player1
        else:
            print("Неверный ход")


def game_with_computer():
    board = Board()
    list_of_empty_cells = [i for i in range(1, 10)]
    name = input("Как тебя зовут? ")
    mark = input("Будешь играть за Х или О? ")
    if mark == "Х":
        player1 = Player(name, "Х")
        player2 = Player("computer", "О")
    else:
        player1 = Player("computer", "Х")
        player2 = Player(name, "О")
    current_player = player1
    while True:
        board.show()
        if current_player.name == "computer":
            cell_number = random.choice(list_of_empty_cells)
            print(f"computer пошел на {cell_number}:")
        else:
            cell_number = int(input(f"\n{current_player.name}, ходит: "))
        try:
            list_of_empty_cells.remove(cell_number)
        except ValueError:
            print("Неверный ход")
        if current_player.move(board, cell_number):
            if board.check_win(current_player.mark):
                board.show()
                print(f"{current_player.name} выиграл")
                break
            elif board.is_full():
                board.show()
                print("Ничья")
                break
            else:
                current_player = player2 if current_player == player1 else player1
        else:
            print("Попробуй другую клетку")


game_for_two()
game_with_computer()