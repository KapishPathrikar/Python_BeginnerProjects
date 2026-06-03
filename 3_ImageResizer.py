import cv2
from tkinter import Tk, filedialog, simpledialog

root = Tk()
root.withdraw() #to hide the main window 

image_path = filedialog.askopenfilename(    #asking to select file path
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

image = cv2.imread(image_path) #reading the image

if image is None:   #to make sure image is selected
    print("No image selected or invalid image!")
    exit()

print(f"Original Size: {image.shape[1]} x {image.shape[0]}") #showing its original size

choice = simpledialog.askinteger(   #window popup for 1 or 2 choice
    "Resize Method",
    "Choose resize method:\n\n1 → Scale Percentage\n2 → Width & Height",
    minvalue=1,
    maxvalue=2
)

if choice is None:  #making sure choice is made
    print("Operation cancelled!")
    exit()

if choice == 1:
    scale = simpledialog.askinteger(
        "Scale Percentage",
        "Enter scale percentage (e.g., 50):"
    )

    if scale is None:
        exit()

    new_width = int(image.shape[1] * scale / 100)
    new_height = int(image.shape[0] * scale / 100)

elif choice == 2:
    new_width = simpledialog.askinteger(
        "Width",
        "Enter width:"
    )

    new_height = simpledialog.askinteger(
        "Height",
        "Enter height:"
    )

    if new_width is None or new_height is None:
        exit()

resized_image = cv2.resize(image, (new_width, new_height)) #resizing image

cv2.imshow("Resized Image", resized_image)   #showing image before saving

save_path = filedialog.asksaveasfilename(  #asking the file path ot save
    title="Save Resized Image",
    defaultextension=".jpg",
    filetypes=[
        ("JPEG files", "*.jpg"),
        ("PNG files", "*.png")
    ]
)

if save_path:   #saving it finally
    cv2.imwrite(save_path, resized_image)
    print("Image saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()     