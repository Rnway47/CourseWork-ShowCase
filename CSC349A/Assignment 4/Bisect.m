% answer to 1a), Bisect function

function root = Bisect(xl, xu, eps, imax, f)
fprintf('iteration approximation \n')

i = 1;
fl = f(xl);

while i <= imax
    xr = (xl + xu)/2;
    fr = f(xr);
    fprintf('%6.0f %18.8f\n', i, xr)
    if fr == 0 || (xu-xl)/abs(xu+xl) < eps
        root = xr;
        return;
    end

    i = i+1;
    if (fl*fr) < 0
        xu = xr;
    else
        xl = xr;
        fl = fr;
    end
end
    fprintf('failed to converge in %g iterations\n', imax)