import numpy as np
import matplotlib.pyplot as plt

print("este programa nos dará datos sobre como evoluciona el contagio de un virus en una población con respecto al tiempo, mostrando la función de la gente contagiada y la susceptible/sana. Los parámetros del comportamiento del virus los elige el usuario")

def sir_model(poblacion, infectados_iniciales, rango_transimision, gamma, contacts_per_day, days):
    # Declaraos los valores iniciales.
    gente_sana = poblacion - infectados_iniciales
    infectados = infectados_iniciales
    recuperandose = 0
    muerte = 0  # Variable para almacenar el número de muertes.
    
    # Cotrastar los del día
    lambda_ = contacts_per_day / poblacion
    
    # Lista para guadrar los resultados para plotting
    susceptible_list = [gente_sana]
    infected_list = [infectados]
    death_list = [muerte]
    
    # Variables para guardar el pico de la epdidemia
    epidemic_peak_day = 0
    epidemic_peak_infected = infectados
    
    # Definimos el cambio de usuarios, sanos, infectados y recuoperados en función del tiempo
    for day in range(days):
        cambio_sanos  = -rango_transimision * gente_sana * infectados / poblacion
        cambio_infectados  = rango_transimision * gente_sana * infectados / poblacion - gamma * infectados
        cambio_recuperados = gamma * infectados
        
        # Calcular muertes (asumiendo muertes constantes en función)
        muerte += gamma * infectados
        
        gente_sana += cambio_sanos
        infectados += cambio_infectados
        recuperandose += cambio_recuperados
        
        susceptible_list.append(gente_sana)
        infected_list.append(infectados)
        death_list.append(muerte)
        
        # Comprobamos con el pico de la epidemia
        if infectados > epidemic_peak_infected:
            epidemic_peak_infected = infectados
            epidemic_peak_day = day + 1  # Adjusting for 0-based indexing
    
    # Calculamos los porcentajes
    healthy_percentage = (gente_sana / poblacion) * 100
    infected_percentage = (infectados / poblacion) * 100
    
    return healthy_percentage, infected_percentage, susceptible_list, infected_list, death_list, epidemic_peak_day, epidemic_peak_infected

# Parametros que utilizamos
total_population = int(input("cuánta población inicial tenemos?"))
initial_infected_percentage = float(input("cuánto porcentaje inicial de gente infectada hay?"))  
transmission_rate = float(input("cuánto porcentaje de transmisión tiene el virus?"))  
recovery_rate = float(input("cuánto porcentaje de gente se recupera?"))  
contacts_per_day = int(input("cuántos contactos por día hay?"))
simulation_days = int(input("cuántos días dura la epidemia?"))

# Con esto corremos todos los datos calculados
healthy_percent, infected_percent, susceptible, infected, deaths, epidemic_peak_day, epidemic_peak_infected = sir_model(
    total_population, 
    initial_infected_percentage * total_population / 100, 
    transmission_rate, 
    recovery_rate, 
    contacts_per_day, 
    simulation_days
)

# Utilizamos print para imprimir todos los datos.
print(f"Porcentaje de personas saludables: {healthy_percent:.2f}%")
print(f"Porcentaje de personas infectadas: {infected_percent:.2f}%")
print(f"Pico de la epidemia en el día {epidemic_peak_day}: {epidemic_peak_infected:.0f} personas infectadas")
print(f"Número total de muertes: {deaths[-1]:.0f}")

# Plotting los resultados
plt.figure(figsize=(10, 6))
plt.plot(susceptible, label='Susceptible')
plt.plot(infected, label='Infected')
plt.plot(deaths, label='Deaths', linestyle='dashed')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('SIR Model Simulation with Deaths')
plt.legend()
plt.show()
