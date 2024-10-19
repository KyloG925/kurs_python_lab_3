import json
import random
import os

# path postaci '/home/user/katalog/'

def readJSON(path: str):
    final_path = path + "Solution.json"
    if not os.path.exists(final_path):
        print("Plik nie istnieje")

    with open(final_path, 'r') as file:
        data = json.load(file)
        sumaA = 0
        for record in data:
            if record['Model'] == "A":
                sumaA += int(record['Czas'].rstrip('s'))
        print(f"Suma czasu dla modeli A: {sumaA}")


def writeJSON(path: str):
    final_path = path + "Solution.json"
    data_to_write = {
        "Model": f"{random.choice(["A", "B", "C"])}",
        "Wynik": f"{random.randint(0, 1000)}",
        "Czas": f"{random.randint(0, 1000)}s"
    }

    if not os.path.exists(final_path) or os.path.getsize(final_path) == 0:
        with open(final_path, 'w') as file:
            data = [data_to_write]
            json.dump(data, file)

    else:
        with open(final_path, 'r') as file:
            data = json.load(file)
            data.append(data_to_write)
            with open(final_path, 'w') as f:
                json.dump(data, f, indent=4)

