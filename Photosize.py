import PySimpleGUI as sg

def resize_file_inches(valores):
    height_px = float(valores['height_px'])
    lenght_px = float(valores['lenght_px'])
    new_res = float(valores['resolution'])

    new_height = height_px / new_res
    new_lenght = lenght_px / new_res
    return round(new_height, 1), round(new_lenght, 1), round(new_res)

def resize_file_cms(valores):
    CMPERINCHES = 2.54
    height_px = float(valores['height_px'])
    lenght_px = float(valores['lenght_px'])
    new_res = float(valores['resolution'])

    new_height = (height_px / new_res) * CMPERINCHES
    new_lenght = (lenght_px / new_res) * CMPERINCHES
    return round(new_height, 1), round(new_lenght, 1), round(new_res)

def calculate_res_having_height_px(valores):
    height_px = float(valores['current_height'])
    lenght_px = float(valores['current_lenght'])
    res = float(valores['current_res'])

    new_height = float(valores['height_needed'])
    new_res = (height_px / new_height) * 2.54  # cm per inches
    new_lenght = (lenght_px / new_res) * 2.54  # cm per inches

    return round(new_height, 1), round(new_lenght, 1), round(new_res)

def calculate_res_having_lenght_px(valores):
    height_px = float(valores['current_height'])
    lenght_px = float(valores['current_lenght'])
    res = float(valores['current_res'])

    new_lenght = float(valores['lenght_needed'])
    new_res = (lenght_px / new_lenght) * 2.54
    new_height = (height_px / new_res) * 2.54

    return round(new_height, 1), round(new_lenght, 1), round(new_res)

def calculate_res_having_height_cm(valores):
    height_cm = float(valores['current_height'])
    lenght_cm = float(valores['current_lenght'])
    res = float(valores['current_res'])

    height_px = height_cm * res * (1/2.54)
    lenght_px = lenght_cm * res * (1/2.54)

    new_height = float(valores['height_needed'])
    new_res = (height_px / new_height) * 2.54
    new_lenght = (lenght_px / new_res) * 2.54

    return round(new_height, 1), round(new_lenght, 1), round(new_res)

def calculate_res_having_lenght_cm(valores):
    height_cm = float(valores['current_height'])
    lenght_cm = float(valores['current_lenght'])
    res = float(valores['current_res'])

    height_px = height_cm * res * (1 / 2.54)
    lenght_px = lenght_cm * res * (1 / 2.54)

    new_lenght = float(valores['lenght_needed'])
    new_res = (lenght_px / new_lenght) * 2.54
    new_height = (height_px / new_res) * 2.54

    return round(new_height, 1), round(new_lenght, 1), round(new_res)

def main():
    sg.theme('DarkPurple1')

    while True:
        main_menu_layout = [[sg.Text('Welcome to PhotoSize®')],
                            [sg.Text('What do you want to do?')],
                            [sg.Button('Resize picture for specific resolution', size=60, key='resize_option')],
                            [sg.Button('Calculate new resolution for specific size having current px', size=60,
                                       key='newreshavingpx')],
                            [sg.Button('Calculate new resolution for specific size having current cm', size=60,
                                       key='newreshavingcm')],

                            [sg.Text(size=(100, 1), key='-OUTPUT-')],
                            [sg.Button('Salir')],
                            ]
        main_menu_window = sg.Window('Photosize® by Rai', main_menu_layout)
        event, values = main_menu_window.read()  # aquí el programa descansa

        if event == 'Salir' and type(event) != None:
            break

        if event == 'resize_option':  # entro al menu resize
            main_menu_window.close()  # cierro el menu principal
            resize_layout = [[sg.Text('Given the current size and a new resolution calculate the new size.')],
                             [sg.Text()],
                             [sg.Text('Current height (px):', size=30), sg.Input(size=5, key='height_px'), sg.Text('px')],
                             [sg.Text('Current lenght (px): ', size=30), sg.Input(size=5, key='lenght_px'), sg.Text('px')],
                             [sg.Text('What resolution do you want for the file? (dpi):', size=30),
                              sg.Input(size=5, key='resolution'), sg.Text('dpi')],
                             [sg.Checkbox('Do you want to receive the new size in inches (in)?', key='inches',
                                          default=False)],
                             [sg.Text()],
                             [sg.Button('Salir'), sg.Button('Resize', key='resize')],
                             ]
            resize_window = sg.Window('Photosize® by Rai', resize_layout)
            event, values = resize_window.read()

            if event == 'resize' and values['inches'] == True:
                resize_window.close()  # cierro ventana de datos para resize

                input_height = str(resize_file_inches(values)[0])
                input_lenght = str(resize_file_inches(values)[1])
                input_res = str(resize_file_inches(values)[2])

                resized_layout_inch = [[sg.Text('¡RESIZED!')],
                                       [sg.Text()],
                                       [sg.Text('The new dimentions are:')],
                                       [sg.Text()],
                                       [sg.Text('Height: ' + input_height + ' in')],
                                       [sg.Text('Lenght: ' + input_lenght + ' in')],
                                       [sg.Text('Current resolution: ' + input_res + ' dpi')],
                                       [sg.Text()],
                                       [sg.Button('Salir'), sg.Button('Back to Home', key='home')],
                                       ]
                resized_window_inch = sg.Window('Photosize® by Rai', resized_layout_inch)

                event, values = resized_window_inch.read()

                if event == 'Salir' and type(event) != None: # boton de salida
                    break

                elif event == 'home': # boton HOME
                    resized_window_inch.close()

            if event == 'resize' and values['inches'] == False:
                resize_window.close()  # cierro ventana de datos para resize

                input_height = str(resize_file_cms(values)[0])
                input_lenght = str(resize_file_cms(values)[1])
                input_res = str(resize_file_cms(values)[2])
                resized_layout_cm = [[sg.Text('¡RESIZED!')],
                                     [sg.Text()],
                                     [sg.Text('The new dimentions are:')],
                                     [sg.Text()],
                                     [sg.Text('Height: ' + input_height + ' cm')],
                                     [sg.Text('Lenght: ' + input_lenght + ' cm')],
                                     [sg.Text('Current resolution: ' + input_res + ' dpi')],
                                     [sg.Text()],
                                     [sg.Button('Salir', key='Salir'), sg.Button('Back to Home', key='home')],
                                     ]
                resized_window_cm = sg.Window('Photosize® by Rai', resized_layout_cm)

                event, values = resized_window_cm.read() # aqui el programa descansa

                if event == 'Salir' and type(event) != None:  # boton de salida
                    break

                elif event == 'home':  # boton HOME
                    resized_window_cm.close()

        if event == 'newreshavingpx':
            main_menu_window.close()
            newreshavingpx_layout = [[sg.Text('Given the current size and resolution calculate the new resolution for a new size.')],
                                    [sg.Text()],
                                    [sg.Text('Witch dimention do you have already defined?')],
                                    [sg.Button('Height', key='height_defined'), sg.Button('Lenght', key='lenght_defined')],
                                    [sg.Button('Salir', key='Salir')],
                                    ]

            newreshavingpx_window = sg.Window('Photosize® by Rai', newreshavingpx_layout)
            event, values = newreshavingpx_window.read()

            if event == 'height_defined':
                newreshavingpx_window.close()
                height_defined_layout = [[sg.Text('With a defined height you resize the photo and recalculate the resolution')],
                                         [sg.Text()],
                                         [sg.Text('Current height (px): ', size=30), sg.Input(size=5, key='current_height'), sg.Text('px')],
                                         [sg.Text('Current lenght (px): ', size=30), sg.Input(size=5, key='current_lenght'),
                                          sg.Text('px')],
                                         [sg.Text('Current resolution (pdi): ', size=30), sg.Input(size=5, key='current_res'), sg.Text('dpi')],
                                         [sg.Text('Height needed (cm): ', size=30), sg.Input(size=5, key='height_needed'), sg.Text('cm')],
                                         [sg.Button('Recalculate Resolution', key='calculate_res')],
                                         ]
                height_defined_window = sg.Window('Photosize® by Rai', height_defined_layout)
                event, values = height_defined_window.read()

                if event == 'calculate_res':
                    height_defined_window.close()

                    input_height = str(calculate_res_having_height_px(values)[0])
                    input_lenght = str(calculate_res_having_height_px(values)[1])
                    input_res = str(calculate_res_having_height_px(values)[2])

                    resolution_calculated_layout = [[sg.Text('¡RESOLUTION CALCULATED!')],
                                                    [sg.Text()],
                                                    [sg.Text('The new dimentions are:')],
                                                    [sg.Text()],
                                                    [sg.Text('Height: ' + input_height + ' cm')],
                                                    [sg.Text('Lenght: ' + input_lenght + ' cm')],
                                                    [sg.Text('Current resolution: ' + input_res + ' dpi')],
                                                    [sg.Text()],
                                                    [sg.Button('Salir'), sg.Button('Back to Home', key='home')],
                                                   ]

                    resolution_calculated_window = sg.Window('Photosize® by Rai', resolution_calculated_layout)
                    event, values = resolution_calculated_window.read()

                    if event == 'Salir':
                        break

                    if event == 'home':
                        resolution_calculated_window.close()

            if event == 'lenght_defined':
                newreshavingpx_window.close()

                lenght_defined_layout = [[sg.Text('With a defined lenght you resize the photo and recalculate the resolution')],
                                         [sg.Text()],
                                         [sg.Text('Current height (px): ',size=30), sg.Input(size=5, key='current_height'), sg.Text('px')],
                                         [sg.Text('Current lenght (px): ', size=30), sg.Input(size=5, key='current_lenght'),sg.Text('px')],
                                         [sg.Text('Current resolution (pdi): ', size=30),sg.Input(size=5, key='current_res'), sg.Text('dpi')],
                                         [sg.Text('Lenght needed (cm): ', size=30), sg.Input(size=5, key='lenght_needed'),sg.Text('cm')],
                                         [sg.Button('Recalculate Resolution', key='calculate_res')]
                                         ]

                lenght_defined_window = sg.Window('Photosize® by Rai', lenght_defined_layout)
                event, values = lenght_defined_window.read()

                if event == 'calculate_res':
                    lenght_defined_window.close()

                    input_height = str(calculate_res_having_lenght_px(values)[0])
                    input_lenght = str(calculate_res_having_lenght_px(values)[1])
                    input_res = str(calculate_res_having_lenght_px(values)[2])

                    resolution_calculated_layout = [[sg.Text('¡RESOLUTION CALCULATED!')],
                                                    [sg.Text()],
                                                    [sg.Text('The new dimentions are:')],
                                                    [sg.Text()],
                                                    [sg.Text('Height: ' + input_height + ' cm')],
                                                    [sg.Text('Lenght: ' + input_lenght + ' cm')],
                                                    [sg.Text('New resolution: ' + input_res + ' dpi')],
                                                    [sg.Text()],
                                                    [sg.Button('Salir', key='Salir'), sg.Button('Back to Home', key='home')]
                                                    ]

                    resolution_calculated_window = sg.Window('Photosize® by Rai', resolution_calculated_layout)
                    event, values = resolution_calculated_window.read()

                    if event == 'Salir':
                        break

                    elif event == 'home':
                        resolution_calculated_window.close()

        if event == 'newreshavingcm':
            main_menu_window.close()

            newreshavingcm_layout = [[sg.Text('Given the current size and resolution calculate the new resolution for a new size.')],
                                     [sg.Text()],
                                     [sg.Text('Witch dimention do you have already defined?')],
                                     [sg.Button('Height', key='height_defined'), sg.Button('Lenght', key='lenght_defined')],
                                     [sg.Button('Salir', key='Salir')],
                                    ]

            newreshavingcm_window = sg.Window('Photosize® by Rai', newreshavingcm_layout)
            event, values = newreshavingcm_window.read()

            if event == 'height_defined':
                newreshavingcm_window.close()
                height_defined_layout = [[sg.Text('With a defined height you resize the photo and recalculate the resolution')],
                                         [sg.Text()],
                                         [sg.Text('Current height (cm): ', size=30), sg.Input(size=5, key='current_height'), sg.Text('cm')],
                                         [sg.Text('Current lenght (cm): ', size=30), sg.Input(size=5, key='current_lenght'),sg.Text('cm')],
                                         [sg.Text('Current resolution (dpi): ', size=30), sg.Input(size=5, key='current_res'), sg.Text('dpi')],
                                         [sg.Text('Height needed (cm): ', size=30), sg.Input(size=5, key='height_needed'), sg.Text('cm')],
                                         [sg.Button('Recalculate Resolution', key='calculate_res')]
                                         ]
                height_defined_window = sg.Window('Photosize® by Rai', height_defined_layout)
                event, values = height_defined_window.read()

                if event == 'calculate_res':
                    height_defined_window.close()

                    input_height = str(calculate_res_having_height_cm(values)[0])
                    input_lenght = str(calculate_res_having_height_cm(values)[1])
                    input_res = str(calculate_res_having_height_cm(values)[2])

                    resolution_calculated_layout = [[sg.Text('¡RESOLUTION CALCULATED!')],
                                                    [sg.Text()],
                                                    [sg.Text('The new dimentions are:')],
                                                    [sg.Text()],
                                                    [sg.Text('Height: ' + input_height + ' cm')],
                                                    [sg.Text('Lenght: ' + input_lenght + ' cm')],
                                                    [sg.Text('Current resolution: ' + input_res + ' dpi')],
                                                    [sg.Text()],
                                                    [sg.Button('Salir'), sg.Button('Back to Home', key='home')],
                                                    ]

                    resolution_calculated_window = sg.Window('Photosize® by Rai', resolution_calculated_layout)
                    event, values = resolution_calculated_window.read()

                    if event == 'Salir':
                        break

                    if event == 'home':
                        resolution_calculated_window.close()

            if event == 'lenght_defined':
                newreshavingcm_window.close()

                lenght_defined_layout = [
                    [sg.Text('With a defined lenght you resize the photo and recalculate the resolution')],
                    [sg.Text()],
                    [sg.Text('Current height (cm): ', size=30), sg.Input(size=5, key='current_height'), sg.Text('cm')],
                    [sg.Text('Current lenght (cm): ', size=30), sg.Input(size=5, key='current_lenght'), sg.Text('cm')],
                    [sg.Text('Current resolution (dpi): ', size=30), sg.Input(size=5, key='current_res'), sg.Text('dpi')],
                    [sg.Text('Lenght needed (cm): ', size=30), sg.Input(size=5, key='lenght_needed'), sg.Text('cm')],
                    [sg.Button('Recalculate Resolution', key='calculate_res')]
                    ]

                lenght_defined_window = sg.Window('Photosize® by Rai', lenght_defined_layout)
                event, values = lenght_defined_window.read()

                if event == 'calculate_res':
                    lenght_defined_window.close()

                    input_height = str(calculate_res_having_lenght_cm(values)[0])
                    input_lenght = str(calculate_res_having_lenght_cm(values)[1])
                    input_res =    str(calculate_res_having_lenght_cm(values)[2])

                    resolution_calculated_layout = [[sg.Text('¡RESOLUTION CALCULATED!')],
                                                    [sg.Text()],
                                                    [sg.Text('The new dimentions are:')],
                                                    [sg.Text()],
                                                    [sg.Text('Height: ' + input_height + ' cm')],
                                                    [sg.Text('Lenght: ' + input_lenght + ' cm')],
                                                    [sg.Text('New resolution: ' + input_res + ' dpi')],
                                                    [sg.Text()],
                                                    [sg.Button('Salir', key='Salir'), sg.Button('Back to Home', key='home')]
                                                    ]

                    resolution_calculated_window = sg.Window('Photosize® by Rai', resolution_calculated_layout)
                    event, values = resolution_calculated_window.read()

                    if event == 'Salir':
                        break

                    elif event == 'home':
                        resolution_calculated_window.close()

    main_menu_window.close()

if __name__ == '__main__':
    main()