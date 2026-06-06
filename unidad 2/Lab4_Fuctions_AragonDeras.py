#Lab 4. Institutional
continuar = "si"
while continuar== "si":
    #variable declarations

    name = input("Ingresa tu nombre: ")
    lastname = input("Ingresa tu apellido: ")

    def generate_email(name, lastname):
        email = f"{name.lower()}.{lastname.lower()}@utd.edu.mx"
        return email

    #main program

    generated_email = generate_email(name, lastname)



    print("Your institutional email is: ", generated_email)
    continuar = input("\n¿Deseas capturar otro? (si/no): ")



def Calcular_tiempo(gb,mbps):
    segundos = (gb*8192)/mbps
    return segundos

ot = "si"

while ot == "si":
    try:
        tam = float(input("tamaño del archivo(GB: )"))
        velocidad = float(input("velocidad(Mbps): "))
        segundos_totales = Calcular_tiempo(tam, velocidad)
        print(f"Tiempo estimado: {segundos_totales:.2f} segundos.")

    except ValueError:
        print("Error: Ingresa solo numeros.")
        print("-"*30)
        ot = input("¿Desea calcular otro tiemo?(si/no):").lower()
