import pywhatkit as whatsapp

whatsapp.start_server()
contacts = {"Anirud": "+919538452313"
            }

contact = input("Enter the name/contact number of the person to message: ")

if contact in contacts.keys() or contact == contacts.get(contact):
    whatsapp.sendwhatmsg_instantly(contact, "hello", 1, True, 1)
else:
    contact_as_list = [_ for _ in contact]
    for person in contacts.keys():

