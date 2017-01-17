from ciscoconfparse import CiscoConfParse

config_file = 'cisco_ipsec.txt'

config_parsed = CiscoConfParse(config_file)
crypto = config_parsed.find_objects(r"^crypto map CRYPTO")

for x in crypto:
    print x.text
    for child in x.children:
        print child.text

 
