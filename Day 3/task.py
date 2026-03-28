print('''.,od88888888888bo,.
                            .d88888888888888888888888b.
                         .d88888888888888888888888888888b.
                       .d888888888888888888888888888888888b.
                     .d8888888888888888888888888888888888888b.
                    d88888888888888888888888888888888888888888b
                   d8888888888888888888888888888888888888888888b
                  d888888888888888888888888888888888888888888888
                  8888888888888888888888888888888888888888888888
                  8888888888888888888888888888888888888888888888
                  8888888888888888888888888888888888888888888888
                  Y88888888888888888888888888888888888888888888P
                  "8888888888P'   "Y8888888888P"    "Y888888888"
                   88888888P        Y88888888P        Y88888888
                   Y8888888          ]888888P          8888888P
                    Y888888          d888888b          888888P
                     Y88888b        d88888888b        d88888P
                      Y888888b.   .d88888888888b.   .d888888
                       Y8888888888888888P Y8888888888888888
                        888888888888888P   Y88888888888888
                        "8888888888888[     ]888888888888"
                           "Y888888888888888888888888P"
                                "Y88888888888888P"
                             888b  Y8888888888P  d888
                             "888b              d888"
                              Y888bo.        .od888P
                               Y888888888888888888P
                                "Y88888888888888P"
                                  "Y8888888888P"
          d8888bo.                  "Y888888P"                  .od888b
         888888888bo.                  """"                  .od8888888
         "88888888888b.                                   .od888888888[
         d8888888888888bo.                              .od888888888888
       d88888888888888888888bo.                     .od8888888888888888b
       ]888888888888888888888888bo.            .od8888888888888888888888b=
       888888888P" "Y888888888888888bo.     .od88888888888888P" "Y888888P=
        Y8888P"           "Y888888888888bd888888888888P"            "Y8P
          ""                   "Y8888888888888888P"
                                 .od8888888888bo.
                             .od888888888888888888bo.
                         .od8888888888P"  "Y8888888888bo.
                      .od8888888888P"        "Y8888888888bo.
                  .od88888888888P"              "Y88888888888bo.
        .od888888888888888888P"                    "Y8888888888888888bo.
       Y8888888888888888888P"                         "Y8888888888888888b=
       888888888888888888P"                            "Y8888888888888888=
        "Y888888888888888       Everest the great        "Y88888888888888P=
             ""Y8888888P                                  "Y888888P"
                "Y8888P                                     Y888P"
                   ""                                        """ 
''')
print("Welcome to Skull Island.")
print("Your mission is to find the treasure.")
cross_road = input('''You're at a cross road. Where do you want to go?\nype "left" or "right"''').lower()

if cross_road =="left":
    lake = input(
        '''You've come to a lake. There is an island in the middle of the lake.
        \nType "wait" to wait for a boat. Type "swim" to swim across.''').lower()
    if lake == "wait":
        island = input(
            '''You arrive at the island unharmed.
             There is a house with 3 doors.\nOne red, one yellow and one blue. 
             Which colour do you choose?''').lower()
        if island == "yellow":
            print("Yay, You have acquired the Treasure now run back to your ship before the island collapse")

        elif island == "red":
            print("That door contains fire")
    else:
        print("You should have waited for a boat now you drowned because your avatar lacks the training to swim")
else:
    print("Sorry you went the wrong way and got trapped. Please try again")

