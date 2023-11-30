import numpy as np
import matplotlib.pyplot as plt

def sir_model(poblacion, infectados_iniciales, rango_transimision, gamma, contacts_per_day, days):
    # Initial values
    gente_sana = poblacion - infectados_iniciales
    infectados = infectados_iniciales
    recuperandose = 0
    muerte = 0  # Variable to store deaths
    
    # Contact rate per day
    lambda_ = contacts_per_day / poblacion
    
    # Lists to store results for plotting
    susceptible_list = [gente_sana]
    infected_list = [infectados]
    death_list = [muerte]
    
    # Variables to store epidemic peak
    epidemic_peak_day = 0
    epidemic_peak_infected = infectados
    
    # SIR model simulation
    for day in range(days):
        cambio_sanos  = -rango_transimision * gente_sana * infectados / poblacion
        cambio_infectados  = rango_transimision * gente_sana * infectados / poblacion - gamma * infectados
        cambio_recuperados = gamma * infectados
        
        # Calculate deaths (assuming a constant death rate for simplicity)
        muerte += gamma * infectados
        
        gente_sana += cambio_sanos
        infectados += cambio_infectados
        recuperandose += cambio_recuperados
        
        susceptible_list.append(gente_sana)
        infected_list.append(infectados)
        death_list.append(muerte)
        
        # Check for epidemic peak
        if infectados > epidemic_peak_infected:
            epidemic_peak_infected = infectados
            epidemic_peak_day = day + 1  # Adjusting for 0-based indexing
    
    # Calculate percentages
    healthy_percentage = (gente_sana / poblacion) * 100
    infected_percentage = (infectados / poblacion) * 100
    
    return healthy_percentage, infected_percentage, susceptible_list, infected_list, death_list, epidemic_peak_day, epidemic_peak_infected

# Parameters
total_population = int(input("cuánta población inicial tenemos?"))
initial_infected_percentage = float(input("cuánto porcentaje inicial de gente infectada hay?"))  
transmission_rate = float(input("cuánto porcentaje de transmisión tiene el virus?"))  
recovery_rate = float(input("cuánto porcentaje de gente se recupera?"))  
contacts_per_day = int(input("cuántos contactos por día hay?"))
simulation_days = int(input("cuántos días dura la epidemia?"))

# Run the SIR model
healthy_percent, infected_percent, susceptible, infected, deaths, epidemic_peak_day, epidemic_peak_infected = sir_model(
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
print(f"Número total de muertes: {deaths[-1]:.0f}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.plot(deaths, label='Deaths', linestyle='dashed')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('SIR Model Simulation with Deaths')
plt.legend()
plt.show()
