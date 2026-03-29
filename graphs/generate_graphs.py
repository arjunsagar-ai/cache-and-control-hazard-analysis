import os
import matplotlib.pyplot as plt

# -------- FUNCTION TO EXTRACT STATS --------
def get_stat(file_path, stat_name):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if stat_name in line:
                    return float(line.split()[1])
    except:
        print(f"Error reading {file_path}")
    return 0


# -------- PATHS --------
paths = {
    "TimingSimpleCPU": "../ControlHazard/timing_simple/stats.txt",
    "O3CPU": "../ControlHazard/o3/stats.txt"
}

results = {}

# -------- EXTRACT DATA --------
for cpu, path in paths.items():
    numCycles = get_stat(path, "numCycles")
    numInsts = get_stat(path, "simInsts")

    # Correct CPI calculation
    if numInsts != 0:
        CPI = numCycles / numInsts
    else:
        CPI = 0

    # Try multiple names for branch misprediction
    mispred = (
        get_stat(path, "branchMispred") or
        get_stat(path, "branchMispredicts") or
        get_stat(path, "condIncorrect")
    )

    results[cpu] = {
        "CPI": CPI,
        "mispred": mispred
    }


# -------- PREPARE DATA --------
cpus = list(results.keys())
cpi_values = [results[c]["CPI"] for c in cpus]
mispred_values = [results[c]["mispred"] for c in cpus]


# -------- GRAPH 1: CPI --------
plt.figure(figsize=(8,5))
bars = plt.bar(cpus, cpi_values)

plt.title("CPI Comparison (Control Hazard Impact)")
plt.xlabel("CPU Type")
plt.ylabel("CPI")

# Add values on bars
for i, v in enumerate(cpi_values):
    plt.text(i, v, f"{v:.2f}", ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("cpi_comparison.png", dpi=300)
plt.close()


# -------- GRAPH 2: Branch Misprediction --------
plt.figure(figsize=(8,5))
bars = plt.bar(cpus, mispred_values)

plt.title("Branch Mispredictions Comparison")
plt.xlabel("CPU Type")
plt.ylabel("Mispredictions")

# Add values on bars
for i, v in enumerate(mispred_values):
    plt.text(i, v, f"{int(v)}", ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("branch_misprediction.png", dpi=300)
plt.close()


print("\nGraphs generated successfully!")
print("✔ cpi_comparison.png")
print("✔ branch_misprediction.png")