primers = [2, 3, 5, 7, 11, 13, 17]  # Llista de primers fins 17

def backtracking(s, prob_test, prob_graf, prob_clas, test_parell, graf_parell, clas_consec, suma_grafics):
    pos = len(s) + 1                # Posició del proper problema (a partir de 1)
    es_parell = int(pos%2 == 0)     # 1 si estem en una posició parell, 0 si estem en una senar

    # Retornem si hem posat massa problemes d'un tipus o tenim massa clàssics consecutius
    if prob_test > 4 or prob_graf > 4 or prob_clas > 9 or clas_consec == 3:
        return

    # Si hem arribat al final, comprovem totes les condicions que no venen assegurades pel propi backtracking
    if (len(s) == 17):
        # Condició 3
        cond_3 = (graf_parell == test_parell)

        # Condició 4
        cond_4 = False
        for i in range(7):
            if s[i] == 'q':
                if s[i + 10] == 'q' and s[i + 5] == 'q':
                    cond_4 = True

        # Condició 5. Anem amb compte que la posició de problema es compta des d'1
        cond_5 = False
        for i in range(17):
            for j in range(17 - i - 1):
                if i != j and s[i] == 'g' and s[j] == 'g' and s[i + j + 1] == 'g':
                    cond_5 = True

        # Si es compleix tot, escrivim
        if cond_3 and cond_4 and cond_5:            
            print(s)
        
        # Retornem
        return
    
    # Fem backtracking per cada possibilitat, actualitzant la resta de variables
    if (pos not in primers):
        backtracking(s + 'q', prob_test + 1, prob_graf, prob_clas, test_parell + es_parell, graf_parell, 0, suma_grafics)
        backtracking(s + 'g', prob_test, prob_graf + 1, prob_clas, test_parell, graf_parell + es_parell, 0, suma_grafics + pos)
    backtracking(s + 'c', prob_test, prob_graf, prob_clas + 1, test_parell, graf_parell, clas_consec + 1, suma_grafics)

backtracking("", 0, 0, 0, 0, 0, 0, 0)

