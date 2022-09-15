input = 'LSRXUIBRSHQLTBWXBHSOZDBDJIIQSVOSYVSRSOWHSWZSMCUECNPPTWGWHIHWWIISMCSQTHLSSVVSLTWQHQLGWJINYTFJXBHTBHXSHTFICHWRVPJSWHSPJBKIFSINXSOKTUICZETGWIGMRVVJBHWSVPIWQSLPITISRSOWHAICGGWZMRVIGSVUWRSIRVGKTWWIYIXBIVSLTWQHQLGWJIOYHHYTTXTZRZORCRMTAICGGWZMRVIGSVUWRSIRVGKTWWIBMRVXPIGWOYUNYACIHSRKSVBCIRVXT'
ofset = 3
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
zählen = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = -3 #start offset (this is intersting, i have not found out the magic so...)

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
    length = len(input) 
    while i <= len(input):
        
        i += ofset
        if i >= len(input):
                esc_print()  
        zählen[finder(abc, input[i])] += 1
    esc_print()

if __name__ == '__main__':
    main()  