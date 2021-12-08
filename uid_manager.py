import os


def request_uid():
    print("Log in to Pager mobile to retrieve UID")
    print("https://ldmessage.web.app/")
    uid = input("Enter your UID:")
    set_uid(uid)


def set_uid(uid):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    path = os.path.join(__location__, 'uid.dat')

    f = open(path, "w")
    f.write(uid)
    f.close()
    print("Successfully set uid to: ", f'\033[1;34;40m {uid}  \n')


def get_uid():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    path = os.path.join(__location__, 'uid.dat')
    try:
        f = open(path, "r")
        uid = f.read()
    except IOError:
        print('no UID set. set uid through Pager/init.py')
        return ""
    return uid
