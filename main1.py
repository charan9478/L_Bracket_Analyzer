import numpy as np

# ================== FUNCTION TO PROCESS ONE FILE ==================
def process_file(stress_file, deformation_file, load):
    # Read only the needed column (much lighter)
    stress = np.genfromtxt(stress_file, delimiter=',', skip_header=1, usecols=1)
    deformation = np.genfromtxt(deformation_file, delimiter=',', skip_header=1, usecols=1)
    
    max_stress = np.max(stress) / 1e6
    mean_stress = np.mean(stress) / 1e6
    max_def = np.max(deformation)
    mean_def = np.mean(deformation)
    
    return {
        'load': load,
        'max_stress': max_stress,
        'mean_stress': mean_stress,
        'max_def': max_def,
        'mean_def': mean_def
    }

# ================== PROCESS ALL LOADS ==================
results = []

results.append(process_file("stress_250N.csv", "totaldeformation_250N.csv", 250))
results.append(process_file("stress_500N.csv", "totaldeformation_500N.csv", 500))
results.append(process_file("stress_750N.csv", "totaldeformation_750N.csv", 750))
results.append(process_file("stress_750N.csv", "totaldeformation_1500N.csv", 1500))
results.append(process_file("stress_750N.csv", "totaldeformation_2000N.csv", 2000))

# ================== SAVE ALL RESULTS AT ONCE ==================
with open("results.txt", "w") as f:
    f.write("=== L-BRACKET ANALYSIS RESULTS ===\n\n")
    
    for r in results:
        f.write(f"----- {r['load']} N -----\n")
        f.write(f"Max Stress             : {r['max_stress']} MPa\n")
        f.write(f"Mean Stress            : {r['mean_stress']} MPa\n")
        f.write(f"Max Total Deformation  : {r['max_def']} meters\n")
        f.write(f"Mean Total Deformation : {r['mean_def']} meters\n\n")
        


print("All results saved successfully in results.txt")