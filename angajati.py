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
        if Date_Angajati.count_documents({'Nume': nume_angajat}) > 0:
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
        else:
            print(f"Angajatul {nume_angajat} nu a fost gasit.")

    @classmethod
    def update_salariu(cls, nume_angajat):
        salariu_actual = None
        cursor = Date_Angajati.find({'Nume': nume_angajat}, {'_id': 0, 'Salariu': 1})
        for i in cursor:
            salariu_actual = i["Salariu"]
        if Date_Angajati.count_documents({'Nume': nume_angajat}) > 0:
            print(f"Salariul angajatului {nume_angajat} este: {salariu_actual}")
            if input("Doriti sa modificati salariul ?"
                     "Y/N: ").upper() == "Y":
                salariu_actual = Departament.float_input("Introduceti noul salariul: ")
                Date_Angajati.update_one({'Nume': nume_angajat}, {"$set": {"Salariu": salariu_actual}})
                print(f"Salariul angajtului {nume_angajat} este acum: {salariu_actual}")
            else:
                print("Schimbare neefectuata")
        else:
            print(f"Angajatul {nume_angajat} nu a fost gasit.")

    @classmethod
    def update_nume(cls, nume_angajat):
        nume_actual = None
        cursor = Date_Angajati.find({'Nume': nume_angajat}, {'_id': 0, 'Nume': 1})
        for i in cursor:
            nume_actual = i["Nume"]
        if Date_Angajati.count_documents({'Nume': nume_angajat}) > 0:
            print(f"Numele angajatului este: {nume_actual}")
            if input("Doriti sa modificati numele ?"
                     "Y/N: ").upper() == "Y":
                nume_actual = input("Introduceti noul nume: ")
                Date_Angajati.update_one({'Nume': nume_angajat}, {"$set": {"Nume": nume_actual}})
                print(f"Numele angajtului {nume_angajat} este acum: {nume_actual}")
            else:
                print("Schimbare neefectuata")
        else:
            print(f"Angajatul {nume_angajat} nu a fost gasit.")

    @classmethod
    def update_job(cls, nume_angajat):
        job_actual = None
        cursor = Date_Angajati.find({'Nume': nume_angajat}, {'_id': 0, 'Pozitie': 1})
        for i in cursor:
            job_actual = i["Pozitie"]
        if Date_Angajati.count_documents({'Nume': nume_angajat}) > 0:
            print(f"Jobul angajatului {nume_angajat} este: {job_actual}")
            if input("Doriti sa modificati jobul ?"
                     "Y/N: ").upper() == "Y":
                job_actual = input("Introduceti noul job: ")
                Date_Angajati.update_one({'Nume': nume_angajat}, {"$set": {"Pozitie": job_actual}})
                print(f"Jobul angajtului {nume_angajat} este acum: {job_actual}")
            else:
                print("Schimbare neefectuata")
        else:
            print(f"Angajatul {nume_angajat} nu a fost gasit.")

    @classmethod
    def update_dep(cls, nume_angajat):
        dep_actual = None
        cursor = Date_Angajati.find({'Nume': nume_angajat}, {'_id': 0, 'Departament': 1})
        for i in cursor:
            dep_actual = i["Departament"]
        if Date_Angajati.count_documents({'Nume': nume_angajat}) > 0:
            print(f"Departamentul angajatului {nume_angajat} este: {dep_actual}")
            if input("Doriti sa modificati departamentul ?"
                     "Y/N: ").upper() == "Y":
                dep_actual = Departament.alegere_dep()
                Date_Angajati.update_one({'Nume': nume_angajat}, {"$set": {"Departament": dep_actual}})
                print(f"Departamentul angajtului {nume_angajat} este acum: {dep_actual}")
                Angajat.update_job(nume_angajat)
            else:
                print("Schimbare neefectuata")
        else:
            print(f"Angajatul {nume_angajat} nu a fost gasit.")
