from departament import *


class Angajat(Departament):

    def __init__(self, workdep: str, empname: str, job: str, hiredate: datetime, salary: float):
        """ Constructorul clasei Angajat. """
        super().__init__(workdep)
        self.empname = empname
        self.job = job
        self.hiredate = hiredate
        self.__salary = salary

    def add_angajat(self) -> None:
        angajat_nou = {
            "Departament": self.workdep,
            "Nume": self.empname,
            "Position": self.job,
            "Data": self.hiredate,
            "Salariu": self.__salary
        }
        Date_Angajati.insert_one(angajat_nou)


