import subprocess, sys

# subprocess.run(["clear"])

# resultado = subprocess.run(["ping", "-c", "1", "8.8.8.8"], text=True, capture_output=True)

# if resultado.returncode == 0:
#     print("Ha funcionado bien")
# else:
#     print("Ha funcionado mal")






resultado = subprocess.run(["date"], text=True, capture_output=True)
if resultado.returncode != 0:
    print("ha habido un problemon mi hermano")
    sys.exit(1)
    
# texto_date = resultado.stdout.strip()

# print(f"Lo que se ha capturado es: {texto_date}")

año = resultado.stdout.strip().split(" ")[4]
print(año)