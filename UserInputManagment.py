from datetime import datetime

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'


def get_submitted_by():
    sto = input(BOLD + "Person that SUBMITTED device. ")
    return sto


def get_date_submitted():
    while True:
        try:
            dsub = input(BOLD + "Date device was received in MM/DD/YYYY format, or leave blank for today's "
                                       "date. ")
            if dsub == '':
                i = datetime.now()
                dsub = i.strftime('%m/%d/%Y')
                break
            else:
                dsub = datetime.strptime(dsub, '%m/%d/%Y')
                break
        except ValueError:
            print(RED + "Incorrect Format")
            continue
    return str(dsub)


def get_accepted_by():
    aby = input(BOLD + "Person that ACCEPTED device. ")


def get_agency():
    agen = input(BOLD + "Agency of person that SUBMITTED device (press enter for SPD) ")
    if agen == "":
        agen = "SPD"
    return agen


def get_intaker_name():
    exrec = str(input(BOLD + "Intake persons name "))
    return exrec


def get_detectives_name():
    detec = str(input(BOLD + "Case investigator's name "))
    return detec


def get_device_make():
    make = str(input(BOLD + "Devices make (Ex: Samsung, Apple) "))
    return make


def get_device_model():
    model = str(input(BOLD + "Devices model (EX: Galaxy A10, iPhone A2111) "))
    return model


def get_device_imei():
    imei = input(BOLD + "Devices serial number or IMEI (IMEI preferred) ")
    if len(imei) < 15 or len(imei) > 15:
        resp = input(YELLOW + "WARNING: INPUT LESS THAN STANDARD LENGTH OF IMEI, "
                     "TRY AGAIN (Y) OR CONTINUE ANYWAY (N)"+ END).lower()
        if resp == 'y':
            imei = input(BOLD + "Devices serial number or IMEI (IMEI preferred) ")
    return imei


def get_case_num():
    cnum = input(BOLD + "SUBMITTING agency's case number ")
    return cnum
