import os
import customtkinter as ctk
import google.generativeai as genai


def initialize_application_window():
    """
    Initialize the main application window with title, size, and theme.
    """
    root = ctk.CTk()
    root.geometry("750x550")
    root.title("Project Idea Generator with Google Gemini")
    ctk.set_default_color_theme("blue")
    ctk.set_appearance_mode('dark')
    root.configure(fg_color='black')
    return root

def display_title_and_frame(root):
    """
    Display the title label and set up the frame for organizing widgets.
    """
    title_label = ctk.CTkLabel(root, text="Project Idea Generator", font=ctk.CTkFont(size=30, weight='bold'))
    title_label.pack(padx=10, pady=(40,20))
    frame = ctk.CTkFrame(root)
    frame.pack(fill='x', padx=100)
    return frame

def collect_user_inputs(frame):
    """
    Collect user inputs including programming language, difficulty level, and additional features.
    """
    languageFrame = ctk.CTkFrame(frame)
    languageFrame.pack(padx=100, pady=(20,5), fill='both')
    language_label = ctk.CTkLabel(languageFrame, text='Programming Language', font=ctk.CTkFont(weight='bold'))
    language_label.pack()
    languageDropdown = ctk.CTkComboBox(languageFrame, values=['Python', 'Java', 'C++', 'C#'])
    languageDropdown.pack(pady=10)

    difficulty_frame = ctk.CTkFrame(frame)
    difficulty_frame.pack(padx=100, pady=5, fill='both')
    difficulty_label = ctk.CTkLabel(difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight='bold'))
    difficulty_label.pack()
    difficulty_value = ctk.StringVar(value='Easy')
    radiobutton1 = ctk.CTkRadioButton(difficulty_frame, text='Easy', variable=difficulty_value, value='Easy')
    radiobutton1.pack(side='left', padx=(20,10), pady=10)
    radiobutton2 = ctk.CTkRadioButton(difficulty_frame, text='Medium', variable=difficulty_value, value='Medium')
    radiobutton2.pack(side='left', padx=10, pady=10)
    radiobutton3 = ctk.CTkRadioButton(difficulty_frame, text='Hard', variable=difficulty_value, value='Hard')
    radiobutton3.pack(side='left', padx=10, pady=10)

    feature_frame = ctk.CTkFrame(frame)
    feature_frame.pack(padx=100, pady=5, fill='both')
    feature_label = ctk.CTkLabel(feature_frame, text='Feature', font=ctk.CTkFont(weight='bold'))
    feature_label.pack()
    checkbox1 = ctk.CTkCheckBox(feature_frame, text='Database')
    checkbox1.pack(side='left', padx=50, pady=10)
    checkbox2 = ctk.CTkCheckBox(feature_frame, text='API')
    checkbox2.pack(side='left', padx=50, pady=10)

    return languageDropdown, difficulty_value, checkbox1, checkbox2

def generate_ideas(languageDropdown, difficulty_value, checkbox1, checkbox2):
    """
    Generate project ideas based on user inputs using Google Gemini API.
    """
    prompt = "Please generate 10 ideas for coding projects. "
    language = languageDropdown.get()
    prompt += "The programming language is " + language + '. '
    difficulty = difficulty_value.get()
    prompt += 'The difficulty is ' + difficulty + '. '
    if checkbox1.get():
        prompt += "The project should include a database. "
    if checkbox2.get():
        prompt += "The project should include an API. "
    
    gemini_api_key = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    ideas = response.text
    return ideas

def display_generated_ideas(ideas, root):
    """
    Display the generated project ideas in the result textbox.
    """
    result = ctk.CTkTextbox(
        root,
        font=ctk.CTkFont(size=15),
        border_color="gray",
        border_width=2,
        corner_radius=10,
        fg_color="black",
        bg_color="white"
    )
    result.pack(pady=20, padx=100, fill='both', expand=True)
    result.insert('0.0', ideas)

    

