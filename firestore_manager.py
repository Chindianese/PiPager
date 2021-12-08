print('start importing firestore manager')
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from firebase_admin import firestore
import threading

import os
from time import sleep

import uid_manager

global currentUser
global callback_done
global lcd_enabled

global lcd_display
global db
print('done importing firestore manager')


def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(f'Received document snapshot: {doc.id}')
        current_message = doc.to_dict()["currentMessage"]
        print(f'current message: {current_message}')
        if lcd_enabled:
            lcd_display.show_on_lcd(current_message)
            import screen_effects
            screen_effects.blink_led(0.2, 2)
    callback_done.set()


# idk why tf i wrote this
def get_target_uid(uid):
    doc_ref = db.collection('Development').document('UserData').collection('Users').document(uid)
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        print(f'Document data: {data}')
        return data['targetUID']
    else:
        print(u'No such document!')


def get_username(uid):
    doc_ref = db.collection('Development').document('UserData').collection('Users').document(uid)
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        # print(f'Document data: {data}')
        return data['displayName']
    else:
        print(u'No such document!')


def init_firestore_listener(lcd_enabled_pri):
    global lcd_enabled
    lcd_enabled = lcd_enabled_pri
    if lcd_enabled:
        global lcd_display
        print("begin import lcd")
        import lcd_display
        print('lcd display imported')
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    path = os.path.join(__location__, 'LDMessageServiceAccountKey.json')
    cred = credentials.Certificate(path)
    firebase_admin.initialize_app(cred)
    global db
    db = firestore.client()

    # Create an Event for notifying main thread.
    global callback_done
    callback_done = threading.Event()

    uid = uid_manager.get_uid()
    display_name = get_username(uid)
    print("logged in as: ", display_name)
    # Create a callback on_snapshot function to capture changes
    doc_ref = db.collection('Development').document('UserContent').collection('Users').document(uid)

    # Watch the document
    doc_watch = doc_ref.on_snapshot(on_snapshot)

    while True:
        sleep(60.0)
