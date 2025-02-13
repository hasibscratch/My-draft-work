@@ -0,0 +1,22 @@
import tkinter as tk
from time import strftime
# Function to update the clock display
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Format the time (24-hour format with AM/PM)
    label.config(text=current_time)         # Update the label text with the current time
    label.after(1000, update_time)          # Call this function again after 1000ms (1 second)
# Create the main window
root = tk.Tk()
root.title("Clock by Hasib") 
# Customize the clock appearance
label = tk.Label(root, font=('Times New Roman', 30, 'bold'), foreground='red') 
label.pack(anchor='center')
# Start the clock
update_time()
# Run the application
root.mainloop()
