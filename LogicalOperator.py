num1 = 10
num2 = 50
num3 = 30

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)

else:
    print(num3)

    #Vowel Consonant with 'or'

ch = 'h'

if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print('Vowel')
else:
    print("Consonat")



        #Letter Grade

marks = 42

if 80<= marks <=100:
    print("A+")
elif 70<= marks <=79:
    print("A")
elif 60<= marks <=69:
    print("A-")
elif 50<= marks <=59:
    print("B")
elif 33<= marks <=49:
    print("C")
else:
    print("F")