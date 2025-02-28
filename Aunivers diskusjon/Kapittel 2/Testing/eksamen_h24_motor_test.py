import eksamen_h24_motor as c
#c meaning class

#testing
#test1: batteriet skal ikke kunne lades opp mer enn kapasiteten
test_batt = c.batteri(energi_kapasitet=100, energi_nivå=50)

test_batt.lad_opp(101)
