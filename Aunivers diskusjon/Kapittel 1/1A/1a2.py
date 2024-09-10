"""
Vannflaske som betår av (fra nederst til øverst)
halvkule med radius r og høyde r
sylinder med radius r og høyde h1
kjegle med radius r og høyde h2

formlene for volumet av disse er
"""
import math

r = 0.41  #dm

#v_kule
v_halvkule = 2*math.pi*r*r*r/3

#v_sylinder
h1 = 0.5 #dm
v_syl = math.pi*r**2*h1

#v_kjegle
h2 = 0.5 #dm
v_kjegle = math.pi*r**2*h2/3

#v_total
v_tot = v_halvkule+v_syl+v_kjegle

print(f"v_tot er lik {v_tot: .2f}")