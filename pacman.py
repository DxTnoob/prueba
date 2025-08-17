import curses
import time

BOARD = [
    "##########",
    "#........#",
    "#.####...#",
    "#.#......#",
    "#.#.##...#",
    "#.#......#",
    "#.######.#",
    "#........#",
    "##########",
]

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    pacman = [1, 1]
    dots = {(r, c) for r, row in enumerate(BOARD) for c, ch in enumerate(row) if ch == '.'}
    while True:
        stdscr.clear()
        for r, row in enumerate(BOARD):
            for c, ch in enumerate(row):
                if [r, c] == pacman:
                    stdscr.addch(r, c, 'C')
                elif (r, c) in dots:
                    stdscr.addch(r, c, '.')
                else:
                    stdscr.addch(r, c, ch)
        stdscr.refresh()
        key = stdscr.getch()
        if key in (ord('q'), 27):
            break
        dr = dc = 0
        if key == curses.KEY_UP:
            dr = -1
        elif key == curses.KEY_DOWN:
            dr = 1
        elif key == curses.KEY_LEFT:
            dc = -1
        elif key == curses.KEY_RIGHT:
            dc = 1
        nr, nc = pacman[0] + dr, pacman[1] + dc
        if BOARD[nr][nc] != '#':
            pacman = [nr, nc]
        dots.discard((pacman[0], pacman[1]))
        if not dots:
            stdscr.addstr(len(BOARD) + 1, 0, "You win! Press q to quit.")
            stdscr.nodelay(False)
            while True:
                if stdscr.getch() in (ord('q'), ord('Q'), 27):
                    return
        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
