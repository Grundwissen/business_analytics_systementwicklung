import datetime
import API

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


BUTTON_WIDHT_HEIGHT_MAIN_FRAME = (25, 2)
BUTTONWIDTH_TOPLEVELS = 18

NoneType = type(None)




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



    def update_dropdowns(self):

        conn = API.DatabaseConnection()

        matrikels = conn.get_matrikelnummer()

        return matrikels

    def student_anlegen(self, info):

        conn = API.DatabaseConnection()

        conn.create_student(info)

        return info


    def drop_student(self, info):

        conn = API.DatabaseConnection()

        conn.drop_student(info)

        return info




    def refresh_dropdown(self, optionmenu, auswahl):

        matrikellist = self.update_dropdowns()

        menu = optionmenu['menu']
        menu.delete(0, "end")

        for name in matrikellist:
            menu.add_command(label=name, command=lambda name=name: self.selection(name, auswahl))

    def selection(self, name, auswahl) :

        auswahl.set(name)



    def PrufungsverwaltungWindow(self):


        newwin = Toplevel(root)

        newwin.grab_set()
        newwin.focus_set()



        def prufung_anlegen_callback():
            prufung_anlegen = (entry_prufungsnummer.get(), entry_prufungstitel.get(), entry_prufungsdatum.get())

            prufungsnummer_evaluierung = False
            prufungstitel_evaluierung = False
            prufungsdatum_evaluierung = False


            # Überprüfung der Prüfungsnummer
            try:
                int(prufung_anlegen[0])
                prufungsnummer_evaluierung = True

            except (ValueError, TypeError):
                pass

            # Überprüfung Prüfungstitel
            if str(prufung_anlegen[1]).istitle():
                prufungstitel_evaluierung = True


            # Überprüfung der Prüfungsdatum
            prufungsdatum = prufung_anlegen[2]

            try:

                # Überprüfung des Datumformats
                parts = str(prufungsdatum).split("-")
                prufungsdatum_evaluiert = datetime.datetime(day=int(parts[0]), month=int(parts[1]), year=int(parts[2]))

                # Überprüfung ob der Datum in der Zukunft liegt
                heute = datetime.datetime.now()

                if (prufungsdatum_evaluiert < heute):
                    pass

                else:
                    prufungsdatum_evaluierung = True

            except (ValueError, IndexError):
                pass

            if prufungsnummer_evaluierung == False:
                messagebox.showwarning("Fehler", "Bitte geben Sie nur Zahlen ein.")

            if prufungstitel_evaluierung == False:
                messagebox.showwarning("Fehler", "Bitte achten Sie auf Groß- und Kleinschreibung.")

            if prufungsdatum_evaluierung == False:
                messagebox.showwarning("Fehler", "Bitte geben Sie ein gültiges Datum ein. Achten Sie darauf, dass der Datum in der Zukunft liegt.")

            # Wenn alle Überprüfungen True sind, wird der Eintrag in der Datenbank eingeschrieben
            if (prufungsnummer_evaluierung == True) and (prufungstitel_evaluierung == True) and (prufungsdatum_evaluierung == True):
                messagebox.showinfo("Erfolgreich", "Die Prüfung wurde erfolgreich angelegt.")
                #hier Datenbankeintrag...


        def prufung_loeschen_callback():
            prufung_zu_loeschen = prufung_zum_loeschen.get()

            if str(prufung_zu_loeschen) == "Bitte auswählen":
                messagebox.showwarning("Fehler", "Bitte wählen Sie eine Prüfung aus.")

            else:
                messagebox.showinfo("Erfolgreich", "Die Prüfung wurde erfolgreich gelöscht.")


        '''Labels'''
        Label(newwin, text="Prüfungsverwaltung").grid(row=0, column=2)

        Label(newwin, text="PNr").grid(row=1, column=0)

        Label(newwin, text="Titel").grid(row=2, column=0)

        Label(newwin, text="Datum").grid(row=3, column=0)

        Label(newwin, text="PNr").grid(row=1, column=3)


        '''Strings Variables'''
        prufung_zum_loeschen = StringVar(newwin)
        prufung_zum_loeschen.set("Bitte auswählen") # default value

        prefill_prufungsnummer = StringVar(newwin, value='Prüfungsnummer')

        prefill_prufungtitel = StringVar(newwin, value='Titel')

        prefill_prufungsdatum = StringVar(newwin, value="DD-MM-YYYY")


        '''Buttons'''
        Button(newwin, text="Prüfung anlegen", width=BUTTONWIDTH_TOPLEVELS, command=prufung_anlegen_callback).grid(row=4, column=1)

        Button(newwin, text="Prüfung löschen", width=BUTTONWIDTH_TOPLEVELS, command=prufung_loeschen_callback).grid(row=2, column=4)

        prufung_auswaehlen = OptionMenu(newwin, prufung_zum_loeschen, 1, 2, 3, 4)
        prufung_auswaehlen.grid(row=1, column=4)


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

        svf.grab_set()
        svf.focus_set()


        def studierenden_anlegen():


            student_informationen = (entry_matrikelnummer.get(), entry_vorname.get(), entry_nachname.get(),  entry_geburtstag.get())

            matrikelnummer_evaluierung = False
            vorname_evaluierung = False
            nachname_evaluierung = False
            geburtstag_evaluierung = False


            matrikelnummer_int = 0

            #Überprüfung Matrikelnummer
            try:
                matrikelnummer_int = int(student_informationen[0])
                matrikelnummer_evaluierung = True

            except ValueError:
                messagebox.showwarning("Fehler", "Bitte geben Sie nur ganze Zahlen ein.")


            #Überprüfung Vorname und Nachname
            if (str(student_informationen[1]).isalnum() == True) and (str(student_informationen[2]).isalnum() == True):
                vorname_evaluierung = True
                nachname_evaluierung = True

            else:
                messagebox.showwarning("Fehler", "Bitte geben richtige Vor- und Nachnamen ein.")


            date = 0

            #Überprüfung Geburtstagsdatum
            try:

                # Überprüfung des Datumformats
                parts = str(student_informationen[3]).split("-")
                geburtstag_evaluiert = datetime.datetime(day=int(parts[0]), month=int(parts[1]), year=int(parts[2]))
                date = str(geburtstag_evaluiert.date().strftime("%d-%m-%Y"))

                # Überprüfung ob der Datum in der Zukunft liegt
                heute = datetime.datetime.now()

                if (geburtstag_evaluiert > heute):
                    messagebox.showwarning("Fehler", "Geburtstag liegt in der Zukunft. Bitte geben Sie ein richtiges Datum ein.")

                else:
                    geburtstag_evaluierung = True

            except (ValueError, IndexError):
                pass


        # Wenn alle Überprüfungen True sind, wird der Eintrag in der Datenbank eingeschrieben
            if (matrikelnummer_evaluierung == True) and (vorname_evaluierung == True) and (nachname_evaluierung == True) and (geburtstag_evaluierung == True):

                try:
                    self.student_anlegen((matrikelnummer_int, student_informationen[1]+" "+student_informationen[2], date))
                    messagebox.showinfo("Erfolgreich", "Der Studierender wurde erfolgreich angelegt.")

                except Exception:
                    messagebox.showinfo("Failed", "Failed create Student.")

            else:

                 messagebox.showinfo("Fehler", "Bitte füllen Sie alle Felder aus.")


        def studierenden_loeschen():
            matrikelnummer_zu_loeschen = matrikelnummer_auswahl.get()
            print(matrikelnummer_zu_loeschen)

            if str(matrikelnummer_zu_loeschen) == "Bitte auswählen":
                messagebox.showwarning("Fehler", "Bitte wählen Sie eine Matrikelnummer zum Löschen aus.")

            else:
                try:
                    self.drop_student(matrikelnummer_zu_loeschen)
                    messagebox.showinfo("Erfolgreich", "Studierender wurde erfolgreich gelöscht.")

                    self.refresh_dropdown(option_matrikelnummer, matrikelnummer_auswahl)


                except Exception:
                    messagebox.showinfo("Failed", "Failed drop Student.")



        '''Labels'''

        Label(svf, text="Studierendenverwaltung").grid(row=0, column=2)

        Label(svf, text="Matrikelnummer").grid(row=1, column=0)

        Label(svf, text="Vorname").grid(row=2, column=0)

        Label(svf, text="Nachname").grid(row=3, column=0)

        Label(svf, text="Geburtsdatum").grid(row=4, column=0)

        Label(svf, text="Matrikelnummer").grid(row=1, column=3)


        '''Prefills'''
        prefill_matrikelnummer = StringVar(svf, value='12345')

        prefill_vorname = StringVar(svf, value='Max')

        prefill_nachname = StringVar(svf, value='Mustermann')

        prefill_geburtstag = StringVar(svf, value="DD-MM-YYYY")


        '''Entries'''
        entry_matrikelnummer = Entry(svf, textvariable=prefill_matrikelnummer)
        entry_matrikelnummer.grid(row=1, column=1)

        entry_vorname = Entry(svf, textvariable=prefill_vorname)
        entry_vorname.grid(row=2, column=1)

        entry_nachname = Entry(svf, textvariable=prefill_nachname)
        entry_nachname.grid(row=3, column=1)

        entry_geburtstag = Entry(svf, textvariable=prefill_geburtstag)
        entry_geburtstag.grid(row=4, column=1)

        entry_matrikelnummer.config(fg="grey")
        entry_vorname.config(fg="grey")
        entry_nachname.config(fg="grey")
        entry_geburtstag.config(fg="grey")


        def delete_matrikelnummer_callback(event):

            if str(entry_matrikelnummer.get()) == "12345":
                entry_matrikelnummer.delete(0, END)
                entry_matrikelnummer.config(fg="black")

            return None

        def delete_vorname_callback(event):

            if str(entry_vorname.get()) == "Max":
                entry_vorname.delete(0, END)
                entry_vorname.config(fg="black")

            return None

        def delete_nachname_callback(event):

            if str(entry_nachname.get()) == "Mustermann":
                entry_nachname.delete(0, END)
                entry_nachname.config(fg="black")

            return None


        def delete_geburtstag_callback(event):

            if str(entry_geburtstag.get()) == "DD-MM-YYYY":
                entry_geburtstag.delete(0, END)
                entry_geburtstag.config(fg="black")

            return None


        entry_matrikelnummer.bind("<Button-1>", delete_matrikelnummer_callback)
        entry_vorname.bind("<Button-1>", delete_vorname_callback)
        entry_nachname.bind("<Button-1>", delete_nachname_callback)
        entry_geburtstag.bind("<Button-1>", delete_geburtstag_callback)


        '''StringVar'''
        matrikelnummer_auswahl = StringVar(svf)
        matrikelnummer_auswahl.set("Bitte auswählen") # default value


        '''Options'''
        option_matrikelnummer = OptionMenu(svf, matrikelnummer_auswahl, ())
        option_matrikelnummer.grid(row=1, column=4)

        option_matrikelnummer.bind("<Button-1>", self.refresh_dropdown(option_matrikelnummer, matrikelnummer_auswahl))

        '''Buttons'''
        Button(svf, text="Studierenden anlegen", width=BUTTONWIDTH_TOPLEVELS, command=lambda: combine_update_and_write_commands(studierenden_anlegen(), self.refresh_dropdown(option_matrikelnummer, matrikelnummer_auswahl))).grid(row=5, column=1)
        Button(svf, text="Studierenden löschen", width=BUTTONWIDTH_TOPLEVELS, command=studierenden_loeschen).grid(row=2, column=4)


    def NotenVerwaltungsFenster(self):


        nvf = Toplevel(root)
        nvf.grab_set()
        nvf.focus_set()

        def note_einspeichern():
            zu_speichern_note = noten_auswahl.get()
            matrikelnummer_auswahl_speichern = matrikelnummer.get()

            if str(zu_speichern_note) == "Bitte auswählen" or str(matrikelnummer_auswahl_speichern) == "Bitte auswählen":
                messagebox.showwarning("Fehler", "Bitte wählen Sie eine Matrikellnummer und eine Prüfung aus.")

            else:

                note = noten_eingabe_uberprufen()

                if isinstance(note, NoneType) == True:
                    messagebox.showinfo("Fehler", "Bitte geben Sie eine richtige Note ein.")

                elif isinstance(note, float) == True:
                    messagebox.showinfo("Erfolgreich", "Die Note wurde erfolgreich gepspeichert.")
                    # hier note in die DB.....


        def note_loeschen():
            zu_loeschen_note = noten_auswahl.get()
            matrikelnummer_auswahl_speichern = matrikelnummer.get()

            if str(zu_loeschen_note) == "Bitte auswählen" or str(matrikelnummer_auswahl_speichern) == "Bitte auswählen":
                messagebox.showwarning("Fehler", "Bitte wählen Sie eine Matrikellnummer und eine Prüfung aus.")

            else:

                note = noten_eingabe_uberprufen()

                if isinstance(note, NoneType) == True:
                    messagebox.showinfo("Fehler", "Bitte geben Sie eine richtige Note ein.")

                elif isinstance(note, float) == True:
                    messagebox.showinfo("Erfolgreich", "Die Note wurde erfolgreich gelöscht.")
                    # hier von der DB löschen .....


        def noten_eingabe_uberprufen():
            zu_uberprufen = entry_note.get()

            if "," in zu_uberprufen:
                zu_uberprufen = str(zu_uberprufen).replace(",", ".")

            try:
                zu_uberprufen = float(zu_uberprufen)

                return zu_uberprufen

            except ValueError:

                return None


        '''Labels'''

        Label(nvf, text="Noteneingabe").grid(row=0, column=2)

        Label(nvf, text="Matrikelnummer").grid(row=1, column=0)

        Label(nvf, text="Note").grid(row=2, column=0)

        Label(nvf, text="Prüfung").grid(row=1, column=3)

        matrikelnummer = StringVar(nvf)
        matrikelnummer.set("Bitte auswählen") # default value

        matrikelnummer_auswahl = OptionMenu(nvf, matrikelnummer, 1, 2, 3, 4)
        matrikelnummer_auswahl.grid(row=1, column=1)

        entry_note = Entry(nvf)
        entry_note.grid(row=2, column=1)

        Label(nvf, text="Note als 2 , 2.0 oder als 2,0 eingeben.").grid(row=3, column=1)

        noten_auswahl = StringVar(nvf)
        noten_auswahl.set("Bitte auswählen") # default value

        note_zu_loeschen = OptionMenu(nvf, noten_auswahl, 1, 2, 3, 4)
        note_zu_loeschen.grid(row=1, column=4)

        Button(nvf, text="Note einspeichern", width=BUTTONWIDTH_TOPLEVELS, command=note_einspeichern).grid(row=2, column=4)

        Button(nvf, text="Note löschen", width=BUTTONWIDTH_TOPLEVELS, command=note_loeschen).grid(row=3, column=4)



def combine_update_and_write_commands(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func


if __name__ == '__main__':

    root = Tk()
    root.geometry("500x350")
    root.resizable(0,0)
    root.title("Verwaltungssystem")
    root.lift()

    app = App(root)
    root.mainloop()

