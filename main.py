#Opens the file and reads it line by line
import meteor_data_class
import PySimpleGUI as sg
from meteor_data_class import MeteorDataEntry

def launchGUI(my_meteor1= None):
    # creating a meteor entry to be used later in the code(NEEDS TO BE OUTSIDE OF FOR LOOP SO DATA IS MAINTAINED AND NOT WRITEN OVER)
    my_meteor1 = MeteorDataEntry('', '', '', '', '3900000', '', '', '', '', '', '', '')

    # All the stuff inside your window.
    layout = [
        # This is where the user will be prompted to put in a year to filter through
        [sg.Text('Minimum Year Limit (0 - 2022, exclusive): >'), sg.InputText(default_text=2012, key='yearU')],
        # This is where the user will be prompted to put in a mass to filter through
        [sg.Text('Minimum Mass Limit (grams, exclusive): >'), sg.InputText(default_text=2900000, key='massU')],
        # These are the buttons at the bottom
        [sg.Button('Apply Filters'), sg.Button('Exit')],
        #This is the year filtered data label
        [sg.Text('Years Filtered Data')],
        #This is the year filtered data field
        [sg.Multiline(key = 'yearT', size=(125, 10))],
        #This is the mas filetered data label
        [sg.Text('Mass Filtered Data')],
        # This is the mass filtered data field
        [sg.Multiline(key = 'massT' ,size=(125, 10))]]


    # Create the Window
    window = sg.Window('Filter Dataset Parameter Input', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Apply Filters':

            yearLimit: int = values['yearU']
            massLimit: int = values['massU']

            # Opens the file and reads
            f = open("Text.txt", 'r')

            # creating a meteor entry to be used later in the code(NEEDS TO BE OUTSIDE OF FOR LOOP SO DATA IS MAINTAINED AND NOT WRITEN OVER)
            my_meteor1 = MeteorDataEntry('', '', '', '', '3900000', '', '', '', '', '', '', '')

            # A count of the line that is read in.
            count = 0

            # IMPORTANT: Need to read first line and throw out because it is the header
            line = f.readline()

            while len(line) > 0:
                count += 1
                # Actually reads in a line from the file
                line = f.readline()

                # if there's no data in the line then it will break out of the while loop
                if not line:
                    break

                # remove end of line character from the line read in
                line = line.strip('\n')

                # Taking a line and splitting it by the tab's and putting it into a variable to use
                x = line.split('\t', 11)

                # IMPORTANT need to see if the file line has all the meteor values
                while (len(x) < 12):
                    x.append('')

                # IMPORTANT need to create a Meteor Data Entry with the list of data read in from a file.
                newMeteor = MeteorDataEntry(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11])

                # Calling to add a meteor to the array
                my_meteor1.addMeat(newMeteor, yearLimit, massLimit)

            # Closes the files so we save memory
            f.close()

            # prints the mass table to the file
            my_meteor1.massTable()

            # write the data to the Mass field on the GUI
            window['massT'].update(my_meteor1.massDataStr)

            # prints the year table to the file
            my_meteor1.yearTable()

            # write the data to the year field on the GUI
            window['yearT'].update(my_meteor1.yearDataStr)

    window.close()
#This runs the program
if __name__ == '__main__':
    launchGUI()