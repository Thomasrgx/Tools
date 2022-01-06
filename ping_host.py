import os

def ping(host):
    """
    Returns response value to determine whether a host responds to a ping request or not.
    """
    response = os.system("ping -c 1 -w2 " + host + " > /dev/null 2>&1")
    if response == 0:
        print (host, 'is up!')
    else:
        print (host, 'is down!')
        response = 1
    return response

ping('8.8.8.8')