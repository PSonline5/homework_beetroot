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
        self.applications = set(applications)
        self.contacts = contacts
        self.settings = settings

    def add_app(self, app):
        self.applications.add(app)

    def del_app(self, app):
        self.applications.remove(app)

    def add_contact(self, contact: tuple):
        self.contacts.append(contact)

    def del_contact(self, contact):
        self.contacts.remove(contact)

    def edit_settings(self, **settings):
        self.settings = settings.update()


class Computer(Gadget):  # OS, applications, trash == list
    def __init__(self, brand, model, year, os, applications):
        super().__init__(brand, model, year,)
        self.os = os
        self.applications = set(applications)
        self.trash_ = []

    def add_app(self, app):
        self.applications.add(app)

    def del_app(self, app):
        self.trash_.append(app)
        self.applications.remove(app)

    def remove_trash(self, trash_):
        self.trash_ = trash_
        self.trash_.clear()
        return self.trash_

    def explore_trash(self):
        return "".join(self.trash_)


class TV(Gadget):
    def __init__(self, brand, model, year, settings, channels_list):
        super().__init__(brand, model, year)
        self.settings = settings
        self.channels_list = channels_list

    def add_channel(self, channel):
        self.channels_list.append(channel)

    def del_channel(self, channel):
        self.channels_list.remove(channel)

    def edit_settings(self, **settings):
        self.settings = settings.update()
