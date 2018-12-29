from tkinter import *
from PIL import ImageTk, Image

BUTTON_WIDHT_HEIGHT_MAIN_FRAME = (25, 2)
BUTTONWIDTH_TOPLEVELS = 18

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.main_Label = Label(frame, text="Verwaltungssystem")
        self.main_Label.pack(side=TOP, padx=10, pady=10)

        self.slogan = Button(frame, text="Prüfung anlegen", command=self.PrufungsverwaltungWindow, width=BUTTON_WIDHT_HEIGHT_MAIN_FRAME[0], height=BUTTON_WIDHT_HEIGHT_MAIN_FRAME[1])
        self.slogan.pack(side=TOP,  padx=10, pady=10)

        self.slogan = Button(frame, text="Studierenden anlegen", command=self.StudierendenverwaltungFenster, width=BUTTON_WIDHT_HEIGHT_MAIN_FRAME[0], height=BUTTON_WIDHT_HEIGHT_MAIN_FRAME[1])
        self.slogan.pack(side=BOTTOM,  padx=10, pady=10)

        self.slogan = Button(frame, text="Noten eingeben", command=self.NotenVerwaltungsFenster, width=BUTTON_WIDHT_HEIGHT_MAIN_FRAME[0], height=BUTTON_WIDHT_HEIGHT_MAIN_FRAME[1])
        self.slogan.pack(side=BOTTOM,  padx=10, pady=10)

        self.slogan = Button(frame, text="Noten eines Studenten ausgeben", width=BUTTON_WIDHT_HEIGHT_MAIN_FRAME[0], height=BUTTON_WIDHT_HEIGHT_MAIN_FRAME[1])
        self.slogan.pack(side=BOTTOM,  padx=10, pady=10)

        self.im = Image.open("images-12.jpeg")
        self.photo = ImageTk.PhotoImage(self.im)

        self.panel = Label(root, image = self.photo)
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")



    def PrufungsverwaltungWindow(self):

        newwin = Toplevel(root)

        #self.resizen(newwin)

        # Um zu verhindern, dass 1. mehrere Instanzen erstellt werden können und
        # während dieses Fenster existiert kann man nicht auf andere Fenster zugreifen,
        # bis dies geschlossen ist
        newwin.grab_set()
        newwin.focus_set()

        '''Labels'''
        Label(newwin, text="Prüfungsverwaltung").grid(row=0, column=2)

        Label(newwin, text="PNr").grid(row=1, column=0)

        Label(newwin, text="Titel").grid(row=2, column=0)

        Label(newwin, text="Datum").grid(row=3, column=0)

        Label(newwin, text="PNr").grid(row=1, column=3)


        '''Strings Variables'''
        variable = StringVar(newwin)
        variable.set("Bitte auswählen") # default value

        prefill_prufungsnummer = StringVar(newwin, value='Prüfungsnummer')

        prefill_prufungtitel = StringVar(newwin, value='Titel')

        prefill_prufungsdatum = StringVar(newwin, value="DD-MM-YYYY")


        '''Buttons'''
        Button(newwin, text="Prüfung anlegen", width=BUTTONWIDTH_TOPLEVELS).grid(row=4, column=1)

        Button(newwin, text="Prüfung löschen", width=BUTTONWIDTH_TOPLEVELS).grid(row=2, column=4)

        OptionMenu(newwin, variable, 1, 2, 3, 4).grid(row=1, column=4)


        '''Entries'''
        entry_prufungsnummer = Entry(newwin, textvariable=prefill_prufungsnummer)
        entry_prufungstitel = Entry(newwin, textvariable=prefill_prufungtitel)
        entry_prufungsdatum = Entry(newwin, textvariable=prefill_prufungsdatum)

        entry_prufungsnummer.grid(row=1, column=1)
        entry_prufungstitel.grid(row=2, column=1)
        entry_prufungsdatum.grid(row=3, column=1)

        entry_prufungsnummer.config(fg="grey")
        entry_prufungstitel.config(fg="grey")
        entry_prufungsdatum.config(fg="grey")


        '''Clear Callbacks'''


        def delete_prufungsnummer_callback(event):

            if str(entry_prufungsnummer.get()) == "Prüfungsnummer":
                entry_prufungsnummer.delete(0, END)
                entry_prufungsnummer.config(fg="black")

            return None

        def delete_prufungstitel_callback(event):

            if str(entry_prufungstitel.get()) == "Titel":
                entry_prufungstitel.delete(0, END)
                entry_prufungstitel.config(fg="black")

            return None


        def delete_prufungsdatum_callback(event):

            if str(entry_prufungsdatum.get()) == "DD-MM-YYYY":
                entry_prufungsdatum.delete(0, END)
                entry_prufungsdatum.config(fg="black")

            return None


        entry_prufungsnummer.bind("<Button-1>", delete_prufungsnummer_callback)

        entry_prufungstitel.bind("<Button-1>", delete_prufungstitel_callback)

        entry_prufungsdatum.bind("<Button-1>", delete_prufungsdatum_callback)


    def StudierendenverwaltungFenster(self):

        svf = Toplevel(root)

        # Um zu verhindern, dass 1. mehrere Instanzen erstellt werden können und
        # während dieses Fenster existiert kann man nicht auf andere Fenster zugreifen,
        # bis dies geschlossen ist
        svf.grab_set()
        svf.focus_set()

        '''Labels'''

        Label(svf, text="Studierendenverwaltung").grid(row=0, column=2)

        Label(svf, text="Matrikelnummer").grid(row=1, column=0)

        Label(svf, text="Vorname").grid(row=2, column=0)

        Label(svf, text="Nachname").grid(row=3, column=0)

        Label(svf, text="Geburtsdatum").grid(row=4, column=0)

        Label(svf, text="Matrikelnummer").grid(row=1, column=3)

        entry_matrikelnummer = Entry(svf).grid(row=1, column=1)

        entry_vorname = Entry(svf).grid(row=2, column=1)

        entry_nachname = Entry(svf).grid(row=3, column=1)

        entry_geburtstag = Entry(svf).grid(row=4, column=1)

        variable = StringVar(svf)
        variable.set("Bitte auswählen") # default value

        OptionMenu(svf, variable, 1, 2, 3, 4).grid(row=1, column=4)

        Button(svf, text="Studierenden anlegen", width=BUTTONWIDTH_TOPLEVELS).grid(row=5, column=1)

        Button(svf, text="Studierenden löschen", width=BUTTONWIDTH_TOPLEVELS).grid(row=2, column=4)


    def NotenVerwaltungsFenster(self):


        nvf = Toplevel(root)
        nvf.grab_set()
        nvf.focus_set()

        #root.withdraw()
        # Um zu verhindern, dass 1. mehrere Instanzen erstellt werden können und
        # während dieses Fenster existiert kann man nicht auf andere Fenster zugreifen,
        # bis dies geschlossen ist

        '''Labels'''

        Label(nvf, text="Noteneingabe").grid(row=0, column=2)

        Label(nvf, text="Matrikelnummer").grid(row=1, column=0)

        Label(nvf, text="Note").grid(row=2, column=0)

        Label(nvf, text="Prüfung").grid(row=1, column=3)

        variable = StringVar(nvf)
        variable.set("Bitte auswählen") # default value

        OptionMenu(nvf, variable, 1, 2, 3, 4).grid(row=1, column=1)

        entry_note = Entry(nvf).grid(row=2, column=1)

        Label(nvf, text="Bitte die Note als ganzes Zahl eingeben. 2,3 als 23").grid(row=3, column=1)

        variable = StringVar(nvf)
        variable.set("Bitte auswählen") # default value

        prüfung_option = OptionMenu(nvf, variable, 1, 2, 3, 4).grid(row=1, column=4)

        Button(nvf, text="Note einspeichern", width=BUTTONWIDTH_TOPLEVELS).grid(row=2, column=4)

        Button(nvf, text="Note löschen", width=BUTTONWIDTH_TOPLEVELS).grid(row=3, column=4)

        Button(nvf, text="Hauptmenü", width=BUTTONWIDTH_TOPLEVELS).grid(row=4, column=4)

        #def closing():

#            root.deiconify()
 #           nvf.destroy()

#        nvf.protocol("WM_DELETE_WINDOW", closing)


    #def resizen(self, toplevel_window):
    #    #toplevel_window.geometry("850x200")
    #    #toplevel_window.resizable(0,0)

     #   return toplevel_window



if __name__ == '__main__':

    root = Tk()
    root.geometry("500x350")
    root.resizable(0,0)
    root.title("Verwaltungssystem")
    app = App(root)
    root.mainloop()
