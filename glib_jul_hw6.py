#task 1
a = {}
b = input()
b = b.split()
for i in b:
    count = a.get(i)
    if count:
        a[i] = count + 1
    else:
        a[i] = 1
print(a)

#task 2
translations = {
     'hello': 'привет',
     'goodbye': 'до свидания',
     'cat': 'кот',
     'dog': 'собака'
}
a = input()
if a in translations:
    print(translations.get(a))

#task 3
result = dict()
print('Існуючі номери: \n')
while True:
    name = input('Введіть прізвище: ')
    cont = int(input('Введіть номер: '))
    if name not in result:
        result[name] = cont
        print('Існуючі номери: \n')
        for i in result:
            print(i, result[i])
    else:
        print('Вже є таке прізвище')
    break

#task 4
 
currencies = {"UAH": 1.0, "USD": 37.18, "PLN": 8.80, "EUR": 39.46}
sum = float(input("Введіть суму у гривнях: "))
a = input("Ведіть потрібну валюту: ")
result = 1
if a in currencies:
    b = float(currencies.get(a))
    result = sum * b
    print(result) 