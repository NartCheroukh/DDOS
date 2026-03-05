import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""               


                         Адыгэ нып Адыгэ нып Адыгэ нып Адыгэ нып 
                         Адыгэ нып Адыгэ нып Адыгэ нып Адыгэ нып 
                         Адыгэ нып Адыгэ нып Адыгэ нып Адыгэ нып  
                         Адыгэ нып Адыгэ нып Адыгэ нып Адыгэ нып        


                        
                                             DGF DDOS TOOL  

                    DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! 
                        DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! 
                    DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! 
                        DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! 
                    DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! 
                        DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! 
                    DGF LEXE AYWA !!!! DGF LEXE AYWA !!!! DGF LEXE AYWA !!!!  


                                            
""")

def display_menu():
    print(Fore.GREEN + """
    1: DDoS
    3: bilgi
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Nrprotocol/ddos-tool.py"' if os.name == 'nt' else 'python Infinity-Tool/ddos-tool.py')
    elif command == '3':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')

        display_menu()
    else:
        print('wrong/yanlis ! doðrusunu gir mal.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
