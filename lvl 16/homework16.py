start = int(input("enter range start: "))
end = int(input("enter range end: "))
step = int(input("enter step (ნაბიჯი): "))


start = int(input("enter range start: "))
end = int(input("enter range end: "))
step = int(input("enter step (ნაბიჯი): "))

for number in range(start, end, step):
     if number % 2 == 0:       
      print(number)