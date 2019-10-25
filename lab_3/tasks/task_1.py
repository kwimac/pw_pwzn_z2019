def parse_input(input):
    """
    W dzisiejszych zadaniach nalezy uzywac tylko modulow wbudowanych.

    Splits multiline string into list of lists with integers.

    Napisz funkcję przymującą wielolinijkowy ciąg znaków.
    a zwracającą listę list liczb całkowitych znajdujących się w podanym ciągu znaków.
    Nie używaj pętl for i while.
    String może zawierać puste linie na początku i końcu.

    :param input: string to parse
    :type input: str
    :return: list of parsed list of integers
    :rtype: list

    wskazówka: skorzystac z modulu string
    """
    temp = input.splitlines(False) # zwraca nam jako elementy listy wiersze w stringu


    temp1 = list(filter(lambda x: x!="", temp))# wywala puste wiersze

    temp2 = list(map(lambda x: x.split(),list(temp1))) # dla kazdego elementu listy wykonywane jest podzielenie jego wartosci na liste w miejscu spacji -- podobnie jak przy lapply w r

    #nie mamy tutaj uzyc map(map) tylko zastosowac comprehension
    temp3 = list(map(
        lambda y: list(map(
            lambda x: int(x),y)),temp2)) # pierwszy map zwraca kazdy element zewnetrznej listy a drugi map mapuje dla kazdego elementu w wewnetrznym elemencie listy na inta

    return (temp3)


if __name__ == '__main__':
    _input = """
1 5
1 6 7
3 2
1 10
1 10
1 6
2 5
3 2
    
    
    """
    assert parse_input(_input) == [
        [1, 5], [1, 6, 7], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]
    ]
