import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
from firebase_admin import firestore
import threading
from time import sleep


global currentUser
currentUser = "Melvan"
global callback_done
global lcd_enabled

global lcd_display

import os
def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        print(f'Received document snapshot: {doc.id}')
        current_message = doc.to_dict()["currentMessage"]
        print(f'current message: {current_message}')
        if lcd_enabled:
            lcd_display.show_on_lcd(current_message)
    callback_done.set()


def init_firestore_listener(lcd_enabled_pri):
    import firebase_admin
    from firebase_admin import credentials
    global lcd_enabled
    lcd_enabled = lcd_enabled_pri
    if lcd_enabled:
        global lcd_display
        import lcd_display
        print('lcd display imported')
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    path = os.path.join(__location__, 'LDMessageServiceAccountKey.json')
    cred = credentials.Certificate(path)
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    # Create an Event for notifying main thread.
    global callback_done
    callback_done = threading.Event()

    # Create a callback on_snapshot function to capture changes
    doc_ref = db.collection('Development').document('UserContent').collection('Users').document('Debug')

    # Watch the document
    doc_watch = doc_ref.on_snapshot(on_snapshot)

    while True:
        sleep(60.0)