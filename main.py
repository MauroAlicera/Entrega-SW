import customtkinter as ctk
import openai

# Configura tu clave API de OpenAI
openai.api_key = "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"

def obtener_respuesta_chatgpt(tipo_problema, variables):
    # Solicitud a la API de OpenAI
    prompt = f"En base al tipo de problema '{tipo_problema}' y sus respectivas variables '{variables}', impleméntame una solución para ese problema."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def abrir_nueva_interfaz(entrada1_valor, entrada2_valor):
    # Destruir la ventana actual
    root.destroy()

    # Crear una nueva ventana con la misma configuración
    nueva_ventana = ctk.CTk()
    nueva_ventana.geometry("800x600")
    
    # Configuración de apariencia y tema para la nueva ventana
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # Configurar el contenido de la nueva ventana
    nueva_frame = ctk.CTkFrame(master=nueva_ventana)
    nueva_frame.pack(pady=40, padx=80, fill="both", expand=True)
    
    nueva_label = ctk.CTkLabel(master=nueva_frame, text="Creación de las funciones específicas para caso 1", font=("Roboto", 28))
    nueva_label.pack(pady=20, padx=20)
    
    entrada1_mostrada = ctk.CTkLabel(master=nueva_frame, text=f"Tipo de Problema: {entrada1_valor}")
    entrada1_mostrada.pack(pady=10, padx=10)
    
    entrada2_mostrada = ctk.CTkLabel(master=nueva_frame, text=f"Variables: {entrada2_valor}")
    entrada2_mostrada.pack(pady=10, padx=10)
    
    # Cuadro de texto grande para mostrar la respuesta de la API
    cuadro_texto = ctk.CTkTextbox(master=nueva_frame, width=400, height=200)
    cuadro_texto.pack(pady=20, padx=20)
    
    # Obtener la respuesta de la API y mostrarla en el cuadro de texto
    respuesta = obtener_respuesta_chatgpt(entrada1_valor, entrada2_valor)
    cuadro_texto.insert("1.0", respuesta)
    
    nueva_button = ctk.CTkButton(master=nueva_frame, text="Regresar", width=200, command=nueva_ventana.destroy)
    nueva_button.pack(pady=20, padx=20)
    
    nueva_ventana.mainloop()

def manejar_continuar():
    entrada1_valor = entrada1.get()
    entrada2_valor = entrada2.get()
    abrir_nueva_interfaz(entrada1_valor, entrada2_valor)

# Configuración de apariencia y tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Creación de la ventana principal
root = ctk.CTk()
root.geometry("800x600")

# Creación del marco (frame)
frame = ctk.CTkFrame(master=root)
frame.pack(pady=40, padx=80, fill="both", expand=True)

# Creación de la etiqueta (label)
label = ctk.CTkLabel(master=frame, text="Generador automático de algoritmos de optimización", font=("Roboto", 24))
label.pack(pady=20, padx=20)

# Creación de las entradas (entry)
entrada1 = ctk.CTkEntry(master=frame, placeholder_text="Tipo de Problema", width=300)
entrada1.pack(pady=20, padx=20)

entrada2 = ctk.CTkEntry(master=frame, placeholder_text="Define las variables necesarias para el problema", width=300)
entrada2.pack(pady=20, padx=20)

# Creación del botón (button)
button = ctk.CTkButton(master=frame, text="Continuar", width=200, command=manejar_continuar)
button.pack(pady=20, padx=20)

# Inicio del bucle principal de la interfaz
root.mainloop()
