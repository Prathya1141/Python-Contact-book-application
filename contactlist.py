from tkinter import *
import contactlist_gui
import contactlist_func


class AppWindow(Frame):
    def __init__(self, app):
        Frame.__init__(self)

        app.option_add("*font", "Helvetica 10")
        app.resizable(width=False, height=False)
        # TODO: add center_window function
        # contactlist_func.center_window(app, 500, 300)
        app.geometry('{}x{}'.format(500, 300))

        app.title('Python Contact Book')
        app.iconbitmap(self, default="assets/contactlist.ico")

        # create an outer frame with padding around window to put all other content
        container = Frame(app)
        container.grid(row=0, column=0, padx=25, pady=10)

        # define tkinter string vars for form fields
        self.text_id = StringVar()
        self.text_first_name = StringVar()
        self.text_last_name = StringVar()
        self.text_email = StringVar()
        self.text_phone_number = StringVar()
        self.text_address = StringVar()

        # create list for form fields and put variables in list
        self.contactlist_fields = []
        self.contactlist_fields.append(self.text_id)
        self.contactlist_fields.append(self.text_first_name)
        self.contactlist_fields.append(self.text_last_name)
        self.contactlist_fields.append(self.text_email)
        self.contactlist_fields.append(self.text_phone_number)
        self.contactlist_fields.append(self.text_address)

        # set contactlist lists for displaying contacts
        self.contactlist_entry_names = []
        self.contactlist_entry_ids = []

        # load GUI into container Frame
        contactlist_gui.load_gui(self, container)

        # load database and populate contact list
        contactlist_func.create_db()
        contactlist_func.load_contactlist(self)


if __name__ == "__main__":
    root = Tk()
    App = AppWindow(root)
    root.mainloop()
