import subprocess

# Thực hiện lệnh command
result = subprocess.run("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# In kết quả
print("Exit code:", result.returncode)
print("Standard output:")
print(result.stdout)
print("Standard error:")
print(result.stderr)