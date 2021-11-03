from tkinter import *
from tkinter import ttk
from functions import *
from tkinter import filedialog

categories = ["Allgemein", "Eltern", "Schüler", "Unterrichtsfrei"]

#-TKINTER EVENTS----------------------------------------


def event_listbox_select(event):
    a, b, c, d, e, f, g, h = (Update_Curr_Entry(lstbx_event_list.curselection(), liste))

    ent_event_name.delete(0, END)
    ent_event_name.insert(0, str(a))

    txtbx_event_description.delete(1.0, END)
    txtbx_event_description.insert(1.0, str(b))

    ent_start_date.delete(0, END)
    ent_start_date.insert(0, str(c))

    ent_start_time.delete(0, END)
    ent_start_time.insert(0, str(d))   

    ent_end_date.delete(0, END)
    ent_end_date.insert(0, str(e))

    ent_end_time.delete(0, END)
    ent_end_time.insert(0, str(f))

    if (g == 'true'):
        bool_alldayevent.set(1)
    else:
        bool_alldayevent.set(0)

def export_entries():
    exportCSVFile(filedialog.asksaveasfilename(title="Exportieren...", initialdir='~/Documents', defaultextension=".csv", filetype=(("Comma Separated Value", "*.csv"),("All Files", "*.*"))), len(liste), liste)

def new_event(): #clear all input fields
    ent_event_name.delete(0, END)
    txtbx_event_description.delete(1.0, END)
    ent_start_date.delete(0, END)
    ent_start_time.delete(0, END)  
    ent_end_date.delete(0, END)
    ent_end_time.delete(0, END)
    bool_alldayevent.set(0)

def save_event():
    save_new_event(ent_event_name.get(), txtbx_event_description.get("1.0",END), ent_start_date.get(), ent_start_time.get(),ent_end_date.get(), ent_end_time.get(), bool_alldayevent.get(), lstbx_categories.get(ANCHOR))

   

def delete_event():
    print()

liste = [["Test0","Das ist ein Text <br>BLABLABLA</br>", "10-02-2021", "10:12:00", "10-02-2021", "10:15:00", "false", "Chinatown, Döner"], ["Test1","Das ist ein Text <br>BLABwadwLABLA</br>", "10-04-2021", "12:15:00", "10-06-2021", "10:30:00", "true", "Bratwurst, Oxford"]]
#for i in range(2,25):
#    liste.append(["Test" + str(i)])


#-MAIN PROGRAM------------------------------------------

bool_new_event='False' #if true, current event is new and hasn't been saved yet

root = Tk()
root.title("Kalender Tool")
root.resizable(False, False)

frm_curr_event = ttk.Frame(root, relief="groove", borderwidth=5, width=600, height=100)
frm_curr_event.grid(column=1, row=1, sticky="N")

lbl_event_name = ttk.Label(frm_curr_event, text="Name")
lbl_event_name.grid(column=1, row=1, sticky="W")

ent_event_name = ttk.Entry(frm_curr_event, width=50)
ent_event_name.grid(column=1, columnspan=2, row=2, sticky="W")


lbl_event_description = ttk.Label(frm_curr_event, text="Beschreibung")
lbl_event_description.grid(column=1, row=3, sticky="W")

txtbx_event_description = Text(frm_curr_event, height=10, width=38, relief="raised")
txtbx_event_description.grid(column=1, columnspan=2, row=4, sticky="W")


lbl_start_date = ttk.Label(frm_curr_event, text="Start Datum (DD-MM-YYYY)")
lbl_start_date.grid(column=1, row=5, sticky="W")

ent_start_date = ttk.Entry(frm_curr_event)
ent_start_date.grid(column=1, row=6, sticky="W")


lbl_start_time = ttk.Label(frm_curr_event, text="Startzeit (HH:MM)")
lbl_start_time.grid(column=1, row=7, sticky="W")

ent_start_time = ttk.Entry(frm_curr_event)
ent_start_time.grid(column=1, row=8, sticky="W")


lbl_end_date = ttk.Label(frm_curr_event, text="End Datum (DD-MM-YYYY)")
lbl_end_date.grid(column=2, row=5, sticky="W")

ent_end_date = ttk.Entry(frm_curr_event)
ent_end_date.grid(column=2, row=6, sticky="W")


lbl_end_time = ttk.Label(frm_curr_event, text="Endzeit (HH:MM)")
lbl_end_time.grid(column=2, row=7, sticky="W")

ent_end_time = ttk.Entry(frm_curr_event)
ent_end_time.grid(column=2, row=8, sticky="W")

bool_alldayevent=BooleanVar()
chk_all_Day_event = ttk.Checkbutton(frm_curr_event, text="Ganztägiges Event?", variable=bool_alldayevent)
chk_all_Day_event.grid(column=1, row=9, sticky="W")

lbl_categories = ttk.Label(frm_curr_event, text="Kategorien")
lbl_categories.grid(column=1, row=10, sticky="W")

categories_var=StringVar(value=[item for item in categories])
lstbx_categories=Listbox(frm_curr_event, height=4, width=50, listvariable=categories_var, relief="raised", selectmode='multiple')
lstbx_categories.grid(column=1, columnspan=2, row=11, sticky="W")




frm_treelist = ttk.Frame(root, relief="groove", borderwidth=5, width=200, height=100)
frm_treelist.grid(column=2, row=1, sticky="N") 



entries_var=StringVar(value=[item[0] for item in liste])

lstbx_event_list=Listbox(frm_treelist, height=25, width=31, listvariable=entries_var, relief="raised")
lstbx_event_list.pack()
lstbx_event_list.bind('<<ListboxSelect>>', event_listbox_select)




frm_entry_controls = ttk.Frame(relief="groove", borderwidth=5, width=200)
frm_entry_controls.grid(column=3, row=1, sticky="N")

btn_create_entry = ttk.Button(frm_entry_controls, text="Neues Event", width=20, command=new_event)
btn_create_entry.pack()
#btn_create_entry.state(['disabled']) 

btn_delete_entry = ttk.Button(frm_entry_controls, text="Event löschen", width=20, command=delete_event)
btn_delete_entry.pack()
#btn_delete_entry.state(['disabled']) 

btn_save_entry = ttk.Button(frm_entry_controls, text="Event speichern", width=20, command=save_event)
btn_save_entry.pack()
#btn_save_entry.state(['disabled']) 



frm_controls = ttk.Frame(relief="groove", borderwidth=5, width=200)
frm_controls.grid(column=3, row=1, sticky="S") 

btn_create_new_db = ttk.Button(frm_controls, text="Datenbank erstellen", width=20)
btn_create_new_db.pack()

btn_load_from_db = ttk.Button(frm_controls, text="Datenbank laden", width=20)
btn_load_from_db.pack()

btn_save_to_db = ttk.Button(frm_controls, text="Datenbank speichern", width=20)
btn_save_to_db.pack()
btn_save_to_db.state(['disabled']) 

btn_import = ttk.Button(frm_controls, text="Importieren", width=20)
btn_import.pack()

btn_export = ttk.Button(frm_controls, text="Exportieren", width=20, command=export_entries)
btn_export.pack()
#btn_export.state(['disabled']) 



root.mainloop()



#exportCSVFile("C:/Users/alexs/Desktop/test.csv", 2, liste)
