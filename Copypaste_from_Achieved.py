from tkinter import *

#quit subroutine
def quit():
    main_window.destroy()

#create the buttons and labels
def setup_buttons():
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries, delete_item
    Button(main_window, text="Quit",command=quit) .grid(column=1, row=0)
    Button(main_window, text="Append Details",command=append_name) .grid(column=0,row=1)
    Button(main_window, text="Print Details",command=print_camp_details) .grid(column=1,row=1)
    Label(main_window, text="Leader") .grid(column=0,row=2)
    entry_leader = Entry(main_window)
    entry_leader.grid(column=1,row=2)
    Label(main_window, text="Location") .grid(column=0,row=3)
    entry_location = Entry(main_window)
    entry_location.grid(column=1,row=3)
    Label(main_window, text="Number of Campers") .grid(column=0,row=4)
    entry_campers = Entry(main_window)
    entry_campers.grid(column=1,row=4)
    Label(main_window, text="Weather") .grid(column=0,row=5)
    entry_weather = Entry(main_window)
    entry_weather.grid(column=1,row=5)
    Label(main_window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item .grid(column=1,row=6)
    Button(main_window, text="Delete",command=delete_row) .grid(column=2,row=6)

    #start the program running
def main():
    global main_window
    global camp_details, entry_name,entry_age,entry_gender, total_entries
    camp_details = []
    total_entries = 0
    main_window =Tk()
    setup_buttons()
    main_window.mainloop()