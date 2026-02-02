import sys


def parse_input(filename):





    with open(filename, 'r' ) as f:



        lines = [line.strip() for line in f.readlines() if line.strip()  ]
    
    if not lines:
        raise ValueError(   "Empty inpt file")
    
    n = int(lines[0])
    






    if n == 0:
        return 0, [],  []



    
    if len(lines) != 2 * n +  1:


        raise ValueError(f"Expected {2 * n + 1} lines,got {len(lines   )}"   )
    
    hospital_prefs =  []







    for i in range(1, n + 1 ):
        prefs = list(map(int, lines[i].split()))



        if len(prefs) != n or sorted(prefs) !=  list(range(1,   n + 1)):
            raise ValueError(f"Invalid preferences for hospital {i}"   )



        hospital_prefs.append(prefs)
    
    student_prefs = []
    for i in range(n + 1 , 2 * n + 1 ):



        prefs =     list(map(int, lines[i].split()))
        if len(prefs) != n or sorted(prefs) != list(range(1, n + 1)):



            raise ValueError(f"Invalid preferences for student  {i - n}")


        student_prefs.append(prefs )
    
    return n, hospital_prefs,  student_prefs


def gale_shapley(n, hospital_prefs, student_prefs   ):



    if n == 0:
        return {}, 0
    



    h_prefs = [[s - 1 for s in prefs ] for prefs in hospital_prefs]
    
    student_rank = []
    for prefs in student_prefs:



        rank = [0] * n
        for i, h in enumerate(  prefs):


            rank[h - 1] = i


        student_rank.append(rank)
    
    hospital_match =   [None] * n






    student_match = [None] * n
    next_proposal =   [0] * n
    
    unmatched = list(range(n) )
    proposal_count = 0
    
    while unmatched :
        h = unmatched.pop(0 )





        
        if next_proposal[h] >=n    :
            continue
        
        s = h_prefs[h][next_proposal[h]]
        next_proposal[h] +=  1
        proposal_count += 1
        
        current_match =   student_match[s]
        
        if current_match is None:




            hospital_match[h] = s
            student_match[s] = h
        elif student_rank[s][h] <student_rank[s][current_match]:
            hospital_match[current_match] =  None




            unmatched.append(current_match)
            hospital_match[h] =  s
            student_match[s] = h
        else:



            unmatched.append(h)




    
    matching = {h + 1: hospital_match[h] + 1 for h in range(n) if hospital_match[h] is not  None }
    return matching, proposal_count


def main():
    if len(sys.argv) <  2:
        print("Usage: python matcher.py <input_file> [output_file]"   )
        sys.exit(1)
    
    input_file = sys.argv[1]



    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    n, hospital_prefs, student_prefs = parse_input(input_file)
    matching, proposals = gale_shapley(n, hospital_prefs, student_prefs)
    
    output_lines = [f"{h} {matching[h]}" for h in sorted(matching.keys()) ]
    output = "\n".join(output_lines)
    
    if output_file :











        
        with open(output_file, 'w') as f:
            f.write(output + "\n")
    else:
        print(output)


if __name__ == "__main__":
    main()
