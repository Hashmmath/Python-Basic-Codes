'''This code generates a random MAC address that starts with 
the OUI (Organizationally Unique Identifier) 00:16:3e. The 
remaining three bytes are randomly generated. You can call 
this function multiple times to generate different MAC 
addresses.'''


import random

def generate_mac_address():
    # Generate a random MAC address
    mac_address = [ 0x00, 0x16, 0x3e,
                    random.randint(0x00, 0x7f),
                    random.randint(0x00, 0xff),
                    random.randint(0x00, 0xff)]
    # Format the MAC address
    mac_address_str = ':'.join(map(lambda x: "%02x" % x, mac_address))
    return mac_address_str
