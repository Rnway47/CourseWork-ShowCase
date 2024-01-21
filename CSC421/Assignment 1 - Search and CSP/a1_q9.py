def isComplete(assignment):
    return None not in (assignment.values())

def select_unassigned_variable(variables, assignment):
    for var in variables:
        if assignment[var] is None:
            return var

def is_consistent(assignment, constraints):
    for constraint_violated in constraints:
        if constraint_violated(assignment):
          return False
    return True

def init_assignment(csp):
    assignment = {}
    for var in csp["VARIABLES"]:
        assignment[var] = None
    return assignment

def add_constraint(csp, constraint): 
    csp['CONSTRAINTS'].append(constraint)
    
def recursive_backtracking(assignment, csp):
    if isComplete(assignment):
        return assignment
    var = select_unassigned_variable(csp["VARIABLES"], assignment)
    for value in csp["DOMAINS"]:
        assignment[var] = value
        if is_consistent(assignment, csp["CONSTRAINTS"]):
            result = recursive_backtracking(assignment, csp)
            if result != "FAILURE":
                return result
        assignment[var] = None
    return "FAILURE"

def unary_constraint(variable, violations):
    return lambda asmt: asmt[variable] in violations

def binary_constraint(var_pair, violations):
    (v1,v2) = var_pair
    return lambda asmt: (asmt[v1], asmt[v2]) in violations

def ternary_constraint(v_ternary, violations):
    (v_sum, v1,v2) = v_ternary
    return lambda asmt: (asmt[v_sum], asmt[v1], asmt[v2]) in violations

csp1 = {"VARIABLES": ["I","F","X","Y","Z","W"],
        "DOMAINS": ["int", "float"],
        "CONSTRAINTS": []}
        
sum_violation = {("int", "float", "float"), ("float", "int", "int"), ("int", "int", "float"), ("int", "float", "int")}
assign_violation = {("int", "float"), ("float", "int")}

#type declaration
add_constraint(csp1, unary_constraint("I", ["float"])) #int I
add_constraint(csp1, unary_constraint("F", ["int"])) #float F

#assignment expression
add_constraint(csp1, binary_constraint(("X", "I"), assign_violation)) # X=I
for (v_sum, v1, v2) in [("Y", "X", "F"), ("Z", "X", "Y"), ("W", "X", "I")]:
    add_constraint(csp1, ternary_constraint((v_sum, v1, v2), sum_violation))
result = recursive_backtracking(init_assignment(csp1), csp1)
  
# add your code for CSP-based type inference as described in the notebook 
# below. The answer to the problem provided should be named result and 
# be a dictionary with a complete assignment of the variables to types 
# as returned by the CSP backtracking method. 