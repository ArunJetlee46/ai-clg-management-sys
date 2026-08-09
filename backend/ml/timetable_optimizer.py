from ortools.sat.python import cp_model


def solve_timetable():
    model = cp_model.CpModel()
    courses = ["DS", "OS", "DBMS"]
    rooms = ["R1", "R2"]
    slots = range(4)

    x = {}
    for c in courses:
        for r in rooms:
            for s in slots:
                x[(c, r, s)] = model.NewBoolVar(f"{c}_{r}_{s}")

    for c in courses:
        model.Add(sum(x[(c, r, s)] for r in rooms for s in slots) == 1)

    for r in rooms:
        for s in slots:
            model.Add(sum(x[(c, r, s)] for c in courses) <= 1)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 5
    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return []

    schedule = []
    for c in courses:
        for r in rooms:
            for s in slots:
                if solver.Value(x[(c, r, s)]) == 1:
                    schedule.append({"course": c, "room": r, "slot": int(s)})
    return schedule


if __name__ == "__main__":
    print(solve_timetable())
