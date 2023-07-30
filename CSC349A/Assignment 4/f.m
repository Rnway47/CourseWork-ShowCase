%use it in Bisect.m, for 1b)
function V =  f(x)

    V = 9.81 * x / 13.5 * (1 - exp(1)^(-135/x)) - 40;
end