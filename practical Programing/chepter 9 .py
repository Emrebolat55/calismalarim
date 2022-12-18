# range fonksiyonu
#for num in range(10):
 #   print(num) #1 den 10 a kadar olan sayıları yazar
 

#list(range(10)) #sonuç 1 den 10 kadar sayıları listeler halinde yazar

#list(range(3)) #sonuç[0,1,2] 3e kadar listeler halinde yazar

#list(range(1)) #sonuç[0]

#list(range(0)) #sonuç [] çünkü değer yok

#list(range(2000, 2050, 4)) # 2000 ile 2050 arasındaki sayıları 4 er 4 er atlayarak yazar

#list(range(2000, 2050, -4)) # bu sefer tam tersi 4 azaltarak yazar

#1 ile 100 arasındaki sayıların toplamını bulan algoritma
#total = 0
#for i in range(1,101):
    #total = total + i
   # print(total)
    
#girilen listedeki elemanların iki katını alma
#values = [4,10,3,8,-6]
#for num in values:
 #   num = num * 2
  #  print(num)   
# sonuç [8,20,6,16,-12]


#values = [4,10,3,8,-6]
#len(values) #values listesindeki karekter sayısını göstrerir

# hem değer hem de indeksini gösteren algoritma
#values = [4,10,3,8,-6]
#for i in range(len(values)):
 #   print(i,values[i])
 
 #girilen metaleri ağırlığına göre sıralayan algoritma
#metals = ["Li","Na","K"]
#weights = [6.941, 22.98976928, 39.0983]
#for i in range(len(metals)):
 #   print(metals [i] , weights [i]) 
#sonuç
#Li 6.941
#Na 22.98976928
#K 39.0983
 

#girlen metal ve halojenleri sırası ile birleştiren algoritma
#outer = ['Li', 'Na', 'K']
#inner = ['F', 'Cl', 'Br']
#for metal in outer:
 #for halogen in inner:
  #print(metal + halogen)
 #sonuç 
#LiF
#LiCl
#LiBr
#NaF
#NaCl
#NaBr
#KF
#KCl
#KBr


#liste içindeki listeelri ayırma
#elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
#for inner_list in elements:
 #print(inner_list) #listeleri ayır
#sonuç
#['Li', 'Na', 'K']
#['F', 'Cl', 'Br']



# C3H7 dizisindeki ilk basamağın dizisini bulmak için tasarlanan algoritma
#s = 'C3H7'
#digit_index = -1 
#for i in range(len(s)):
    
 #if digit_index == -1 and s[i].isdigit():
  #digit_index = i
  #print(digit_index)
  
  
  
a=int(input("a sayısı:"))
b=int(input("b sayısı:"))
c=int(input("c sayısı:"))
if a>b and a>c:
   print("a en büyük sayıdır")  # a>b ve a>c olduğunda en büyük a olur.
elif b>a and b>c:
   print("b en büyük sayıdır") # b>a ve b>c olduğunda en büyük b olur.
else:
   print("c sayısı en büyüktür") # bunların hiç biri olmadığında c en büyük olur.