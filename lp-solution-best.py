import pulp
import pandas as pd

# best case scenario

df = pd.read_csv("project-plan.csv", header=0)

tasks = df.to_dict(orient="records")

prob = pulp.LpProblem("Minimize Cost", pulp.LpMinimize)

# generate variable for each task
task_hours = {
    task["taskID"]: pulp.LpVariable(task["task"], lowBound=task["bestCaseHours"],
                                    cat='Continuous')
    for task in tasks
}


# define objective function
prob += pulp.lpSum([task["hourlyRate"] * task_hours[task["taskID"]] for task in tasks]), "Total Cost"


prob.solve()


if pulp.LpStatus[prob.status] == "Optimal":
    total_cost = 0
    for task in tasks:
        hours_spent = task_hours[task["taskID"]].varValue
        cost = task["hourlyRate"] * hours_spent
        total_cost += cost
        print(f"{task['task']}: {hours_spent} hours, Cost: ${cost:.2f}")
    print(f"Total Minimum Cost: ${total_cost:.2f}")
else:
    print("No optimal solution found")