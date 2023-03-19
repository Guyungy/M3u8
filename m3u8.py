import tkinter as tk
import requests


class M3U8Checker:
    def __init__(self, master):
        self.master = master
        master.title("M3U8链接检查器")

        # 待检测的 M3U8 链接输入框
        self.m3u8_input_label = tk.Label(master, text="待检测的 M3U8 链接：")
        self.m3u8_input_label.grid(row=0, column=0, sticky=tk.W)
        self.m3u8_input_text = tk.Text(master, height=10)
        self.m3u8_input_text.grid(row=1, column=0, padx=10, pady=10)

        # 有效的 M3U8 链接列表框
        self.valid_m3u8_label = tk.Label(master, text="有效的 M3U8 链接：")
        self.valid_m3u8_label.grid(row=2, column=0, sticky=tk.W)
        self.valid_m3u8_listbox = tk.Listbox(master, height=10)
        self.valid_m3u8_listbox.grid(row=3, column=0, padx=10, pady=10)

        # 无效的 M3U8 链接列表框
        self.invalid_m3u8_label = tk.Label(master, text="无效的 M3U8 链接：")
        self.invalid_m3u8_label.grid(row=4, column=0, sticky=tk.W)
        self.invalid_m3u8_listbox = tk.Listbox(master, height=10)
        self.invalid_m3u8_listbox.grid(row=5, column=0, padx=10, pady=10)

        # 检查按钮
        self.check_button = tk.Button(master, text="检查", command=self.check_m3u8)
        self.check_button.grid(row=6, column=0, padx=10, pady=10)

    def check_m3u8(self):
        m3u8_str = self.m3u8_input_text.get("1.0", tk.END)
        m3u8_lines = m3u8_str.strip().split('\n')
        for m3u8_url in m3u8_lines:
            m3u8_url = m3u8_url.strip()
            try:
                response = requests.get(m3u8_url, timeout=5)
                if response.status_code == 200:
                    self.valid_m3u8_listbox.insert(tk.END, m3u8_url)
                else:
                    self.invalid_m3u8_listbox.insert(tk.END, m3u8_url)
            except:
                self.invalid_m3u8_listbox.insert(tk.END, m3u8_url)


root = tk.Tk()
m3u8_checker = M3U8Checker(root)
root.mainloop()
