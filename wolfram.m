(*Before Collision
First ball : m1
Velocity : u
Mass : m1

Second Ball : m2
Velocity : v
Mass : m2

*After Collision
First Ball: m1
Velocity : x
Mass: m1


Second Ball: m2
Velocity : y
Mass : m2

*) 

x1 =.;
y1 =. ;
 u1 =. ;
v1 =.;
z =.;

(*getting the assumptions as inputs *)
a = Input["Write your assumptions : ", {}];
b = Input["Name the variables you want to get ", {}];

eq6 = (m1*x1 + m2*y1) + (-m1*u1 + m2*v1) == 0;
eq5 = (m1*x1 + m2*y1) - (m1*u1 + m2*v1)  == 0;
eq2 = Assuming[{0 <= e <= 1, I1 == 0}, (y1 - x1) == -e*(v1 - u1)];
eq3 = Assuming[I2 != 0, I2 == m2*y1 - m2*v1];
eq4 = Assuming[I3 != 0, I3 == m1*x1 - m1*u1];
(*eq1=Assuming[I1 \[NotEqual] 0,(m1*x + m2*y)\[Equal] (m1*u+m2*v)];*)
\

(*eq4=(1 (m1*v^2))/2-(1 (m2*w^2))/2\[Equal](1 (m1*x^2))/2-(1 \
(m2*y^2))/2; *)
(*d = Input["Any Equations you gonna change"];*)
c = Input["Mention the equations you going to use", {}];
sol = Solve[c, b]