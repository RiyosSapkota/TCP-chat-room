import socket
import threading
import tkinter as tk

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                chat_box.insert(tk.END, message + '\n')
        except:
            print("An error occurred")
            client.close()
            break

def write(event=None):
    message = message_input.get()
    message_input.delete(0, tk.END)
    client.send(f'{nickname}: {message}'.encode('ascii'))

def on_closing(event=None):
    write()
    client.close()
    window.quit()

nickname = input("Choose a nickname:")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 14628))

window = tk.Tk()
window.title("Chat Client")

chat_box = tk.Text(window)
chat_box.pack(expand=True, fill=tk.BOTH)

message_input = tk.Entry(window)
message_input.pack(side=tk.LEFT, expand=True, fill=tk.X)
message_input.bind("<Return>", write)

send_button = tk.Button(window, text="Send", command=write)
send_button.pack(side=tk.RIGHT)

window.protocol("WM_DELETE_WINDOW", on_closing)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

window.mainloop()
