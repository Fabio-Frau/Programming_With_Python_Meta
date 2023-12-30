def ispresent(person):
    names = ["Al", "Bo", "Chi", "Ma"]
    if person in names:
        return True
    else:
        False


def nodigit(person):
    if person.isalpha():
        return True
    else:
        return False