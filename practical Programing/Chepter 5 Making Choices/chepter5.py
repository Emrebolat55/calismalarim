# boolen operatörleri
#not true
# false

#not False
# true

# and kapısı 
#True and True
 # true
#False and False
# False
#True and False
# False
#False and True
# False


# or kapısı
#True or True
# True

#False or False
# False

#True or False
# True

#False or True
# True

# atama yapma
#cold=True
#windy=False
#(not cold) and windy
# False
#not (cold and windy)
# True

# semboler ve gösterimleri 
# Symbol  Operation
#   >     Büyüktür 
#   <     Küçüktür 
#   >=    Büyük eşittir  
#   <=    Küçük eşitti 
#   ==    Eşittir 
#   !=    Eşit değildir 

#x=2
#y=5 
#z=7
#x<7 and y<z
# sonuç True

#3<5 !=True
# True
#3<5 !=False
#(2<3) or (1/0)
# True


# str ifadeleri kıyaslama

#'A'<'a'
# True

#'A'>'z'
# False

#'abc'< 'abd'
# True

#'abc'<'abcd'
# True

#'Jan'in '01 Jan 1838'
# True

#'Feb'in ('01 Jan 1838')
# False

# girilien sayıdan ph değeri bulma
#ph=float(input('ph seviyesi giriniz:'))
#if ph<7:
 #   print(asıt)
#elif ph>7:
 #   print(baz)
    
 
 
#if else elif örnekleri
#A= input('bir bileşen gir: ')
#if A == "H2O": #eğer A eşittir H2O ise su yazdır
 #  print("su")
#elif A == "NH3": # eğer A eşittir NH3 ise amonyak yazdır
 #    print("amonyak")
#elif A == "CH4": # eğer A eşittir CH4 ise metan yazdır
 #   print("metan")
    
     
 # girilen elementin adını söyelyen if else algoritması    
#compound = input('Enter the compound: ') #bir bileşik girin
#if compound == "H2O": # eğer bu bileşik H2O ise Water yazdır
 #print("Water")
#elif compound == "NH3":# eğer bu NH3 ise Ammonia yazdır
 #print("Ammonia")
#elif compound == "CH4":# eğer bu bileşik CH4 ise Methane yazdır
 #print("Methane")
#else:
 #print("Unknown compound") # hiçbiri değilse bileşiği bilmiyorumm
 
 
 
 #girilen sayınının asitmi,baz yada nötr olduğunu gösteren algoritma
#value = input('Enter the pH level: ')
#if len(value) > 0: #eğer girilen değer > 0 ise ph tam sayıdır
 #ph = float(value)
#if ph < 7.0: # girilen rakam < 7 ise asidiktir 
 #print(ph, "is acidic.")
#elif ph > 7.0: # yada girlen değer > 7 ise basic yazılır
 #print(ph, "is basic.")
#else:  # hiçbiri değilse nötr yazılır
 #print(ph, "is neutral.")







