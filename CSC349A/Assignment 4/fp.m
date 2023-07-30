%use it in Newton.m, for 2c), 2d)

function y = fp(t)
    y = -exp(-t) * (18*pi*sin(2*pi*t)+9*cos(2*pi*t));
end