import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def update(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                phone = str(input('Escribe el nuevo número de teléfono del contacto: '))
                if not phone:
                    contact.phone = contact.phone
                else:
                    contact.phone = phone
                email = str(input('Escribe el nuevo email del contacto: '))
                if not email:
                    contact.email = contact.email
                else:
                    contact.email = email
                response = str(input('Quiere actualizar el nombre del contacto?: (y|N)'))
                if response == 'y':
                    name = str(input('Ingresa el nuevo nombre del contacto: '))
                    contact.name = name
                self._save()
                break
        else:
            self._not_found()

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()
    
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                print('**********')
                print('Contacto {} eliminado correctamente'.format(contact.name))
                print('**********')
                self._save()
                break
        else:
            self._not_found()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)


    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nómbre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('**********')
        print('¡No Encontrado!')
        print('**********')

    def _save(self):
        with open('contacts.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                write.writerow((contact.name, contact.phone, contact.email))


def run():
    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
			¿Qué deseas hacer?

			[a]ñadir contacto
			[ac]tualizar contacto
			[b]uscar contacto
			[e]liminar contacto
			[l]istar contacto
			[s]alir
		'''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el número de teléfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.add(name, phone, email)
        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.update(name)
        elif command == 'b':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.search(name)
        elif command == 'e':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.delete(name)
        elif command == 'l':
            contact_book.show_all()
        elif command == 's':
            break
        else:
            print('Comando no encontrado')


if __name__ == "__main__":
    print('		B I E N V E N I D O  A  L A  A G E N D A  ')
    run()
