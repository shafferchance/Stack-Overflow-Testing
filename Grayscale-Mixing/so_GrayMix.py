from PIL import ImageColor, ImageTk, Image
import tkinter as tk

def grayMixer(image: ImageTk.Image):
    # Color variables

    # Creating mixer window
    mixer = tk.Tk()
    mixer.title("Grayscale Mixer")
    mixer.geometry("250x250")

    # Creating sliders for values
    reds = tk.Scale(mixer)

def main():
    # Declaring image path
    path = "lavee.jpg"

    # Creating and configuring window
    img = tk.Tk()
    img.title("Example")
    img.geometry("1024x720")
    
    # Creating and adding toolbar
    tlbar = tk.Frame(img, bg="black", width="1024", height="100")
    scaleMixer = tk.Button(tlbar, text="Grayscale Mixer",command="")
    scaleMixer.pack(side="left", padx=2, pady=2)

    # Creating and adding the image
    display = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(tlbar, image = display)
    panel.pack(side="bottom", fill="none", expand=False)

    # Preparing final GUI and launching
    tlbar.pack(side="top")
    img.mainloop()

if __name__ == "__main__":
    main()