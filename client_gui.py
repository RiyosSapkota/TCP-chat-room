import tkinter as tk

wwi= tk.Tk()
wwi.title("Client Chat")

chat_box = tk.Text(wwi)
chat_box.pack(expand = True, fill= tk.BOTH)

message_input = tk.Entry(wwi)
message_input.pack(side=tk.LEFT, expand=True, fill=tk.X)
message_input.bind("<Return>")

send_button = tk.Button(wwi, text="Send", )
send_button.pack(side=tk.RIGHT)

wwi.mainloop()