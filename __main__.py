import CSVManagment
import os

#runs and loops to see if user would like to add additional devices
def main():

    os.system('cls')
    devz = input("How many devices do you want to add? (Enter for 1)")

    if devz is None:
        int(devz) == 1
        CSVManagment.new_csv_entry()
        exit()
    else:
        devz == int(devz)
        while devz != 0:
            CSVManagment.new_csv_entry()
            devz -= 1

if __name__ == "__main__":
    main()
