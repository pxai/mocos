def saludo (momento):
    if  momento == "mañana": return "Buenos días"
    elif momento == "tarde": return "Buenas tardes"
    elif momento == "noche": return "Buenas noches"
    else: return ""

print(saludo("tarde"))

def saludo2 (momento):
    return {
        "mañana": "Buenos Días",
        "tarde": "Buenas tardes",
        "noche":"Buenas noches"
    }[momento]

print(saludo2("tarde"))
