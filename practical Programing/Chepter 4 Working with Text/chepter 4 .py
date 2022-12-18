#girilen karekter dizesinin uzunluğunu gösteren fonksiyon

#len('Albert Einstein') # Albert Einstein 15 karekterden oluşmakta

#len('123!') # 4 tane içerik olduğu için ,

#len(' ')  # içerisinde 0  karekteri olduğu için 1

#len('')  #içerisine hiç karekter olmadığı için 0 



#iki tane karekteri birleştirme

#'Albert' + ' Einstein'  # sonuç 'Albert Einstein'
#"Alan Turing" + ""  #sonuç Alan Turing çünkü karekter dizesinin  içi boşş olduğu için 0 kabul edilir

# sayıları ifade etmede kulandığımız fonksiyonlar

#int('0') #int tam sayıları temsil eder sonuç 0
#int("11")   #11
#int('-324')  #-324
#float('-324') #-324.0 float ise küsüratlı sayıları temsil eder
#float("56.34") #56.34

#a = "AT" *5 #AT kelimesinini 5 kere ekrana yazdırır
#print(a)


#sequence = 'ATTGTCCCCC' #bu atamanın  kaç karekter içerdiğini gösterir
#print(len(sequence))
#sonuç 10
#new_sequence = sequence + 'GGCCTCCTGC' #değişkene karekter atama ve toplama
#print(new_sequence * 2) #ve atadığımız karekterin sonucunu 2 ile çarpma
#sonuç 'ATTGTCCCCCGGCCTCCTGCATTGTCCCCCGGCCTCCTGC'


#species = input("Homo sapiens")
#print("species")

#population = input(6973738433) #değişken tanımlama
#print(population)

sayi=int(input("sayı giriniz:"))
if(sayi<0): 
    print("Sayı Negatif") # girilen sayı 0'dan küçük olunca ekrana negatif yazdır 
elif (sayi>0):
    print("Sayı Pozitif") # girilen sayı 0'dan büyük olunca ekrana pozitif yazdır 
else:
    print("Sayı Sıfırdır") # girilen sayı diğerlerini içermiyorsa ekrana 0 yazdır
