import numpy as np
import chempy as ch

species = []
done = "n"
while done == "n":
    specin = input("Input the chemical formula for one type of chemical in the reaction network: ")
    species.append(specin)
    done = input("done inputting chemicals? y or n: ")

current_state = []
print("chemical order: ", species)
counter = 1
while counter <= len(species):
    current_state.append(float(input("Input the concentration for each chemical in the current state of the system, in the order as you listed the chemicals above: ")))
    counter+=1
np.array(current_state)

end_state = []
counter = 1
while counter <= len(species):
    end_state.append(float(input("Input the concentration for each chemical in the desired end state of the system, in the order as you listed the chemicals above: ")))
    counter+=1
np.array(end_state)

reactions = []
reactions = list(ch.reactionsystem.ReactionSystem(rxns, species)
#convert reactions elements into proper form (see paper)

m = np.matrix([])
for i in reactions:
    x = i[1] - i[0]
    m.np.append(x)

relevant_reactions = []

F = m.I * (end_state - current_state)
reactions[:] = [x for x in reactions if F[x] > 0]

if not reactions:
    print("not reachable")
else:
    s = []
    for i in reactions:
        calc = 1/len(reactions) * sum(F[i])
        s.append(calc)
    np.array(s)
    epsilon = min(s)/2
    #compute the max support flux vector sequence U_c, epsilon
    v = s - u
    print("U: ",u, " epsilon: ",epsilon," v: ",v, " (padded with 0s for eliminated reactions)")

