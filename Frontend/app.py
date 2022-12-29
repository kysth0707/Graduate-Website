import os

Link = os.getcwd()
# Link = 'E:\\GithubProjects\\Graduate-Website\\Frontend\\'
os.system(f"cd {Link}")
print(Link)
os.system('python -m http.server 2023')