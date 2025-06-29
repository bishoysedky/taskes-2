try :
    the_temperature = float(input("Enter the temperature here: "))
    if the_temperature >= 30:
        print("It's a hot day 🥵. Stay hydrated. Drink a lot of water! 🥤")

    elif 20 <= the_temperature <= 29:
      print("It's a good day to do sport 🏐. Enjoy the weather!")

    elif 10 <= the_temperature <= 19:
     print("It's a cool day ☃️. Wear a jacket!")

    else:
      print("It's a cold day 🥶. Stay warm!")
      
except ValueError:
    print("please enter number!")