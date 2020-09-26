#Lab #4 Python Code, ezzhou

#Mass of Cart (kg)
mCart = 0.4999
mDEV = 0.0001

#Trial Speed
speed = #trialSpeed

#Initial Velocity (m/s)
Vi = #initial vel.
ViDEV = #uncertainity for vi

#Final Velocity (m/s)
Vf = #final vel.
VfDEV = #uncertainity for vf

#Initial Momentum (kgm/s)
Pi = round(Vi * mCart, 3)
PiDEV = round(Pi * (ViDEV/Vi + mDEV/mCart), 3)

#Final Momentum (kgm/s)
Pf = round(Vf * mCart, 3)
PfDEV = round(Pf * (VfDEV/Vf + mDEV/mCart), 3)

#Print Results
print("Results of ", speed, "trial:")
print("Initial Momentum was:", Pi, "kgm/s, with an uncertainty of", PiDEV, "kgm/s.")
print("Final Momentum was  :", Pf, "kgm/s, with an uncertainty of", PfDEV, "kgm/s.")