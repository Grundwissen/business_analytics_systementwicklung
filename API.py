import DB

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
