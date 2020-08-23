class Formato:
    @staticmethod
    def formato (nombre):
        return nombre[0].upper() + nombre[1:].lower()

print(Formato.formato("gUmBaLl"))