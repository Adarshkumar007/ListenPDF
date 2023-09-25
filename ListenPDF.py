import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import filedialog

# Function to read PDF aloud
def read_pdf():
    # Get the selected PDF file from the user
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    if not file_path:
        return

    # Open the PDF file in binary read mode
    pdf_book = open(file_path, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_book)

    # Initialize the text-to-speech engine
    pdf_speaker = pyttsx3.init()

    # Read each page in the PDF
    for page in pdf_reader.pages:
        # Extract text from the page
        pdf_text = page.extract_text()

        # Say the extracted text
        pdf_speaker.say(pdf_text)
        pdf_speaker.runAndWait()

# Function to exit the application
def exit_app():
    app.quit()

# Create the main application window
app = tk.Tk()
app.title("PDF Reader")

# Configure colors
app.configure(bg='#F0F0F0')  # Background color

# Create a button to select and read the PDF with custom colors
read_button = tk.Button(app, text="Select PDF and Read", command=read_pdf, bg='#4CAF50', fg='white')
read_button.pack(pady=20)

# Create an "Exit" button to close the application
exit_button = tk.Button(app, text="Exit", command=exit_app, bg='red', fg='white')
exit_button.pack(pady=10)

# Run the application
app.mainloop()
