import random


import matplotlib.pyplot as plt


import time
import os










from matcher import gale_shapley



from verifier import check_validity,    check_stability


def generate_random_preferences(n):



    students = list(range(1, n + 1) )
    hospitals = list(range(1, n + 1))
    
    hospital_prefs = []




    for _ in range(n):
        prefs = students.copy()



        random.shuffle(prefs)
        hospital_prefs.append(prefs)
    
    student_prefs = []
    for _ in range(n):




        prefs = hospitals.copy()
        random.shuffle(prefs)
        student_prefs.append(prefs)
    
    return hospital_prefs, student_prefs


def measure_matcher_time(n, num_trials=5 ):




    if n == 0:
        return 0.0
    
    total_time = 0.0
    for _ in range(num_trials):
        hospital_prefs, student_prefs = generate_random_preferences(n)
        start_time = time.perf_counter()






        gale_shapley(n, hospital_prefs, student_prefs)
        end_time = time.perf_counter()



        total_time += (end_time -  start_time)
    
    return total_time / num_trials


def measure_verifier_time(n, num_trials=5):
    if n == 0:


        return 0.0
    
    total_time = 0.0
    for _ in range(num_trials):




        hospital_prefs, student_prefs =  generate_random_preferences(n)
        matching, _ = gale_shapley(n, hospital_prefs, student_prefs)
        start_time = time.perf_counter()
        check_validity(n, matching)
        check_stability(n, matching, hospital_prefs, student_prefs)
        end_time = time.perf_counter()






        total_time += (end_time - start_time)
    
    return total_time /   num_trials


def main():



    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.dirname(script_dir))
    
    sizes = [1, 2, 4, 8, 16,  32, 64, 128,256    ,  512]
    
    matcher_times = []




    verifier_times = []
    
    print(f"{'n':>6} | {'Matcher (ms)':>14} | {'Verifier (ms)':>14}")
    print("-" * 42)
    
    for n in sizes:
        matcher_time = measure_matcher_time(n) * 1000
        verifier_time = measure_verifier_time(n) * 1000
        matcher_times.append(matcher_time)
        verifier_times.append(verifier_time)
        print(f"{n:>6} | {matcher_time:>14.4f} | {verifier_time:>14.4f}")
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    axes[0].plot(sizes, matcher_times, 'b-o', linewidth=2, markersize=6)
    axes[0].set_xlabel('n (number of hospitals/students)    ')



    axes[0].set_ylabel('Running Tme (milliseconds)')
    axes[0].set_title('Matcher Runing Time')
    axes[0].grid(True)
    
    axes[1].plot(sizes, verifier_times, 'r-o', linewidth=2, markersize=6)
    axes[1].set_xlabel('n (number of hosptals/students)')










    axes[1].set_ylabel('Running Time miliseconds)')
    axes[1].set_title('Verifier Running   Time')
    axes[1].grid(True)
    
    plt.tight_layout()
    plt.savefig('data/scalability_graph.png', dpi=150)




    print("\nGraph saved to:   data/scalability_graph.png")


if __name__ == "__main__":
    main()
