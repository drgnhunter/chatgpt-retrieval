# from sympy import symbols, Eq, solve

# # Define symbols
# m1, x1, y1, u1, v1, m2, e, I1, I2, I3 = symbols('m1 x1 y1 u1 v1 m2 e I1 I2 I3')

# # User input for assumptions and target variables
# a = input("Write your assumptions : ")
# b = input("Name the variables you want to get ")

# # Define equations
# eq6 = Eq(m1*x1 + m2*y1 - m1*u1 + m2*v1, 0)
# eq5 = Eq(m1*x1 + m2*y1 - m1*u1 - m2*v1, 0)
# eq2 = Eq(y1 - x1 + e*(v1 - u1), 0)
# eq3 = Eq(I2 - m2*y1 + m2*v1, 0)
# eq4 = Eq(I3 - m1*x1 + m1*u1, 0)

# # User input for equations to use
# c = input("Mention the equations you going to use")

# # Solve equations
# sol = solve((eq6, eq5, eq2, eq3, eq4), symbols(b))
# print(sol)


from sympy import symbols, Eq, solve

# Define symbols
m1, m2, u1, v1, x1, y1, e, I2 = symbols('m1 m2 u1 v1 x1 y1 e I2')

# User input for assumptions and target variables
a = input("Write your assumptions : ")
b = input("Name the variables you want to get ")

# Define equations
eq5 = Eq(m1*x1 + m2*y1 - m1*u1 + m2*v1, 0)
eq2 = Eq(y1 - x1 + e*(v1 - u1), 0)
eq3 = Eq(I2 - m2*y1 + m2*v1, 0)

# Substituting assumptions into the equations
m1_value = 2
m2_value = 1
u1_value = symbols('u')
v1_value = -u1_value
x1_value = 0
y1_value = symbols('v')

eq5 = eq5.subs({m1: m1_value, m2: m2_value, u1: u1_value, v1: v1_value, x1: x1_value, y1: y1_value})
eq2 = eq2.subs({u1: u1_value, v1: v1_value, x1: x1_value, y1: y1_value})
eq3 = eq3.subs({m2: m2_value, y1: y1_value, v1: v1_value})

# User input for equations to use
c = input("Mention the equations you going to use")

# Solve equations
sol = solve((eq5, eq2, eq3), symbols(b))
print(sol)
