import version_number
import wifi_manager
print("HELLO!-----------------")
print("Pager version: ", version_number.version)
print("enter 'sh wifi' to set up wifi")
print("enter 'sh init' to set up UID. << You need to set up UID of your account "
      "for the device to work. You'll get more instructions after entering 'sh init'")
print("enter 'sh update' to update pager software. It should only take about 10 seconds. ")
print("enter 'sh reboot' to restart device")


def check_connection():
    print('checking connection')
    hostname = wifi_manager.get_hostname()
    ip = wifi_manager.get_ip()
    print("hostname: ", hostname)
    is_connected = wifi_manager.is_connected()
    connection_name = wifi_manager.get_connection_name()
    print("connection_name: ", connection_name)
    connected_to_default = False
    global default_connection
    if connection_name.lower() == default_connection.lower():
        print("Connected to default: ", default_connection)
        connected_to_default = True
    else:
        connected_to_default = False
        print("Connected to: ", connection_name)

    print("Connected to internet: ", is_connected)
    print("ip: ", ip)

    if connected_to_default:
        return "DEFAULT"
    # if not is_connected:
        # return "NULL"
    return "CONNECTED"


check_connection()