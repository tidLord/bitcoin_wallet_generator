from bitcoinaddress import Wallet
from colorama import Fore, Style

working = True
while working == True:
    count_is_int = False
    while count_is_int == False:
        count = input(Fore.MAGENTA + Style.BRIGHT + 'Amount to generate' + Style.RESET_ALL + ' : ')
        try:
            count = int(count)
            if count > 0:
                count_is_int = True
            else:
                print(Fore.RED + Style.BRIGHT + '??? Count < 1 ???\n' + Style.RESET_ALL)
        except:
            print(Fore.RED + Style.BRIGHT + '!!! Amount must be INT !!!\n' + Style.RESET_ALL)
    text = '************\nBitcoin wallet generator 1.0 by tidLord\n[ WIF private key format & compressed address ]\n************\n\n'
    for i in range(1,int(count)+1):
        genhex = Wallet()
        wallet = Wallet(genhex.key.hex)
        text += 'Wallet Number : ' + str(i) + '\nPrivate Key : ' + wallet.key.__dict__['mainnet'].__dict__['wifc'] + '\nBitcoin Address : ' + wallet.address.__dict__['mainnet'].__dict__['pubaddr1c']
        if i < int(count):
            text += '\n\n'
        print(Fore.BLUE + '> ' + Style.RESET_ALL + Fore.YELLOW + str(i) + Style.RESET_ALL + Fore.GREEN + ' created' + Style.RESET_ALL)
    with open('result.txt','w', encoding='utf-8') as file:
        file.write(text)
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'Finished' + Style.RESET_ALL + ' :-)\n')
    ask_to_working = True
    while ask_to_working == True:
        need_continue_working = input(Fore.MAGENTA + Style.BRIGHT + 'Want to work again? (Y/N)' + Style.RESET_ALL + ' : ')
        if need_continue_working == 'Y' or need_continue_working == 'y':
            print('\n')
            ask_to_working = False
        elif need_continue_working == 'N' or need_continue_working == 'n':
            ask_to_working = False
            working = False
        else:
            print(Fore.RED + Style.BRIGHT + '!!! Please answer Y or N only !!!\n' + Style.RESET_ALL)