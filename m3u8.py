import tkinter as tk
import requests

# 创建GUI界面
root = tk.Tk()
root.title("M3U8检查器")

# 创建多行文本框
text = tk.Text(root, width=50, height=10)
text.pack()

# 创建检查按钮
def check_m3u8():
    lines = text.get("1.0", "end").splitlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        try:
            response = requests.get(line, timeout=5)
            if response.status_code == 200:
                text.tag_add("ok", f"{i+1}.0", f"{i+1}.end")
                text.tag_config("ok", foreground="green")
            else:
                text.tag_add("error", f"{i+1}.0", f"{i+1}.end")
                text.tag_config("error", foreground="red")
        except:
            text.tag_add("error", f"{i+1}.0", f"{i+1}.end")
            text.tag_config("error", foreground="red")

button_check = tk.Button(root, text="检查", command=check_m3u8)
button_check.pack()

# 创建清理按钮
def clean_text():
    text.tag_remove("error", "1.0", "end")

button_clean = tk.Button(root, text="清理", command=clean_text)
button_clean.pack()

# 运行GUI界面
root.mainloop()
