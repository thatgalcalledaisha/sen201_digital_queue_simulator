number_of_people = int(input("Enter number of people in the queue: "))
service_time = int(input("Enter service time per person (minutes): "))

print("\nQueue Simulation Results")

total_waiting_time = 0

for position in range(1, number_of_people + 1):
    waiting_time = (position - 1) * service_time
    total_waiting_time += waiting_time
    print("Person", position, "waiting time:", waiting_time, "minutes")

print("\nTotal waiting time for all people:", total_waiting_time, "minutes")