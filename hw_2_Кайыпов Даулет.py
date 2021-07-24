current_year = 2021

class Person:
    """docstring"""
    __total_person= 0

    def __init__(self,name,birth_year,**language):
        if birth_year > current_year:
            raise Exception (f"{name}  не может существавать, вы неверно указали год")
        else:
            self.__birth_yer = birth_year
            self.__name = name
            self.__language = language.get("language")
            Person.inc_person()


    def is_adault(self):
        if current_year - self.__birth_yer >=12:
            return True
        else:
            return False


    def get_name(self):
        return self.__name

    @classmethod
    def get_total_person(cls):
        return  cls.__total_person

    def get_language(self):
        return self.__language


    def talk(self):
        print("Hello World")



    @classmethod
    def inc_person(cls):
        cls.__total_person += 1

class Teacher(Person):
    def talk(self):
        print("Greetings, I'm your teacher")

    def teach(self):
        print("Lesson started by Teacher")



p1 = Person("Ivan", 2011,language= "russian" )
p2 = Person("Jeims", 2009)
p3 = Person("Aidar", 2012, language="Africa")

t1 = Teacher("Daaaa",2006, language="English")
t2 = Teacher("DEEEE", 1978)
t3 = Teacher("DYYYY", 2004)

print(p1.get_language())
print(p2.get_total_person())
print(t1.get_name(),t1.get_language(),t1.talk())
print(Person.get_total_person())