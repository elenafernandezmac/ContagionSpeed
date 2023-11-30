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



def sir_model(poblacion, infectados_iniciales, rango_transimision, gamma, contacts_per_day, days):
    # Initial values
    gente_sana = poblacion - infectados_iniciales
    infectados = infectados_iniciales
    recuperandose = 0
    
    # Contact rate per day
    lambda_ = contacts_per_day / poblacion
    
    # Lists to store results for plotting
    susceptible_list = [gente_sana]
    infected_list = [infectados]
    
    # SIR model simulation
    for day in range(days):
        dS = -rango_transimision * gente_sana * infectados / poblacion
        dI = rango_transimision * gente_sana * infectados / poblacion - gamma * infectados
        dR = gamma * infectados
        
        gente_sana += dS
        infectados += dI
        recuperandose += dR
        
        susceptible_list.append(gente_sana)
        infected_list.append(infectados)
    
    # Calculate percentages
    healthy_percentage = (gente_sana / poblacion) * 100
    infected_percentage = (infectados / poblacion) * 100
    
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


