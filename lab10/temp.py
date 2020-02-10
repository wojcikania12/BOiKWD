from scipy.optimize import linprog


f=[-23,-17];
A=[[4,3],[1,1]];
rA=[190,55]

bounds = (0, None);

res = linprog(f,A, rA, bounds=(bounds,bounds))
print(res.x);

A=[[4,3],[1,1], [1,0]];
rA=[190,55, 47]

bounds = (0, None);

res = linprog(f,A, rA, bounds=(bounds,bounds))
print(res.x);


f=[-23,-17];
A=[[4,3],[1,1], [1,0],[0,-1]];
rA=[190,55, 47,-1]

bounds = (0, None);

res = linprog(f,A, rA, bounds=(bounds,bounds))
print(res.x);

f=[-23,-17];
A=[[4,3],[1,1], [1,0],[0,-1]];
rA=[190,55, 46,-1]

bounds = (0, None);

res = linprog(f,A, rA, bounds=(bounds,bounds))
print(res.x);
print("lancuszkow: ",res.x[0]," pierscionkow: ",res.x[1])


