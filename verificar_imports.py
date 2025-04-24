import os
import ast

PROYECTO_ROOT = "app"  # ajusta si tu carpeta principal cambia

def verificar_imports(carpeta_base):
    errores = []

    for root, _, files in os.walk(carpeta_base):
        for archivo in files:
            if archivo.endswith(".py"):
                path = os.path.join(root, archivo)
                with open(path, "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read(), filename=archivo)
                    except Exception as e:
                        errores.append(f"⚠️ Error de sintaxis en {path}: {e}")
                        continue

                    for node in ast.walk(tree):
                        if isinstance(node, ast.ImportFrom):
                            modulo = node.module
                            if modulo and modulo.startswith("app."):
                                ruta_relativa = modulo.replace(".", "/") + ".py"
                                ruta_completa = os.path.join(PROYECTO_ROOT, *modulo.split(".")[1:]) + ".py"
                                if not os.path.isfile(ruta_completa):
                                    errores.append(f"❌ FALTA: {modulo} (importado en {path})")

    return errores


# Ejecutar revisión
if __name__ == "__main__":
    faltantes = verificar_imports(PROYECTO_ROOT)
    if faltantes:
        print("\n".join(faltantes))
    else:
        print("✅ Todo en orden. No faltan archivos importados.")
