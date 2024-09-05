def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Number of disks
n = 3

# Names of the pegs
source = 'A'
auxiliary = 'B'
target = 'C'

# Call the function
tower_of_hanoi(n, source, auxiliary, target)
