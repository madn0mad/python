"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над четвертым заданием.
Разработать методы, отвечающие за приём оргтехники на
склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над пятым заданием. Р
еализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class merror(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    def __init__(self, model):
        self.model = model


class OfficePrinter(OfficeEquipment):
    def __init__(self, printer_type, model):
        super().__init__(model)
        self.printertype = printer_type


class OfficeScanner(OfficeEquipment):
    def __init__(self, scanner_dpi, model):
        super().__init__(model)
        self.dpi = scanner_dpi


class OfficeCopier(OfficeEquipment):
    def __init__(self, copier_velocity, model):
        super().__init__(model)
        self.velocity = copier_velocity


class Storage:

    def __init__(self):
        self.estorage = {}

    def __str__(self):
        return f'{self.estorage}'

    def st_income(self, new_equipment: OfficeEquipment, equantity):
        try:
            if type(equantity) != int:
                raise merror('Неверный тип данных. Необходимо указать число')
            self.estorage.update({new_equipment.model: equantity})
        except merror as err:
            print(err)

    def transfer_to(self, new_equipment: OfficeEquipment, equantity):
        try:
            if type(equantity) != int:
                raise merror('Неверный тип данных. Необходимо указать число')
            emodel = self.estorage.get(new_equipment.model)
            self.estorage.update({new_equipment.model: emodel - equantity})
        except merror as err:
            print(err)


mystorage = Storage()
printer1 = OfficePrinter('Струйный', 'Epson L805')
printer2 = OfficePrinter('Лазерный', 'HP LaserJet Pro M15w')
scanner1 = OfficeScanner('4800x4800', 'Canon CanoScan LiDE 400')
scanner2 = OfficeScanner('600x600', 'Brother ADS-2400N')
copier1 = OfficeCopier('21', 'Canon PIXMA MG2540S')
copier2 = OfficeCopier('99', 'Platinum M6500')
mystorage.st_income(printer1, 5)
mystorage.st_income(printer2, 15)
mystorage.st_income(scanner1, 7)
mystorage.st_income(scanner2, 4)
mystorage.st_income(copier1, 2)
mystorage.st_income(copier2, 4)
print(mystorage)

mystorage.transfer_to(printer2, 7)
print(mystorage)

mystorage.transfer_to(printer1, '2')
mystorage.st_income(scanner2, '22')
