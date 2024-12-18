import random
import math

def exponentialTime(rate):
    
    return -1 / rate * math.log(1 - random.random())

def simulateTime(rate, simulations=10000):

    waiting_times = [exponentialTime(rate) for _ in range(simulations)]
    avg_time = sum(waiting_times) / simulations
    return avg_time

average_rate = 6 
lambda_rate = average_rate / 60  

simulated_avg_time = simulateTime(lambda_rate)


theoretical_time = 1 / lambda_rate

print(f"Theoretical average waiting time: {theoretical_time:.2f} minutes")
print(f"Simulated average waiting time: {simulated_avg_time:.2f} minutes")
