import PySimpleGUI as sg

layout =  [[sg.Text('X Starts First')]]
layout += [[sg.Button(size=(3,2), key=(row,col)) for col in range(3)] for row in range(3)]
layout += [[sg.Button('Reset'), sg.Button('Cancel')]]

window = sg.Window('Window Title', layout, use_default_focus=False)

board, player = {}, 0

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Reset':
        board = {}
        for row in range(3):
            for col in range(3):
                window[(row, col)].update(' ')
    elif event not in board:
        board[event] = player
        window[event].update('O' if player else 'X')
        player = (player+1) % 2
window.close()
