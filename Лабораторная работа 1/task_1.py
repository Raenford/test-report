numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbersS = [i for i in numbers if i is not None]
a = round(sum(numbersS)/len(numbers),  2)
numbers = [item if item else a for item in numbers]
print("Измененный список:", numbers)
