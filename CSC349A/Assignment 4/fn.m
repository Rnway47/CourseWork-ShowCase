%use it in Bisect.m, for 1c)

function V =  fn(m)
    V = 9.81 * m / 13.5 * (1 - exp(1)^(-135/m)) - 40;
End