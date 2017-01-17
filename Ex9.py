from ciscoconfparse import CiscoConfParse

config_file = 'cisco_ipsec.txt'
config_parsed = CiscoConfParse(config_file)

pfs2 = config_parsed.find_objects_w_child (parentspec=r"^crypto map CRYP", childspec=r'pfs group2')

for x in pfs2:
    print x.text

