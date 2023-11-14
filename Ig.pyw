# Importar los módulos necesarios
import instaloader
import tkinter as tk
from tkinter import messagebox
import os

# Crear una instancia de Instaloader
loader = instaloader.Instaloader()

# Crear una función que descargue el reel
def descargar_reel():
  # Obtener el link del post desde el campo de texto
  link = entry.get()
  # Verificar que el link sea válido
  if link.startswith(""):
    # Obtener el shortcode del post
    shortcode = link.split("/")[-2]
    # Obtener el objeto Post
    post = instaloader.Post.from_shortcode(loader.context, shortcode)
    # Verificar que el post sea un reel
    if post.is_video and post.video_duration < 60:
      # Descargar el post
      try:
        loader.download_post(post, target="Descargas")
        # Eliminar los archivos que no sean .mp4
        for file in os.listdir("Descargas"):
          if not file.endswith(".mp4"):
            os.remove("Descargas/" + file)
        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "Reel descargado exitosamente.")
      except Exception as e:
        # Mostrar un mensaje de error
        messagebox.showerror("Error", f"Ocurrió un error al descargar el reel: {e}")
    else:
      # Mostrar un mensaje de advertencia
      messagebox.showwarning("Advertencia", "El post no es un reel válido.")
  else:
    # Mostrar un mensaje de advertencia
    messagebox.showwarning("Advertencia", "El link no es válido.")

# Crear una ventana
window = tk.Tk()
window.title("Akame Downloader")
window.resizable(0, 0)
window.iconbitmap("Akame.ico")
window.geometry("650x350")
window.config(bg="pink")

# Crear una etiqueta con instrucciones y centrarla
label = tk.Label(window, text="Ingresa el link del post de Instagram que contiene el reel:")
label.config(fg="pink", bg="black", font=("Arial", 16, "bold"))
label.grid(row=0, column=0, columnspan=2, padx=40, pady=10)

# Crear un campo de texto para ingresar el link y centrarlo
entry = tk.Entry(window)
entry.config(fg="pink", bg="black", font=("Arial", 10, "bold"))
entry.grid(row=1, column=0, columnspan=2, padx=25, pady=5)

# Crear un botón para descargar el reel y centrarlo
button = tk.Button(window, text="Descargar", command=descargar_reel)
button.config(fg="pink", bg="black", font=("Arial", 16, "bold"))
button.grid(row=2, column=0, columnspan=2, padx=25, pady=10)

# Iniciar el bucle principal de la ventana
window.mainloop()


# Comentario Prueba