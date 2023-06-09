import tkinter as tk
import ApiHandler

def create_input_window():
    def save_prompt():
        prompt = entry.get()
        send_prompt(prompt, 0.5, 100)
        input_window.destroy()
    def send_prompt(prompt, temperature, max_tokens):
        create_response_window(ApiHandler.gen_from_prompt(prompt, temperature, max_tokens))

    input_window = tk.Tk()

    label = tk.Label(input_window, text="Enter your prompt:")
    label.pack()

    entry = tk.Entry(input_window)
    entry.pack()

    button = tk.Button(input_window, text="Submit", command=save_prompt)
    button.pack()

    

    input_window.mainloop()

def create_response_window(response):
    if 'response_window' in globals():
        response_window.destroy()

    response_window = tk.Tk()

    label = tk.Label(response_window, text="Response:")
    label.pack()

    def display_text_one_by_one(text, index=0):
        if index < len(text):
            response_label.config(text=text[:index+1])
            index += 1
            response_label.after(100, lambda: display_text_one_by_one(text, index))


    response_label = tk.Label(response_window, text=response)
    response_label.pack()

    response_window.mainloop()

# Example usage:
# Create input window to save prompt
create_input_window()

# Simulating response received from some process
response = "This is the default response message."

# Create response window with the received response
create_response_window(response)
