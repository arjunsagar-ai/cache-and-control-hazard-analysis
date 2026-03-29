import os
import matplotlib.pyplot as plt

# Policies
policies = ["LRU", "FIFO", "RANDOM"]
cpus = ["timing_simple", "o3"]

# Function to extract stat
def get_stat(file_path, stat_name):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if stat_name in line:
                    return float(line.split()[1])
    except:
        return 0
    return 0

# Store results
cpi_results = {}
miss_results = {}

for policy in policies:
    cpi_results[policy] = {}
    miss_results[policy] = {}

    for cpu in cpus:
        path = f"../{policy}/{cpu}/stats.txt"

        # CPI
        cpi = get_stat(path, "system.cpu.cpi")

        # Cache miss rate
        miss = get_stat(path, "overallMissRate")

        cpi_results[policy][cpu] = cpi
        miss_results[policy][cpu] = miss

# -------- GRAPH 1: CPI --------
plt.figure(figsize=(10,6))

x = range(len(policies))
width = 0.35

timing_cpi = [cpi_results[p]["timing_simple"] for p in policies]
o3_cpi = [cpi_results[p]["o3"] for p in policies]

plt.bar([i - width/2 for i in x], timing_cpi, width, label="TimingSimpleCPU")
plt.bar([i + width/2 for i in x], o3_cpi, width, label="O3 CPU")

plt.xticks(x, policies)
plt.xlabel("Cache Policy")
plt.ylabel("CPI")
plt.title("CPI Comparison for Cache Policies")

plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("cache_policy_cpi.png", dpi=300)
plt.close()

# -------- GRAPH 2: Cache Miss Rate --------
plt.figure(figsize=(10,6))

timing_miss = [miss_results[p]["timing_simple"] for p in policies]
o3_miss = [miss_results[p]["o3"] for p in policies]

plt.bar([i - width/2 for i in x], timing_miss, width, label="TimingSimpleCPU")
plt.bar([i + width/2 for i in x], o3_miss, width, label="O3 CPU")

plt.xticks(x, policies)
plt.xlabel("Cache Policy")
plt.ylabel("Miss Rate")
plt.title("Cache Miss Rate Comparison")

plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("cache_policy_miss_rate.png", dpi=300)
plt.close()

# -------- GRAPH 3: Miss Rate (Bar Chart) --------
plt.figure(figsize=(8,5))

miss_values = [miss_results[p]["o3"] for p in policies]

plt.bar(policies, miss_values)

plt.title("Cache Miss Rate Comparison (FIFO vs Random vs LRU)")
plt.xlabel("Policy")
plt.ylabel("Miss Rate")

# Add values on top
for i, v in enumerate(miss_values):
    plt.text(i, v, f"{v:.6f}", ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("miss_rate_bar.png", dpi=300)
plt.close()


# -------- GRAPH 4: Writebacks --------
writeback_results = {}

for policy in policies:
    path = f"../{policy}/o3/stats.txt"

    writebacks = (
        get_stat(path, "writebacks") or
        get_stat(path, "system.cpu.dcache.writebacks")
    )

    writeback_results[policy] = writebacks

plt.figure(figsize=(8,5))

wb_values = [writeback_results[p] for p in policies]

plt.bar(policies, wb_values)

plt.title("Cache Writebacks Comparison (FIFO vs Random vs LRU)")
plt.xlabel("Policy")
plt.ylabel("Writebacks")

# Add values
for i, v in enumerate(wb_values):
    plt.text(i, v, f"{int(v)}", ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("writebacks_comparison.png", dpi=300)
plt.close()

print("Cache policy graphs generated!")
