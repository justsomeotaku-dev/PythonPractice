import tkinter as tk
import ctypes

WS_EX_LAYERED = 0x80000
WS_EX_TRANSPARENT = 0x20

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.8)
root.configure(bg="black")
root.attributes("-topmost", True)

root.update()

hwnd = ctypes.windll.user32.GetParent(root.winfo_id())

style = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
style |= WS_EX_LAYERED | WS_EX_TRANSPARENT
ctypes.windll.user32.SetWindowLongW(hwnd, -20, style)

root.mainloop()