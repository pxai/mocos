class Alumno:
    def __init__ (self, nombre):
        self._nombre = nombre

class Aula:
    def __init__ (self):
        self._alumnos = []
    
    def meteAlumno (self, alumno):
        self._alumnos.append(alumno)

    def pasarLista (self):
        for alumno in self._alumnos:
            print(alumno._nombre)

alumno1 = Alumno("Gumball")
alumno2 = Alumno("Darwin")

aula = Aula()

aula.meteAlumno(alumno1)
aula.meteAlumno(alumno2)
aula.pasarLista()