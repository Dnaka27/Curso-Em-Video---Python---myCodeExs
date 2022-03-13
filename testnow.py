print("-" * 30)
print("Excluindo arquivos")
import os
try:
    os.remove("CursoEmVideo.txt")
except OSError as e:
    print(f"Error: {e.strerror}")
else:
    print("Arquivo excluido com sucesso")