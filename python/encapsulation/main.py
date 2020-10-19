from datetime import datetime

from models.person import Person

if __name__ == '__main__':
    p1 = Person("zaza", "vanderquack", datetime(2012, 2, 13))
    # p1.set_birthdate(datetime(2012,12,13)) sans property
    # sans property
    p1.birthdate(datetime(2012, 12, 13))
    desc = p1.se_decrire()
    print(desc)
    print(p1.get_birthdate_month())

    # p1.set_lastname(p1.get_lastname().upper()) sans property
    # avec property
    p1.lastname = p1.lastname.upper()
    print(p1.se_decrire())