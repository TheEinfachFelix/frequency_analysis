input = 'LSRXUIBRSHQLTBWXBHSOZDBDJIIQSVOSYVSRSOWHSWZSMCUECNPPTWGWHIHWWIISMCSQTHLSSVVSLTWQHQLGWJINYTFJXBHTBHXSHTFICHWRVPJSWHSPJBKIFSINXSOKTUICZETGWIGMRVVJBHWSVPIWQSLPITISRSOWHAICGGWZMRVIGSVUWRSIRVGKTWWIYIXBIVSLTWQHQLGWJIOYHHYTTXTZRZORCRMTAICGGWZMRVIGSVUWRSIRVGKTWWIBMRVXPIGWOYUNYACIHSRKSVBCIRVXT'
ofset = 3 # the general ofset (this can only be 1 or more not 0)
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
zählen = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = 0 #start offset (0 is the first and so on)

def finder(array, tofind) -> int:
    for element in range(len(array)):
        if array[element] == tofind:
            return int(element)
    return False

def esc_print():
    for i,x in enumerate(abc):
        print(str(x) + " : " + str(zählen[i]))
    exit()

def main():
    global i
    while i <= len(input):
        zählen[finder(abc, input[i])] += 1
        i += ofset
        if i >= len(input):
                esc_print()  
    esc_print()

if __name__ == '__main__':
    main()  