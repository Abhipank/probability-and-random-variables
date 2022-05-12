
Prob_E=0.001
#given in question
print("P(E) = ",Prob_E)

Prob_Ecomplement=0.999
#given in question
print("P(E') = ",Prob_Ecomplement)

Prob_AbyE=0.9
#given in question
print("P(A|E) = ",Prob_AbyE)

Prob_AbyEcomplement=0.01
#given in question
print("P(A|E') = ",Prob_AbyEcomplement)




#using bayes theorem
Prob_A=Prob_E*Prob_AbyE+Prob_Ecomplement*Prob_AbyEcomplement
print("P(A) = ",Prob_A)

Prob_EbyA=(Prob_E*Prob_AbyE)/Prob_A
print("P(E|A) = ",Prob_EbyA)