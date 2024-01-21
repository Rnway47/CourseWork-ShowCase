parent(_,_).
child(_,_).
sibling(_,_).
parent(X,Y) :- child(Y,X).
child(X,Y), child(Z,X) :- sibling(X,Z).

parent(homer, bart).
parent(homer, lisa).
parent(homer, maggie).
parent(marge, bart).
parent(marge, lisa).
parent(marge, maggie).

Query:
child(X, homer).
parent(X, bart).
sibling(lisa, homer).
sibling(lisa, bart).
sibling(bart,bart).