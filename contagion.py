#1-personas que mueren por hora
#2-velocidad de contagio
#3-cuanto se tardará en que muera toda la poblacion


#PARÄMETROS
#1-poblacion total
#2-porcentaje inicial de gente contagiada
#3-numero de interacciones entre personas por dia
#4-duracion del virus(infinito)

import numpy as np
import matplotlib.pyplot as plt

def sir_model(N, I0, beta, gamma, contacts_per_day, days):
    # Initial values
    S = N - I0
    I = I0
    R = 0
    
    # Contact rate per day
    lambda_ = contacts_per_day / N
    
    # Lists to store results for plotting
    susceptible_list = [S]
    infected_list = [I]
    
    # SIR model simulation
    for day in range(days):
        dS = -beta * S * I / N
        dI = beta * S * I / N - gamma * I
        dR = gamma * I
        
        S += dS
        I += dI
        R += dR
        
        susceptible_list.append(S)
        infected_list.append(I)
    
    # Calculate percentages
    healthy_percentage = (S / N) * 100
    infected_percentage = (I / N) * 100
    
    return healthy_percentage, infected_percentage, susceptible_list, infected_list

# Parameters
total_population = 1000
initial_infected_percentage = 1  # 1%
transmission_rate = 0.15  # 15%
recovery_rate = 1 / 10  # 10 days infectious period
contacts_per_day = 10
simulation_days = 30

# Run the SIR model
healthy_percent, infected_percent, susceptible, infected = sir_model(
    total_population, 
    initial_infected_percentage * total_population / 100, 
    transmission_rate, 
    recovery_rate, 
    contacts_per_day, 
    simulation_days
)

# Print results
print(f"Percentage of Healthy Individuals: {healthy_percent:.2f}%")
print(f"Percentage of Infected Individuals: {infected_percent:.2f}%")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('SIR Model Simulation')
plt.legend()
plt.show()


