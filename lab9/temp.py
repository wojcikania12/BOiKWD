from scipy.optimize import linprog
f = [-32,-24,-48];
A = [[2,2,5],[1,3,2],[3,1,3]];
b = [40,30,30];
bounds = bounds = (0, None);

res = linprog(f,A, b)
print(res.fun *(-1));


f = [-32,-24,-48];
A = [[2,2,5],[1,3,2],[3,1,3]];
b = [30,20,30];
bounds = bounds = (0, None);

res = linprog(f,A, b)

print("tak, zmniejszenie tych czasow wplynie na rozwiazanie");
print(res);
