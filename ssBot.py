from imapclient import IMAPClient
import random, email, getpass, os, re, yagmail, loginInfo



def FamilySetUp():
    last_name_list = []
    family_dict = {}
    sm_family_names_list = []
    family_individual = {}


    # Gets Last names and appends to list DONE
    total = int(input("How many families are there? "))
    for x in range(1, total + 1):
        last_name = input("Last name of family %i? " % (x))
        last_name_list.append(last_name)
        print(last_name_list)

    # TEST!!!! last_name_list = ['Hanek', 'Malone']

    # Makes a dictionary with keys as last name and values of each family individual DONE
    for x in last_name_list:
        familty_total = int(input("Total number in the %s family? " % (x))) #make this unique?
        last_name = x
        for y in range(1, familty_total + 1):
            family_names = input("Enter name of a family member until complete. ")
            sm_family_names_list.append(family_names)
        family_dict[last_name] = sm_family_names_list
        sm_family_names_list = []
        print(family_dict)

    # !!!We changed the order of the dictionary lets see if this helps, it worked need to edit above to make bottom
    # family_dict = {'Jon': 'Johnson', 'jacob': 'Johnson', 'mom': 'Johnson', 'dad': 'Johnson', 'danny': 'Smith', 'dan': 'Smith', 'morgan': 'Smith', 'lizzy': 'Smith'}

    present_dict = {}
    # Each family member now has their individual christmas list
    for key, values in family_dict.items():
      for value in values:
            present_dict[value] = input("What does %s want for Xmas? " % (value))
    print(present_dict)

    # Now to assign secret santa, restriction put on family (no family member will be SS to someone within their family
    # present_dict = {'Jon': 'Hockey', 'jacob': 'MtG', 'mom': 'Paint', 'dad': 'Fish', 'danny': 'MtG', 'dan': 'Cook',
    # 'morgan': 'Clothes', 'lizzy': 'Clothes'}

    pairing_dict = {}
    all_list = []
    for key in family_dict.keys():
        all_list.append(key)
    print(all_list)

    while len(pairing_dict) != len(all_list):
        gift_list = all_list
        rec_list = all_list
        gift = random.choice(gift_list)
        rec = random.choice(rec_list)
        # print(gift)
        # print(rec)
        if family_dict[gift] != family_dict[rec] and rec not in pairing_dict.values():
            pairing_dict[gift] = rec
        else:
            continue
    print(pairing_dict)

    # pairing_dict = {'Jon': 'danny', 'jacob': 'lizzy', 'lizzy': 'dad', 'danny': 'Jon', 'dan': 'mom', 'dad': 'morgan', 'mom': 'dan', 'morgan': 'jacob'}
    pairing_present_dict = {}

    for gift, rec in pairing_dict.items():
        pairing_present_dict[gift] = (rec, present_dict[rec])
    print(pairing_present_dict)

#FamilySetUp()

#You need to scrap emails for incoming and send out outgoing and then we are pretty much done.
# Too much effort to understand how to get the body out of a scrape. It would be easier just to copy and paste

def EmailInnkeeper():
    server = IMAPClient('imap.gmail.com', use_uid=True)
    server.login(loginInfo.email, loginInfo.pwd)
    reciever = "email of reciever"
    body = "Put the present suggestions here"
    yag.send(reciever, 'Friendly Secret Santa 2019', body)
    print("Sent to %s" % (reciever))
    print('Done. Merry Christmas!')








def EmailSender():
    yag = yagmail.SMTP(loginInfo.email, loginInfo.pwd)
    receiver = "Hanekj25@gmail.com"
    # Make this cycle through email list
    body = "Hello there from Yagmail"
    # This will hold person and descrption
    yag.send(receiver, 'Friendly Secret Santa 2019', body)
    print("Sent to %s" % (receiver))

# EmailSender()
# EmailInnkeeper()
