import curses

def print_menu(stdscr, selected_row_idx, menu_items):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu_items):
        x=w//2 - len(row)//2
        y=h//2 - len (menu_items)//2 + idx

        if idx == selected_row_idx:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y,x , row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

def show_message_box (stdscr, title, lines):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(0, 0, f"---{title}---")
    stdscr.attron(curses.A_BOLD)

    for i, line in enumerate(lines):
        if i+2 <h:
            stdscr.addstr(i+2, 0, str(line))
    
    msg = "Press any key to return"
    stdscr.addstr(h-2, 0, msg, curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()
