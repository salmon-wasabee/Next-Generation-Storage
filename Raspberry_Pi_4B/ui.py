import tkinter as tk

def create_ui(ser, move_forward, move_backward, status_label_text_var):
    root = tk.Tk()
    root.title("Stepper Motor Controller")

    # Create and place widgets
    steps_label = tk.Label(root, text="Control:")
    steps_label.grid(row=0, column=0)

    forward_button = tk.Button(root, text="Forward", command=lambda: move_forward(ser, status_label_text_var))
    forward_button.grid(row=1, column=0)

    backward_button = tk.Button(root, text="Backward", command=lambda: move_backward(ser, status_label_text_var))
    backward_button.grid(row=1, column=1)

    status_label = tk.Label(root, textvariable=status_label_text_var)
    status_label.grid(row=2, columnspan=2)

    return root
