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

    @classmethod
    def del_angajat(cls, nume_angajat):

        cursor = Date_Angajati.find({'Nume': nume_angajat}, {'_id': 0})
        for i in cursor:
            for attr, value in i.items():
                if attr != "Data":
                    print(f"{attr}: {value}")
                else:
                    print(f"{attr}: {value.date()}")

        if input("Doriti sa eliminati angajatul din baza de date ?"
                 "\nAceasta actiune este ireversibila"
                 "\nY/N: ").upper() == "Y":

            Date_Angajati.delete_one({'Nume': nume_angajat})
        else:
            print("Schimbare neefectuata")

    @classmethod
    def update_salariu(cls, nume):
        salariu_actual = None
        cursor = Date_Angajati.find({'Nume': nume}, {'_id': 0, 'Salariu': 1})
        for i in cursor:
            salariu_actual = i["Salariu"]
        print(f"Salariul angajatului {nume} este: {salariu_actual}")
        if input("Doriti sa modificati salariul ?"
                 "Y/N: ").upper() == "Y":
            salariu_actual = Departament.float_input("Introduceti noul salariul: ")
            Date_Angajati.update_one({'Nume': nume}, {"$set": {"Salariu": salariu_actual}})
            print(f"Salariul angajtului {nume} este acum: {salariu_actual}")
        else:
            print("Schimbare neefectuata")

    @classmethod
    def update_nume(cls, nume):
        nume_actual = None
        cursor = Date_Angajati.find({'Nume': nume}, {'_id': 0, 'Nume': 1})
        for i in cursor:
            nume_actual = i["Nume"]
        print(f"Numele angajatului este: {nume_actual}")
        if input("Doriti sa modificati numele ?"
                 "Y/N: ").upper() == "Y":
            nume_actual = input("Introduceti noul nume: ")
            Date_Angajati.update_one({'Nume': nume}, {"$set": {"Nume": nume_actual}})
            print(f"Numele angajtului {nume} este acum: {nume_actual}")
        else:
            print("Schimbare neefectuata")

    @classmethod
    def update_job(cls, nume):
        job_actual = None
        cursor = Date_Angajati.find({'Nume': nume}, {'_id': 0, 'Pozitie': 1})
        for i in cursor:
            job_actual = i["Pozitie"]
        print(f"Jobul angajatului {nume} este: {job_actual}")
        if input("Doriti sa modificati jobul ?"
                 "Y/N: ").upper() == "Y":
            job_actual = input("Introduceti noul job: ")
            Date_Angajati.update_one({'Nume': nume}, {"$set": {"Pozitie": job_actual}})
            print(f"Jobul angajtului {nume} este acum: {job_actual}")
        else:
            print("Schimbare neefectuata")

    @classmethod
    def update_dep(cls, nume):
        dep_actual = None
        cursor = Date_Angajati.find({'Nume': nume}, {'_id': 0, 'Departament': 1})
        for i in cursor:
            dep_actual = i["Departament"]
        print(f"Departamentul angajatului {nume} este: {dep_actual}")
        if input("Doriti sa modificati departamentul ?"
                 "Y/N: ").upper() == "Y":
            dep_actual = Departament.alegere_dep()
            Date_Angajati.update_one({'Nume': nume}, {"$set": {"Departament": dep_actual}})
            print(f"Departamentul angajtului {nume} este acum: {dep_actual}")
            Angajat.update_job(nume)
        else:
            print("Schimbare neefectuata")
