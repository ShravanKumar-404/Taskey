import subprocess

# with open('info.txt', 'w') as file:
#     info = subprocess.run("systeminfo", shell=True,
#                           stdout=file, text=True)

text = []
info = subprocess.run("systeminfo", shell=True,
                      capture_output=True, text=True).stdout
x = info.split('\n')
print(x)
