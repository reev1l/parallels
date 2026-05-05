import csv
import matplotlib.pyplot as plt

PATH = "schedule_results.csv"

data = {
    "static": {"chunks": [], "times": []},
    "dynamic": {"chunks": [], "times": []},
    "guided": {"chunks": [], "times": []}
}

print(f"{'Schedule':<10} | {'Chunk':<8} | {'Work Time (s)'}")
print("-" * 40)

try:
    with open(PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sched = row["schedule"]
            chunk = int(row["chunk"])
            work_time = float(row["work_time_s"])
            
            if sched in data:
                data[sched]["chunks"].append(chunk)
                data[sched]["times"].append(work_time)
            
            print(f"{sched:<10} | {chunk:<8} | {work_time:.6f}")
except FileNotFoundError:
    print(f"Файл {PATH} не найден. Убедись, что путь правильный.")
    exit()

plt.figure(figsize=(10, 6))

for sched, values in data.items():
    if values["chunks"]:
        plt.plot(values["chunks"], values["times"], marker="o", label=f"schedule={sched}")

plt.xscale("log")
plt.xlabel("Chunk Size (log scale)")
plt.ylabel("Work Time (s) - Чем меньше, тем лучше")
plt.title("OpenMP Schedule Performance")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()

plt.savefig("schedule_comparison.png", dpi=200, bbox_inches="tight")
plt.show()