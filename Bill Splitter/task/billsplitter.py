import random

friends_number = int(input("Enter the number of friends joining (including you): "))

if friends_number > 0:
    print("\nEnter the name of every friend (including you), each on a new line: ")

    friends_dict = {input(): 0.0 for _ in range(friends_number)}

    bill_amount = int(input("\nEnter the total bill value: \n"))

    bill_split = bill_amount / len(friends_dict)

    for name in friends_dict:
        friends_dict[name] = round(bill_split, 2)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')

    if input().lower() == 'yes':

        friends_list = [name for name in friends_dict]

        lucky_number = random.randint(0, len(friends_dict) - 1)

        lucky_one = friends_list[lucky_number]

        print(f"\n{lucky_one} is the lucky one!")

        bill_split = bill_amount / (len(friends_dict) -1)

        for name in friends_dict:
            friends_dict[name] = round(bill_split, 2)

        friends_dict[lucky_one] = 0

        print("\n" + str(friends_dict))

    else:
        print("\nNo one is going to be lucky")
        print("\n" + str(friends_dict))

else:
    print("\nNo one is joining for the party")

