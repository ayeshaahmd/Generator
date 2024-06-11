import os
import customtkinter as ctk
# Import the actual Google Gemini API SDK (this is a hypothetical import, adjust according to the actual SDK)
import google.generativeai as genai

def generate():
    # Construct prompt based on user input
    prompt = "Please generate 10 ideas for coding projects. "
    language = languageDropdown.get()
    prompt += "The programming language is " + language + '. '
    difficulty = difficulty_value.get()
    prompt += 'The difficulty is ' + difficulty + '. '
    if checkbox1.get():
        prompt += "The project should include a database. "
    if checkbox2.get():
        prompt += "The project should include an API. "
    
    # Print prompt for debugging
    print(prompt)
  
    # Set up Google Gemini API key
    gemini_api_key = os.getenv('GOOGLE_API_KEY')  # Ensure you have set the API key in your environment variables
    gemini_api_key='AIzaSyBsnSuXo37uFnEmAMYC6ObKH70VLoeI8w4'
    # Initialize Gemini client
    genai.configure(api_key=gemini_api_key)  # Hypothetical initialization, replace with actual method
    
    # Initialize the GenerativeModel (adjust according to the actual SDK)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Generate project ideas using Google Gemini's API (hypothetical method, replace with actual API call)
    response = model.generate_content(prompt)  # Hypothetical method, replace with actual API call
    ideas = response.text  # Hypothetical response parsing, replace with actual parsing logic
    
    # Display generated ideas in the result textbox
    result.delete('1.0', ctk.END)
    result.insert('1.0', ideas)

# Create the main application window
root = ctk.CTk()
root.state('zoomed')  # Maximize window
root.title("Project Idea Generator with Google Gemini")
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode('dark')
root.configure(fg_color='black')

# Create and pack the title label
title_label = ctk.CTkLabel(root, text="Project Idea Generator", font=ctk.CTkFont(size=30, weight='bold'))
title_label.pack(pady=(20, 20))

# Create and pack the frame
frame = ctk.CTkFrame(root)
frame.pack(fill='both', expand=True, padx=100, pady=20)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Create and pack the language selection dropdown
languageFrame = ctk.CTkFrame(frame)
languageFrame.grid(row=0, column=0, pady=20)
language_label = ctk.CTkLabel(languageFrame, text='Programming Language', font=ctk.CTkFont(weight='bold'))
language_label.pack()
languageDropdown = ctk.CTkComboBox(languageFrame, values=['Python', 'Java', 'C++', 'C#'])
languageDropdown.pack(pady=10)

# Create and pack the difficulty selection radiobuttons
difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.grid(row=1, column=0, pady=20)
difficulty_label = ctk.CTkLabel(difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight='bold'))
difficulty_label.pack()
difficulty_value = ctk.StringVar(value='Easy')
radiobutton1 = ctk.CTkRadioButton(difficulty_frame, text='Easy', variable=difficulty_value, value='Easy')
radiobutton1.pack(side='left', padx=(20,10), pady=10)
radiobutton2 = ctk.CTkRadioButton(difficulty_frame, text='Medium', variable=difficulty_value, value='Medium')
radiobutton2.pack(side='left', padx=10, pady=10)
radiobutton3 = ctk.CTkRadioButton(difficulty_frame, text='Hard', variable=difficulty_value, value='Hard')
radiobutton3.pack(side='left', padx=10, pady=10)

# Create and pack the feature selection checkboxes
feature_frame = ctk.CTkFrame(frame)
feature_frame.grid(row=2, column=0, pady=20)
feature_label = ctk.CTkLabel(feature_frame, text='Feature', font=ctk.CTkFont(weight='bold'))
feature_label.pack()
checkbox1 = ctk.CTkCheckBox(feature_frame, text='Database')
checkbox1.pack(side='left', padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(feature_frame, text='API')
checkbox2.pack(side='left', padx=50, pady=10)

# Create and pack the generate button
button = ctk.CTkButton(frame, text='Generate Idea', command=generate)
button.grid(row=3, column=0, pady=(5,20))

# Customize and create the CTkTextbox
result = ctk.CTkTextbox(
    root,
    font=ctk.CTkFont(size=15),
    border_color="gray",
    border_width=2,
    corner_radius=10,
    fg_color="black",  # foreground color (text color)
    bg_color="white"  # background color
)

# Pack the CTkTextbox with options to fill the space
result.pack(pady=20, padx=100, fill='both', expand=True)

# Run the application
root.mainloop()
