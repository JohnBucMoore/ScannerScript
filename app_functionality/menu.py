import subprocess
from app_functionality import vulScan, ufwSetup, networkCapture

def show_homepage():
    print("")
    print("          === Network Defender ===          ")
    print("------------------------------------------- ")
    print("| 1.    Network Scans     | 2.    Firewall Setup  |")
    print("-------------------------------------------  ")
    print("-------------------------------------------  ")
    print("| 3.  Packet Capture     | 4.        Exit         |")



def menu_options():

    # uc stands for User Choice
    uc = int(input("Please choose a menu option: "))

    if uc == 1:
        vulScan.v_scans()
    elif uc == 2:
        ufwSetup.firewall_setup()
    elif uc == 3:
        networkCapture.start_capture()
#    elif uc == 4:
#        snortSetup.configure_snort_rules()
    elif uc == 4:
        exit()
    else:
        print('Invalid Input')
