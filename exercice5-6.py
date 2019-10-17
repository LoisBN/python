#encoding:utf8

#question 1
def base_comp(base):
    if base == "A":
        return "T"
    if base == "G":
        return "C"
    if base == "T":
        return "A"
    if base == "C":
        return "G"
    else:
        return "erreur votre base azoté n'est pas valide"

assert base_comp('A') == "T"
assert base_comp('G') == "C"
assert base_comp('T') == "A"
assert base_comp('C') == "G"

#question 2
def brin_comp(brin):
    i = 0
    brin_comp = ""
    while i<len(brin):
        brin_comp = base_comp(brin[i]) + brin_comp
        i = i+1
    return brin_comp

print(brin_comp("ATCG"))

#question 3
def test_comp(a,b):
    if len(a) == len(b):
        return brin_comp(a) == b
    else:
        return False

assert test_comp('ATTGCCGTATGTATTGCGCT', 'AGCGCAATACATACGGCAAT') == True
assert test_comp('ATCG', '') == False

#question 4
def test_sous_sequence(a,b):
    if len(a) <= len(b):
        i = 0
        test = False
        while i + len(a) < len(b):
            if a == b[i:i+len(a)]:
                test = True
            i = i+1
        return test
    return False

assert test_sous_sequence('ABCD',"EFGHABCDIJK") == True
assert test_sous_sequence("","ATCG") == True



