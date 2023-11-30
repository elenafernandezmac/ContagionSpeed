
import numpy as np
import matplotlib.pyplot as plt


print("Este programa mostrará la expansión del contagio de un virus respecto al tiempo que elijamos.")

#modelo SIR (Susceptible-Infectado-Recuperado). divide a la población en: susceptibles, infectados y recuperados y como estos varian en el tiempo
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
        cambio_gente_sana = -rango_transimision * gente_sana * infectados / poblacion
        cambio_infectados = rango_transimision * gente_sana * infectados / poblacion - gamma * infectados
        cambio_recuperados = gamma * infectados
        
        gente_sana += cambio_gente_sana
        infectados += cambio_infectados
        recuperandose += cambio_recuperados
        
        susceptible_list.append(gente_sana)
        infected_list.append(infectados)
    
    # Calculate percentages
    healthy_percentage = (gente_sana / poblacion) * 100
    infected_percentage = (infectados / poblacion) * 100
    
    return healthy_percentage, infected_percentage, susceptible_list, infected_list

# Parameters
total_population = int(input("cuanta poblacion inicial tenemos?"))
initial_infected_percentage = int(input("cuanto porcentaje inicial de gente infectada hay?"))
transmission_rate = int(input("cuanto porcentaje de transmision tiene el virus?"))  
recovery_rate = int(input("cuanto porcentaje de gente se recupera?"))  
contacts_per_day = int(input("cuantos contactos por dia hay?"))
simulation_days = int(input("cuantos dias dura la epidemia?"))

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


