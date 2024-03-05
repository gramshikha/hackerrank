def creditcardcheck(credno):
    val = False
    if credno[0] == '4' or credno[0] == '5' or credno[0] == '6':
        val = True

    if val:
        return 'Valid'
    else:
        return 'Invalid'        

    # to check the number of digits in credit card 


cardno = input("Enter your credit card no:")
print(creditcardcheck(cardno))