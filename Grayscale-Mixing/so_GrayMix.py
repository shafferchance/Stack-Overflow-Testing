from PIL import ImageTk, Image
import tkinter as tk

def main():
    # Declaring image path
    path = "lavee.jpg"

    # Creating and adding elements to widget
    wigdet = tk.Tk()
    wigdet.title("Graymix")
    wigdet.geometry("1024x720")
    display = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(wigdet, image = display)

    # Preparing final GUI and launching
    panel.pack(side="bottom", fill="none",expand=False)
    wigdet.mainloop()

if __name__ == "__main__":
    main()