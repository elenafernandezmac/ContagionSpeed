import numpy as np
import matplotlib.pyplot as plt


#esta funcion define el modelo SIR (Susceptible-Infectado-Recuperado). Este modelo divide a la población en tres categorías: susceptibles, infectados y recuperados y calcula como varian estos grupos en el tiempo
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
    
    # Variables to store epidemic peak
    epidemic_peak_day = 0
    epidemic_peak_infected = infectados
    
    # SIR model simulation
    for day in range(days):
        cambio_sanos  = -rango_transimision * gente_sana * infectados / poblacion
        cambio_infectados  = rango_transimision * gente_sana * infectados / poblacion - gamma * infectados
        cambio_recuperados = gamma * infectados
        
        gente_sana += cambio_sanos
        infectados += cambio_infectados
        recuperandose += cambio_recuperados
        
        susceptible_list.append(gente_sana)
        infected_list.append(infectados)
        
        # Check for epidemic peak
        if infectados > epidemic_peak_infected:
            epidemic_peak_infected = infectados
            epidemic_peak_day = day + 1  # Adjusting for 0-based indexing
    
    # Calculate percentages
    healthy_percentage = (gente_sana / poblacion) * 100
    infected_percentage = (infectados / poblacion) * 100
    
    return healthy_percentage, infected_percentage, susceptible_list, infected_list, epidemic_peak_day, epidemic_peak_infected

# Parameters
total_population = int(input("cuanta poblacion inicial tenemos?"))
initial_infected_percentage = float(input("cuanto porcentaje inicial de gente infectada hay?"))  
transmission_rate = float(input("cuanto porcentaje de transmision tiene el virus?"))  
recovery_rate = float(input("cuanto porcentaje de gente se recupera?"))  
contacts_per_day = int(input("cuantos contactos por dia hay?"))
simulation_days = int(input("cuantos dias dura la epidemia?"))
# Run the SIR model
healthy_percent, infected_percent, susceptible, infected, epidemic_peak_day, epidemic_peak_infected = sir_model(
    total_population, 
    initial_infected_percentage * total_population / 100, 
    transmission_rate, 
    recovery_rate, 
    contacts_per_day, 
    simulation_days
)

# Print results
print(f"Porcentaje de personas saludables: {healthy_percent:.2f}%")
print(f"Porcentaje de personas infectadas: {infected_percent:.2f}%")
print(f"Pico de la epidemia en el día {epidemic_peak_day}: {epidemic_peak_infected:.0f} personas infectadas")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('SIR Model Simulation')
plt.legend()
plt.show()
