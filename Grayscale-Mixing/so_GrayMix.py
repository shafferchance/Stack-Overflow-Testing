from PIL import ImageColor, ImageTk, Image
import tkinter as tk
import colorsys as cs

def rgbToHls(image: Image):
    hlsImg = [[0]*(image.width) for _ in range(0, image.height)]
    for x in range(0, image.height):
        for y in range(0, image.width):
            pixelData = image.getpixel((x,y)) / 255
            hlsImg[x][y] = cs.rgb_to_hls(
                            pixelData[0],
                            pixelData[1],
                            pixelData[2])
    return hlsImg


def grayMixer(image):
    
    # Creating mixer window
    mixer = tk.Tk()
    mixer.title("Grayscale Mixer")
    mixer.geometry("250x400")

    # Creating sliders for values
    reds = tk.Scale(
                mixer, 
                from_ = 0, 
                to = 255, 
                orient = "horizontal",
                label = "Red")
    magentas = tk.Scale(
                mixer, 
                from_ = 0, 
                to = 255, 
                orient = "horizontal", 
                label = "Magenta")
    yellows = tk.Scale(
                mixer, 
                from_ = 0, 
                to = 255, 
                orient = "horizontal", 
                label = "Yellow")
    cyans = tk.Scale(
                mixer, 
                from_ = 0, 
                to = 255, 
                orient = "horizontal", 
                label = "Cyans")
    blues = tk.Scale(
                mixer, 
                from_ = 0, 
                to = 255, 
                orient = "horizontal", 
                label = "Blue")
    greens = tk.Scale(
                mixer, 
                from_ = 0, 
                to = 255, 
                orient="horizontal", 
                label = "Green")

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
    img.geometry("400x400")

    # Opening Image
    display = ImageTk.PhotoImage(Image.open(path))
    
    # Creating and adding toolbar
    tlbar = tk.Frame(
                img, 
                bg="black", 
                width="400", 
                height="100")
    scaleMixer = tk.Button(
                tlbar, 
                text="Grayscale Mixer",
                command=lambda img=display: grayMixer(img))
    # Lambda necessary to pass function without improper handling
    scaleMixer.pack(
                side="left", 
                padx=2, 
                pady=2)

    # Adding the image
    panel = tk.Label(tlbar, image = display)
    panel.pack(side="bottom", fill="none", expand=False)

    # Preparing final GUI and launching
    tlbar.pack(side="top")
    img.mainloop()

if __name__ == "__main__":
    main()