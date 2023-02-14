
import random

# Variables.
queue_length = 0
our_lambda = [0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745]
mu = 0.75
simulations = 1000000
queue_average = [0,0,0,0,0,0,0,0,0,0]

# For loop for each lambda value
for i in range(len(our_lambda)):
    queue_total = 0

    # For loop for 1 million simulations on each lambda value.
    for t in range(simulations):
        packet_arrived = random.random() <= our_lambda[i]
        packet_departed = random.random() <= mu

        if packet_arrived:
            queue_length = queue_length + 1

        if packet_departed and queue_length != 0:
            queue_length = queue_length - 1

    # Used to get the average over the simulation rather than final value.
        queue_total = queue_total + queue_length
    queue_average[i] = round(queue_total/simulations,4)

    print(str(our_lambda[i]) + ", " + str(queue_average[i]))