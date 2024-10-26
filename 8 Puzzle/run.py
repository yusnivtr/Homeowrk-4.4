import os
import subprocess

# Đường dẫn tới thư mục chứa các script
folder_path = "/home/tiamo/Documents/code/Intro AI/8 Puzzle"

# Lấy danh sách tất cả các file .py trong thư mục
scripts = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".py")]

# Chạy tất cả các script cùng lúc
processes = [subprocess.Popen(["python", script]) for script in scripts]

# Đợi tất cả các script hoàn thành
for process in processes:
    process.wait()
