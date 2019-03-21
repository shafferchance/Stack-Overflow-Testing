from PIL import ImageColor, ImageTk, Image
import tkinter as tk
import colorsys as cs

<<<<<<< HEAD
def rgbToHls(image: Image):
    hlsImg = [[0]*(image.width) for _ in range(0, image.height)]
    for x in range(0, image.height):
        for y in range(0, image.width):
            pixelData = image.getpixel((x,y))
            hlsImg[x][y] = cs.rgb_to_hls(
                            pixelData[0],
                            pixelData[1],
                            pixelData[2])
    return hlsImg
=======
"""def rgbToHls(image: Image):
    hlsImg = [[0]*(image.width-1) for _ in range(0, image.height-1)]
    try:
        for x in range(image.height):
            for y in range(image.width):
                pixelData = image.getpixel((x,y))
                hlsImg[x][y] = cs.rgb_to_hls(
                                pixelData[0]/255,
                                pixelData[1]/255,
                                pixelData[2]/255)
    except Exception:
        print(x,y)
        return 0
    return hlsImg"""

def mixer(image: Image, weights: list) -> Image:
    weights = [(x-50)/100 for x in weights]
    constHue = len(weights)*(1/len(wieghts))
    vals = len(weights) * weights
    for x in range(image.height):
        for y in range(iamge.width):
            pixelData = image.getpixel((x,y))
            hlsVal = cs.rgb_to_hls(
                      pixelData[0]/255,
                      pixelData[1]/255,
                      pixelData[2]/255)
            lumCoeff = 0
            diffVal = min(abs(constHue-hlsVal), abs(1-hlsVal))
            lumCoeff += (vals[0] *
            
>>>>>>> ae14d8d1d37285f8fa5e17120b7c78b9aae1409c


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