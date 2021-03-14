# Vasilescu Alexandru Madalin 331CB
import sys
import string

f = open((str(sys.argv[1])), 'r')
# Citire din fisier si eliminarea '\n' de la finalul liniei pentru pattern si text
pattern = f.readline()
pattern = pattern[:-1]
t = f.readline()
t = t[:-1]
f = open((str(sys.argv[2])), 'w')
# Lista cu toate literele in format upper case
alphabet = [x for x in string.ascii_uppercase]
# Matricea de patternuri cu cate o linie pentru fiecare lungime a patternului
# Am completat matricea cu 0 pentru ca ulterior sa modific doar unde gasesc match
matrix = [[0 for _ in alphabet] for _ in range(len(pattern) + 1)]


# Functia de calcul a matricei
def matrix_calculator():
    # Iterez pentru fiecare status al patternului de la empty la lungimea intreaga
    for status in range(len(pattern) + 1):
        # Folosesc un string auxiliar in care retin doar primele status caractere din pattern
        s = pattern[:status]
        # Iterez peste alfabet si retin atat indexul literei cat si litera
        for idx, letter in enumerate(alphabet):
            # Adaug litera la finalul stringului
            s = s + letter
            # Iterez peste lungimea stringului auxiliar
            for i in range(len(s)):
                # Daca ultimele i caractere in stringul auxiliar se potrivesc cu primele i caractere
                # Din pattern actualizez matricea
                if s[i:] == pattern[:len(s) - i]:
                    matrix[status][idx] = len(s) - i
                    break
            # Elimin litera de la finalul stringului
            s = s[:-1]


# Functia explicata si la curs de cautara a patternului in text
def pattern_finder():
    state = 0
    # Iterez peste lungimea textului
    for i in range(len(t)):
        # Modific state in functie de valoare din matrice a literei de la indexul i
        state = matrix[state][alphabet.index(t[i])]
        # Daca se ajunge la lungimea patternului se afiseaza pozitia de unde incepe patternul
        if state == len(pattern):
            f.write(str(i - state + 1)+' ')


# Apelurile functiilor de calcul al matricelor si gasire a patternului
matrix_calculator()
pattern_finder()
f.write('\n')
