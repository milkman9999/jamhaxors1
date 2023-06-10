import tkinter as tk
from openai import ChatCompletion

# Set your OpenAI API key
openai.api_key = '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'

# Create the main application window
window = tk.Tk()
window.title("OpenAI API Example")

# Create an input text box
input_text = tk.Text(window, height=10, width=50)
input_text.pack()

# Create an output text box
output_text = tk.Text(window, height=10, width=50)
output_text.pack()

# Define a function to process the input and generate the output
def generate_output():
    # Get the user input from the input text box
    user_input = input_text.get("1.0", tk.END)

    # Make an API call to OpenAI to get the model's response
    response = ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    # Extract the assistant's reply from the API response
    assistant_reply = response['choices'][0]['message']['content']

    # Display the assistant's reply in the output text box
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, assistant_reply)

# Create a button to generate the output
generate_button = tk.Button(window, text="Generate", command=generate_output)
generate_button.pack()

# Start the main event loop
window.mainloop()
