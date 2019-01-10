import DB
from fpdf import FPDF

conn = DB.DatabaseConnection()


def update_matrikel_dropdowns():

    matrikels = conn.get_matrikelnummer()

    return matrikels


def refresh_matrikel_dropdown(optionmenu, auswahl):

    matrikellist = update_matrikel_dropdowns()

    menu = optionmenu['menu']
    menu.delete(0, "end")

    for name in matrikellist:
        menu.add_command(label=name, command=lambda name=name: selection(name, auswahl))


def selection(name, auswahl) :

    auswahl.set(name)


def student_anlegen(info):

    conn.create_student(info)

    return info


def drop_student(info):


    conn.drop_student(info)

    return info


def update_klausur_dropdowns():


    klausuren = conn.get_klausurnummer()

    return klausuren


def refresh_klausur_dropdown(optionmenu, auswahl):

    klausurlist = update_klausur_dropdowns()

    menu = optionmenu['menu']
    menu.delete(0, "end")

    for name in klausurlist:
        menu.add_command(label=name, command=lambda name=name: kl_selection(name, auswahl))


def kl_selection(name, auswahl) :

    auswahl.set(name)


def klausur_anlegen(info):

    conn.create_klausur(info)

    return info


def drop_klausur(info):

    conn.drop_klausur(info)

    return info


def insert_note(info):

    conn.insert_note(info)

    return info


def delete_note(info):

    cursor_status = conn.delete_note(info)

    return cursor_status


def combine_update_and_write_commands(*funcs):

    def combined_func(*args, **kwargs):

        for f in funcs:
            f(*args, **kwargs)

    return combined_func


def generate_pdf(info):

    noten = conn.get_all_noten_by_student(info)

    try:

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        # Eine Seite hinzufügen:
        pdf.add_page()
        # Schriftart festlegen:
        pdf.set_font("Arial", size=18)
        #Logo
        pdf.image("Ressources/images-12.jpeg")
        # Überschrift
        pdf.cell(30, 10, 'Notenliste')
        pdf.ln(10)
        #Name
        pdf.set_font("Arial", size=12)
        pdf.cell(30, 10, 'Name', 1, 0, 'C')
        pdf.ln(15)
        #Noten
        pdf.cell(30, 10, 'Auflistung der Noten: ')
        pdf.ln(10)

        for i in noten:
            pdf.write(5, str(i))
            pdf.ln(10)

        pdf.output("Notenspiegel-{}.pdf".format(info))

        return True

    except Exception:

        return False





