
def count(int n):
    """Funkcija: ako je paran n/2, neparan n*3+1
    
    Omogucava da vraca broj koraka ako koristimo forume koje su vec navedene
    
    Arguments:
        int n  -- Vraca nam najveci broj sa najvise koraka
    
    Returns:
        steps -- 
    """
    lista = []
    for i in range(1, n):
        fake_n = i
        steps = 1
        while fake_n != 1:
            steps = steps + 1
            if fake_n%2==0:
                fake_n = fake_n/2
            elif fake_n%2==1:
                fake_n = 3*fake_n+1
        lista.append([i, steps])
    print('Done')
    return max(lista, key=lambda x: x[1])
