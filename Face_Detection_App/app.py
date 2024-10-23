# Import required libraries
import cv2 # type: ignore
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Function to load an image and detect faces
def detect_faces():
    # Load image using file dialog
    file_path = filedialog.askopenfilename(title = 'Select an Image',
                                           filetypes = [("Image Files","*.jpg *.jpeg *.png")])
    if not file_path:
        messagebox.showwarning("Warning", "No file selected.")
        return
    
    try:
        # Load pre-trained classifier for face detection
        face_cascade = cv2.CascadeClassifier('face_detector.xml')

        # Read the selected image
        img = cv2.imread(file_path)

        if img is None:
            messagebox.showerror("Error", "Invalid image format or corrput file.")
            return

        # Detecting faces in the image
        faces = face_cascade.detectMultiScale(img, scaleFactor = 1.1, minNeighbors = 4)

        if len(faces) == 0:
            messagebox.showinfo("Result", "No faces detected in the image.")
        else:
            # Annotating bounding boxes around images detected
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        
        # Create output folder if doesn't exist
        output_dir = './output'
        os.makedirs(output_dir, exist_ok = True)

        # Save the images with face detection annotations
        output_path = os.path.join(output_dir, os.path.basename(file_path))
        cv2.imwrite(output_path, img)

        # Display success message with saved file path
        messagebox.showinfo("Success", f"Face Detection Completed!!! Image saved to {output_path}")

        # Update the displayed image in the UI
        display_image(output_path)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to display image in the UI
def display_image(img_path):
    # Open the image and resize it to fit to background area
    img = Image.open(img_path)
    img = img.resize((400,400), Image.Resampling.LANCZOS)  # Resize to fit to UI

    # Convert the image to ImageTk format
    img = ImageTk.PhotoImage(img)

    # Update the background label with the new image
    background_label.config(image = img)
    background_label.image = img  # Keep a reference of the image to avoid garbage collection

# Function to create UI for the application
def create_ui():
    root = tk.Tk()
    root.title("Face Detection App")

    # Set dimensions of the window
    window_width = 400
    window_height = 500

    # Get the UI screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates to center the UI dialog window
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set geometry of the window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Load and set the background image
    bg_img = Image.open('./background_image.jpg')
    bg_img = bg_img.resize((400,400), Image.Resampling.LANCZOS)
    bg_img = ImageTk.PhotoImage(bg_img)

    # Create label to display background image
    global background_label
    background_label = tk.Label(root, image = bg_img)
    background_label.image = bg_img  # Keep a reference to avoid garbage collection
    background_label.pack()

    # Create a button for loading an image
    load_button = tk.Button(root, text = "Select Image & Detect Faces", command = detect_faces, width = 30, font = ('Ariel',14))
    load_button.pack(side = "bottom", pady = 20)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_ui()
