import pickle

with open ('project/about.pickle', 'wb') as pf:
    d1 = {}
    d1['Mission'] = "To Empower girls to stay in school by educating them about their menstrual cycle and distributing eco-friendly sanitary napkins.\n Kindly visit our website to find out more about the impact we have made through various projects. "
    d1['Story'] = "International students attending Lincoln School in Kathmandu, Nepal started this student-led NGO in 2016 with inspiration from (Tanzania)--\n The Purple Box Project that provides free sanitary pads to those who don't have access."
    d1['PLUM?'] = "PLUM is derived from Nepali and Korean. Menstruation in English is commonly called period.\n In Korean, it is referred to as magic (마법).\n Magic in Nepali is जादू,(Jādū).\n जादू (Jādū) is the same pronunciation of plum in Korean."
    d1['partners'] = "PLUM is aided by organizations such as KOICA - Korea International Cooperation Agency in Nepal in terms of donations and aid.\n Often, fundraises are conducted to raise money for this important cause so contributions are highly valued.\n Please visit the contact/contribute page and help students make a difference!"
    
    pickle.dump(d1, pf)
    
