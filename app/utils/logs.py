import os
import json
from tabulate import tabulate

def resumen_logs(n: int = 10):
    carpeta = "logs/articulos"
    if not os.path.exists(carpeta):
        print("⚠️ No hay artículos procesados todavía.")
        return

    files = sorted(os.listdir(carpeta), reverse=True)
    data = []

    for file in files[:n]:
        path = os.path.join(carpeta, file)
        with open(path, encoding="utf-8") as f:
            art = json.load(f)
            data.append([
                art.get("titulo", "Sin título"),
                art.get("fecha", ""),
                art.get("autor", ""),
                "🟢" if art.get("resumen") else "❌",
                len(art.get("texto", "")),
                ", ".join(art.get("categorias", {}).keys())
            ])

    print(tabulate(data, headers=["Título", "Fecha", "Autor", "Resumen", "Longitud", "Categorías"]))
