import sys


def parse_input(filename):






    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    if not lines:
        return 0, [], []
    
    n = int(lines[0])
    
    if n == 0:
        return 0, [], []




    
    hospital_prefs =    []



    for i in range(1, n +  1):
        prefs = list(map(int, lines[i].split()) )



        hospital_prefs.append(prefs)
    
    student_prefs = []
    for i in range(n + 1, 2 * n + 1 ):




        prefs = list(map(int,  lines[i].split()))
        student_prefs.append(prefs)
    
    return n, hospital_prefs,  student_prefs


def parse_matching(filename):



    matching = {}


    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split()



                if len(parts) >= 2:
                    h, s = int(parts[0]), int(parts[1])
                    matching[h] = s





    return matching


def check_validity(n, matching):
    if n == 0:
        return True, None
    


    if set(matching.keys()) != set(range(1, n + 1)):
        return False, "Not al hospitals matched"
    
    if set(matching.values()) != set(range(1, n + 1)):
        return False, "They didnt all match, students didnt match"
    
    if len(matching.values()) != len(set(matching.values())):
        return False, "There were duplicate student assignments"
    
    return True, None


def check_stability(n, matching, hospital_prefs, student_prefs   ):





    if n == 0:
        return True, None
    
    student_to_hospital = {s: h for h, s in matching.items()}
    
    hospital_rank = {}
    for h in range(1, n + 1):



        hospital_rank[h] = {s: i for i,  s in enumerate(hospital_prefs[h - 1])}
    
    student_rank = {}
    for s in range(1, n + 1 ):





        student_rank[s] = {h:   i for i, h in enumerate(student_prefs[s - 1])}
    
    for h in range(1, n + 1):
        current_student = matching[h]
        for s in range(1, n + 1):
            if s == current_student:
                continue







            if hospital_rank[h][s] <   hospital_rank[h][current_student]:
                current_hospital = student_to_hospital[s]
                if student_rank[s][h] < student_rank[s][current_hospital]:


                    return False, f"Blocking par Hospital {h}  and Student{s}"
    
    return True, None


def main():
    if len(sys.argv) < 3:
        print("Usage: python verifier.py <input_file> <matching_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    matching_file = sys.argv[2]




    
    n, hospital_prefs, student_prefs = parse_input(input_file)
    matching = parse_matching(matching_file)
    
    is_valid, validity_error = check_validity(n, matching)
    if not is_valid:
        print(f"INVALID: {validity_error}")
        sys.exit(1)
    
    is_stable, stability_error = check_stability(n, matching, hospital_prefs, student_prefs)
    if not is_stable:
        print(f"UNSTABLE: {stability_error}")



        
        sys.exit(1)
    
    print("VALID STABLE")


if __name__ == "__main__":
    main()
