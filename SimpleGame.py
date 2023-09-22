""" 
A comment describing the game module
"""
import PySimpleGUI as sg
import random

import cmd_parser.command_manager as cm


def modal_map_window():

    # Extra fun :-) !
    place_width = 100
    off_set = place_width/2

    def to_pos(pLoc):
        return 10 + (pLoc*place_width)

    map_structure = {key: [cm.game_places[key][next_place][1] for next_place in cm.game_places[key]
                           if next_place != "Story" and next_place != "Image"]
                     for key in cm.game_places}

    total_places = len(map_structure)
    print(total_places, map_structure)
    # draw the map with two way paths
    # create a set of edges.
    edges = ()
    for key in map_structure:
        for place in map_structure[key]:
            edge = tuple(frozenset((key, place)))
            if edge not in edges:
                edges += (edge,)

    print(edges)

    locations = {key: (random.randint(0, total_places - 1),
                       random.randint(0, total_places - 1),)
                 for key in map_structure
                 }

    print(locations)

    # Set up a window with a canvas on it

    can = sg.Canvas(size=((place_width + 10)*total_places, (place_width + 10)
                    * total_places), background_color='grey', key='canvas')
    layout = [[can]]
    window = sg.Window('Canvas Example - Modal Map', layout, finalize=True)

    tkc = can.TKCanvas

    fig = []

    # Draw Edges
    for edge in edges:
        from_row, from_col = locations[edge[0]]
        from_x = to_pos(from_col)
        from_y = to_pos(from_row)

        to_row, to_col = locations[edge[1]]
        to_x = to_pos(to_col)
        to_y = to_pos(to_row)

        fig += [tkc.create_line(from_x+off_set-10, from_y+off_set-10, to_x+off_set-10,
                                to_y+off_set-10, fill='green', width=5)]
    # Draw Places
    prev_location = tuple()

    for key in locations:
        location = locations[key]
        row, col = location
        x = to_pos(col)
        y = to_pos(row)
        colour = "blue"
        show_text = key
        if cm.game_state == key:
            colour = "yellow"
            show_text = "YOU ARE HERE \n"+key
        fig += [tkc.create_oval(x, y, x+off_set, y+off_set, fill=colour),
                tkc.create_text(x, y, text=show_text)
                ]

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    sg.theme('Dark Blue 3')  # please make your windows
    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(
        key='-IN-', size=(20, 1), font='Any 14')]
    buttons = [sg.Button('Show Map'), sg.Button(
        'Enter',  bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    layout = [[sg.Image(r'images/forest.png', size=(100, 100), key="-IMG-"), sg.Text(cm.show_current_place(), size=(300, 8), font='Any 12', key='-OUTPUT-')],
              [command_col]]

    return sg.Window('Adventure Game', layout, size=(640, 400))


if __name__ == "__main__":
    # testing for now - these should be part of a test suite
    # print(show_current_place())
    # current_story = game_play('North')
    # print(show_current_place())

    # A persisent window - stays until "Exit" is pressed
    window = make_a_window()

    while True:
        event, values = window.read()
        print(event)
        if event == 'Enter':
            current_story = cm.game_play(values['-IN-'].lower())

            window['-OUTPUT-'].update(current_story)

            window['-IMG-'].update(r'images/'+cm.game_places[cm.game_state]
                                   ['Image'], size=(100, 100))

            pass
        elif event == 'Show Map':
            modal_map_window()
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break  # out of loop
        else:
            pass

    window.close()
