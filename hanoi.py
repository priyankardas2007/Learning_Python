def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = []

    def record_state():
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")

    record_state()

    def move(disks, source, auxiliary, target):
        if disks == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()
        else:
            move(disks - 1, source, target, auxiliary)

            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()

            move(disks - 1, auxiliary, source, target)

    move(n, 0, 1, 2)

    return "\n".join(states)
