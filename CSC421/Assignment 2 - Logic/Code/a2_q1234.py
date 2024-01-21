
# Add the code for this function as described in the notebook 
def evaluate(s):
    prefix_list = s.split(" ")
    if prefix_list[0] == "&": #determine &, =>, <=>, or | start with &
        return int(prefix_list[1])&int(prefix_list[2])#return true when both operands are T
    elif prefix_list[0] == "=>": # =>
        return 0 if prefix_list[1] == "1" and prefix_list[2] == "0" else 1 #False only when T => F
    elif prefix_list[0] == "<=>":
        return int(prefix_list[1] == prefix_list[2])#return True when both operands are equal to each other
    elif prefix_list[0] == "|":
        return 0 if prefix_list[1] == prefix_list[2] == "0" else 1 #False only when both are False
# Examples test cases
e1 = "| 0 1" # 1
e2 = "<=> 1 1" # 1
e3 = "& 0 0" # 0

res_e1 = evaluate(e1)
res_e2 = evaluate(e2)
res_e3 = evaluate(e3)

print(f'{e1} = {res_e1}')
print(f'{e2} = {res_e2}')
print(f'{e3} = {res_e3}')

d = {'foo': 0, 'b': 1}
print(d)
be1 = '& 0 1'
be2 = '& foo 1'
be3 = '& foo ~b'


# Add the code for this function 
def evaluate_with_bindings(s,d):
    new_dict = {}
    for item in d.keys():
        new_dict[item] = d[item]
        new_dict["~"+item] = int(not d[item])
    #expression evaluation, replace d with its value
    prefix_list = s.split(" ")
    for symbol in prefix_list:
        if symbol in new_dict.keys():
            prefix_list[prefix_list.index(symbol)] = new_dict[symbol]
    if prefix_list[0] == "&": #determine &, =>, or <=>, start with &
        return int(prefix_list[1])&int(prefix_list[2])#return true when both operands are T
    elif prefix_list[0] == "=>": # =>
        return 0 if prefix_list[1] == "1" and prefix_list[2] == "0" else 1 #False only when T => F
    elif prefix_list[0] == "<=>":
        return int(prefix_list[1] == prefix_list[2])#return True when both operands are equal to each other
    elif prefix_list[0] == "|":
        return 0 if prefix_list[1] == prefix_list[2] == "0" else 1 #False only when both are False
  

# Example test cases 
res_be1 = evaluate_with_bindings(be1,d)
res_be2 = evaluate_with_bindings(be2,d)
res_be3 = evaluate_with_bindings(be3,d)

print(f'{be1} = {res_be1}')
print(f'{be2} = {res_be2}')
print(f'{be3} = {res_be3}')


# # Add the code for this function as described in the notebook 
# # You can add helper functions if you want as long as the function works as expected 
def recursive_prefix_eva(input):
    head, tail = input[0], input[1:]
    if head in ['&', '=>', "<=>", "|"]: #break input when counters operators
        val1, tail = recursive_prefix_eva(tail)
        val2, tail = recursive_prefix_eva(tail)
        if head == '&': 
            return (int(int(val1)&int(val2)), tail)
        elif head == '=>':
            return (0, tail) if val1 == 1 and val2 == 0 else (1, tail)
        elif head == "<=>":
            return (int(int(val1)==int(val2)), tail)
        elif head == "|":
            return (0, tail) if val1 == val2 == "0" else (1, tail) #False only when both are False
    # operator is a number 
    else:  
        return (int(head),tail)

def prefix_eval(input_str, d): 
    new_dict = {}
    for item in d.keys():
        new_dict[item] = d[item]
        new_dict["~"+item] = int(not d[item])
    #expression evaluation, replaced with its value
    prefix_list = input_str.split(" ")
    for symbol in prefix_list:
        if symbol in new_dict.keys():
            prefix_list[prefix_list.index(symbol)] = new_dict[symbol]
    result, tail = recursive_prefix_eva(prefix_list)
    return result

d = {"a": 1, "b": 0}
pe1 = "& a | 0 1"
pe2 = "& 0 | 1 b"
pe2 = "| 1 => ~b b"
pe3 = "<=> b <=> ~b 0"
pe4 = "=> 1 & a 0"
pe5 = "& ~a <=> 0 0"

print(d)
for e in [pe1,pe2,pe3,pe4,pe5]:
    print("%s \t = %d" % (e, prefix_eval(e,d)))

### SAMPLE OUTPUT 
# | 0 1 = 1
# <=> 1 1 = 1
# & 0 0 = 0
# {'foo': 0, 'b': 1}
# & 0 1 = 0
# & foo 1 = 0
# & foo ~b = 0
# {'a': 1, 'b': 0}
# & a | 0 1        = 1
# | 1 => ~b b      = 1
# <=> b <=> ~b 0   = 1
# => 1 & a 0       = 0
# & ~a <=> 0 0     = 0



