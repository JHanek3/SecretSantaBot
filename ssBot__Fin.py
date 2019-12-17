import random, email, getpass, os, re, yagmail, loginInfo

"""
in another file called loginInfo we have the email and pwd
There is also a dictionary with Keys of first name partcipants then a list with their email and present selection
Example: 
info = {'Jon': ['myEmail', 'My Present Suggestions'
        'Jonathon': ['hisEmail', 'His Present Suggestions'}
"""

def SetUp():
    # Create a dictionary Any restrictions?, group them together under the same value name
    # Make sure they match your loginInfo info dictionary

    name_dict = {'Jon': 'Jaroline', 'Caroline': 'Jaroline', 'Liam': 'Miam', 'Maria': 'Miam',
                      'Parthiv': 'NotClose', 'Austin': 'NotClose', 'Andrew': 'NotClose',
                      'David': 'NotClose', 'Kelly': 'LastNameA', 'Sadie': 'LastNameB', 'Maddie': 'LastNameC'}


    # Appends every name to a list for pairing off
    pairing_dict = {}
    all_list = []
    for key in name_dict.keys():
        all_list.append(key)
    # print(all_list)

    # Here we pair off everyone
    while len(pairing_dict) != len(all_list):
        gift_list = all_list
        rec_list = all_list
        gift = random.choice(gift_list)
        rec = random.choice(rec_list)

        if name_dict[gift] != name_dict[rec] and rec not in pairing_dict.values():
            pairing_dict[gift] = rec
        else:
            continue

    print(pairing_dict)
    return pairing_dict

def run(dic):
    # Here we make the person a key with values of who they have and what they said they wanted
    pairing_present_dict = {}
    for giftR, recR in dic.items():
        pairing_present_dict[giftR] = (recR, loginInfo.info[recR][1])
    # print(pairing_present_dict)

    yag = yagmail.SMTP(loginInfo.email, loginInfo.pwd)

    for name, values in pairing_present_dict.items():
        reciever = loginInfo.info[name][0]
        body = ("Hello %s!\n This is the Secret Santa Bot, for this year you have %s.\n They told me: %s" % (name, values[0], values[1]))
        # print(body)
        yag.send(reciever, 'Friendly Secret Santa 2019', body)
        print("Sent to %s" % (reciever))
    print('Done. Merry Christmas!')


def main():
    pairings = SetUp()
    # Let's check here if we are happy with the pairings
    while True:
        go = input("Are we happy with these pairings(y/n)?")
        if go == "y":
            break
        else:
            pairings= SetUp()
    run(pairings)


main()