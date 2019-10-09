class Gadget:  # brand, model, year
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def gadget_info(self):
        return f"{self.brand} {self.model} {self.year}"


class Phone(Gadget):   # applications(list), contacts(list[tuple]), settings
    def __init__(self, brand, model, year, applications, contacts, settings):
        super().__init__(brand, model, year)
        self.applications = applications
        self.contacts = contacts
        self.settings = settings

    def add_app(self, app):
        self.app = app
        if self.app not in self.applications:
            self.applications.append(self.app)
        else:
            print("This app already exist")
        return self.applications

    def del_app(self, app):
        self.app = app
        self.applications.remove(self.app)
        return self.applications

    def add_contact(self, contact):
        self.contact = contact
        self.contacts.append(self.contact)
        return self.contacts

    def del_contact(self, contact):
        self.contact = contact
        self.contacts.remove(self.contact)
        return self.contacts

    def edit_settings(self, **settings):
        self.settings = settings.update()


class Computer(Gadget):  # OS, applications, trash == list
    def __init__(self, brand, model, year, OS, applications):
        super().__init__(brand, model, year,)
        self.OS = OS
        self.applications = applications
        self.trash_ = []

    def add_app(self, app):
        self.app = app
        if self.app not in self.applications:
            self.applications.append(self.app)
        else:
            print("This app already exist")
        return self.applications

    def del_app(self, app):
        self.app = app
        self.applications.remove(self.app)
        return self.applications

    def remove_trash(self, trash_):
        self.trash_ = trash_
        self.trash_.clear()
        return self.trash_

    def explore_trash(self, trash_):
        self.trash_ = trash_
        self.trash_ = "".join(self.trash_)
        return self.trash_


class TV(Gadget):   # chanels_list settings
    def __init__(self, brand, model, year, settings, channels_list):
        super().__init__(brand, model, year)
        self.settings = settings
        self.channels_list = channels_list

    def add_channel(self, channel):
        self.channel = channel
        self.channels_list.append(self.channel)

    def del_channel(self, channel):
        self.channel = channel
        self.channels_list.remove(self.channel)

    def edit_settings(self, **settings):
        self.settings = settings.update()



