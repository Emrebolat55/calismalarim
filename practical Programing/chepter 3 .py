#abs(-9) # cevap 9 içerisine yazılan sayının mutlak değerini bulur 

#değişken atma abs örneği
#day_temperature = 3
#night_temperature = 10
#print(abs(day_temperature - night_temperature))
#sonuç = 7 içerisindeki karekterlerin  mutlak değerini alır 

#print(abs(-7) + abs(3.3)) #sonuç=10.3 

#print(pow(abs(-2), round(4.3))) #abs 2 roun 4 pow 2 üzeri 4 olduğu için cevap 16
a=int(input("a sayısı:"))
b=int(input("b sayısı:"))
c=int(input("c sayısı:"))
if a>b and a>c :
 print("a en büyük sayıdır")  # a>b ve a>c olduğunda en büyük a olur
elif b>a and b>c:
 print("b en büyük sayıdır") # b>a ve b>c olduğunda en büyük b olur
else: 
  print("c sayısı en büyüktür") # bunların hiç biri olmadığında c en büyük olur