def cost_bennefit_inner():
    with open("1.txt", 'r') as input1:
        lista = []
        for line in input1.readlines():
            if 'HVM' in (line):
                it = line.split(',')[0]
                vpcu = line.split(',')[1]
                with open("2.txt", 'r') as input2:
                    for line1 in input2.readlines():
                        if it in (line1):
                            mem = line1.split(',')[1]
                            custo = line1.split(',')[2]
                            # Formula #
                            mem = float(mem)
                            vpcu   = float(vpcu)
                            custo = float(custo)
                            cost_benefit = (((mem / 3.75) + vpcu)/custo)
                            cost_benefit = round(cost_benefit, 0)
                        
                            lista.append((it,cost_benefit))
        return lista

def cost_bennefit_out(lista):
    lista = sorted(lista, reverse=False, key=lambda it: it[1])
    with open("output.txt", 'a') as output:
        for i in lista:
            i = i[0]
            output.write(i+'\n')
def main():
    a = cost_bennefit_inner()
    cost_bennefit_out(a)
   
   
if __name__ == "__main__":
    main()

