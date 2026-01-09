def fair_sharer(werte, iterationen, anteil):
    """
    Diese Funktion simuliert einen fairen Verteiler bsp von Vermögen
    
    
    werte: Die Vermögensverteilung als Python-Liste
    iterationen: Wie oft die Anpassung durchgefühhrt wird
    anteil: Der prozentuale Anteil, den der "Reichste" abgeben muss
    """
    for iteration in range(iterationen):
        max_wert = float("-inf")
        # Sucht den größten Wert
        for i, wert in enumerate(werte):
            if wert > max_wert:
                max_wert = wert
                max_ind = i
        # Zieht dem max_Wert seinen Anteil ab
        abzug = anteil * max_wert
        werte[max_ind] -= abzug
        # Verteile es an Nachbarn
        left = (max_ind - 1) % len(werte)
        right = (max_ind + 1) % len(werte)
        werte[left] += abzug / 2
        werte[right] += abzug / 2
        # Zum erstmaligen testen
        print(werte, iteration)
    return werte

werte = [0, 1000, 800, 0]
fair_sharer(werte, iterationen=2, anteil=0.2)
