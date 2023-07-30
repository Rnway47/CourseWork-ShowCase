%  answer to 1(a), Euler function
%  m is the mass of the falling object
%  c is the drag coefficient
%  g is the gravity constant
%  t0 is the initial time
%  v0 is the initial velocity
%  tn is the final time at which the velocity is to be computed
%  n is the number of time steps into which [t0, tn] is divided

function Euler(m, c, g, t0, v0, tn, n)
% print headings and initial conditions
fprintf('values of t  approximations v(t)\n')
fprintf('%8.3f', t0), fprintf('%19.4f\n', v0)
%compute step size h
h=(tn-t0)/n;
%  set t,v to the initial values 
t=t0;
v=v0;
%  compute v(t) over n time steps usings Euler's method
for i=1:n
    v=v+(g-c/m*v)*h;
    t=t+h;
    fprintf('%8.3f', t), fprintf('%19.4f\n', v)
end 