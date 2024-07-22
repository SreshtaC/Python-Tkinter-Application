import dbm
db = dbm.open('/Users/sreshtacheekatla/Desktop/Python/project/pdb','c')
db['Nuwakot'] = 'PLUM often goes to a rural areas like Nuwakot to teach lessons on puberty,\n the female reproductive system, and menstruation to boys and girls at Bacchala Devi School.'
db['KOICA'] = 'When Nepal experienced severe flooding in 2017, the Korean Aid Agency KOICA\n distributed emergency food, first aid kits, etc. PLUM partnered with KOICA to\n distribute 2000+ PLUM kits to female victims in the Terai area.'
db['Service Nepal'] = 'Every year, students from Lincoln School visit different places in rural Nepal for service\n projects. Among them are a number of PLUM members who educate and\n empower girls and boys to overcome period & puberty-related hurdles in society.'
db.close()