from PIL import ImageColor, ImageTk, Image
import tkinter as tk

def grayMixer():
    # Color  = 0
    magenta = 0
    yellow = 0
    cyan = 0
    blue = 0
    green = 0

    # Creating mixer window
    mixer = tk.Tk()
    mixer.title("Grayscale Mixer")
    mixer.geometry("250x250")

    # Creating sliders for values
    reds = tk.Scale(mixer, from_ = 0, to = 255, orient = "horizontal", label = "Red")
    magentas = tk.Scale(mixer, from_ = 0, to = 255, orient = "horizontal", label = "Magenta")
    yellows = tk.Scale(mixer, from_ = 0, to = 255, orient = "horizontal", label = "Yellow")
    cyans = tk.Scale(mixer, from_ = 0, to = 255, orient = "horizontal", label = "Cyans")
    blues = tk.Scale(mixer, from_ = 0, to = 255, orient = "horizontal", label = "Blue")
    greens = tk.Scale(mixer, from_ = 0, to = 255, orient="horizontal", label = "Green")

    # Adding sliders
    reds.pack()
    magentas.pack()
    yellows.pack()
    cyans.pack()
    blues.pack()
    greens.pack()

    # Preparing final GUI and launch
    mixer.mainloop()

def main():
    # Declaring image path
    path = "lavee.jpg"

    # Creating and configuring window
    img = tk.Tk()
    img.title("Example")
    img.geometry("1024x720")
    
    # Creating and adding toolbar
    tlbar = tk.Frame(img, bg="black", width="1024", height="100")
    scaleMixer = tk.Button(tlbar, text="Grayscale Mixer",command=grayMixer)
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