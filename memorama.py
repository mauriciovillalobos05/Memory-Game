def pedir_números(mem,memorama):
    r=int(input("renglón de la primera tarjeta: "))
    c=int(input("columna de la primera tarjeta: "))
    mem[r-1][c-1]=memorama[r-1][c-1]
    ren=int(input("renglón de la segunda tarjeta: "))
    col=int(input("columna de la segunda tarjeta: "))
    mem[ren-1][col-1]=memorama[ren-1][col-1]
    print(*mem,sep="\n")
    if memorama[r-1][c-1]!=memorama[ren-1][col-1]:
            mem[ren-1][col-1]= "| |"
            mem[r-1][c-1]= "| |"
            print("terminó tu turno")
    else:
        print("Padrote(a), te va de nuevo")
    if mem!=memorama:    
        pedir_números(mem,memorama)

mem=[["| |","| |","| |","| |","| |","| |","| |","| |","| |","| |"],
    ["| |","| |","| |","| |","| |","| |","| |","| |","| |","| |"],
    ["| |","| |","| |","| |","| |","| |","| |","| |","| |","| |"],
    ["| |","| |","| |","| |","| |","| |","| |","| |","| |","| |"],
    ["| |","| |","| |","| |","| |","| |","| |","| |","| |","| |"]]

memorama=[["| 1 |","| 11 |","| 2 |","| 12 |","| 5 |","| 4 |","| 18 |","| 9 |","| 8 |","| 8 |"],
        ["| 17 |","| 15 |","| 12 |","| 2 |","| 13 |","| 4 |","| 23 |","| 19 |","| 10 |","| 15 |"],
        ["| 6 |","| 3 |","| 25 |","| 9 |","| 16 |","| 21 |","| 22 |","| 23 |","| 24 |","| 16 |"],
        ["| 7 |","| 19 |","| 3 |","| 24 |","| 14 |","| 20 |","| 1 |","| 7 |","| 22 |","| 21 |"],
        ["| 6 |","| 18 |","| 25 |","| 5 |","| 13 |","| 20 |","| 17 |","| 14 |","| 15 |","| 10 |"]]

pedir_números(mem,memorama)