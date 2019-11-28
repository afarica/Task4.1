class Students:
	def __init__(self, name, lastname,department, year_of_entrance):
		self.name = name
		self.lastname=lastname
		self.department=department 
		self.year_of_entrance=year_of_entrance
	def get_students_info(self):
		print(f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет {self.department}')

info=Students('Вася','Иванов','Программирование','2017')
info.get_students_info()

info1=Students('Шамир','Бейшебаев','Инженерия','2019')
info1.get_students_info()