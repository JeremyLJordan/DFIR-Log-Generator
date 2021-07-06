import UserInputManagment
import csv
import os.path
import DOCXManagment


def new_csv_entry():
    newdev = UserInputManagment
    headers = ["DATE SUBMITTED", "SUBMITTED BY", "SUBMITTED TO", "DATE RELEASED", "RELEASED TO",
               "RELEASED BY", "AGENCY", "DEVICE MAKE/MODEL", "SERIAL NUMBER", "CASE NUMBER"]
    newdata = [newdev.get_date_submitted(),
               newdev.get_detectives_name(),
               newdev.get_intaker_name(),
               "",
               "",
               "",
               newdev.get_agency(),
               newdev.get_device_make() + " " +
               newdev.get_device_model(),
               newdev.get_device_imei(),
               newdev.get_case_num()]


    #checks for existence of intake log. If one doesnt exist it makes one. Then writes list to line in csv file
    #finally, checks if user wants to generate report with device info, if so
    if not os.path.exists('device_intake_log.xlsx'):
        with open('device_intake_log.xlsx', "a", newline='') as f:
            i = csv.writer(f)
            i.writerow(headers)
            i.writerow(newdata)
            f.close()
            check_for_report(newdata)
    else:
        with open('device_intake_log.xlsx', "a", newline='') as f:
            i = csv.writer(f)
            i.writerow(newdata)
            f.close()
            check_for_report(newdata)

#checks if user wants to generate a report, if so sends to DOCXManagment
def check_for_report(device):
    i = input("Would you like to generate a report with this device information? (Y)es or (N)o?").lower()
    if i == "y":
        DOCXManagment.create_report(device)
    else:
        pass
