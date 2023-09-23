def printing_style(a):
    printing = "+" + a + "+"
    emptyline = "+" + " "*len(a) + "+"
    addline = "+" * len(printing)

    print(f"{addline}\n{emptyline}\n{printing}\n{emptyline}\n{addline}\n")

def printing_style1(a, b, c, d):
    ls = []

    ls.insert(0, len(a))
    ls.insert(0, len(b))
    ls.insert(0,len(c))
    ls.insert(0,len(d))
    ls.sort()
    lenght = ls[-1]

    addline = "+"*(lenght + 2)
    emptyline = "+" + " "*lenght + "+"
    printingline = "+" + a + " "*(lenght - len(a)) + "+"
    printingline1 = "+" + b + " "*(lenght - len(b)) + "+"
    printingline2 = "+" + c + " "*(lenght - len(c)) + "+"
    printingline3 = "+" + d + " "*(lenght - len(d)) + "+"

    print(f"{addline}\n{emptyline}\n{printingline}\n{emptyline}\n{printingline1}\n{emptyline}\n{printingline2}\n{emptyline}\n{printingline3}\n{addline}")

def hangman_name_style():
    for _ in range(0, 100):
        print("")
    print('''
    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    ''')
    print("\n")
