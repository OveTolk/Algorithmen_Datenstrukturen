import pandas as pd
import time

# Einlesen der Dateien mit Überprüfung auf gültige Eingaben
def einlesen():
    # Input des Benutzers für den zweiten Dateipfad und Trennzeichen
    file1 = input("Bitte geben Sie den Pfad zur ersten Tabelle an: ")
    delimiter1 = input("Bitte geben Sie das Trennzeichen der ersten Tabelle an: ")

    # Solange der Benutzer kein gültiges Trennzeichen angibt, wird er aufgefordert, ein gültiges Trennzeichen einzugeben
    while delimiter1 not in [",", ";", "\t", "|", ":"]:
        print("Bitte geben Sie ein gültiges Trennzeichen an! (Komma (,), Semikolon (;), Tabulator (\\t), Pipe (|) oder Doppelpunkt (:))")
        delimiter1 = input("Bitte geben Sie das Trennzeichen der ersten Tabelle an: ")
    
    # Input des Benutzers für den zweiten Dateipfad und Trennzeichen
    file2 = input("Bitte geben Sie den Pfad zur zweiten Tabelle an: ")
    delimiter2 = input("Bitte geben Sie das Trennzeichen der zweiten Tabelle an: ")

    # Solange der Benutzer kein gültiges Trennzeichen angibt, wird er aufgefordert, ein gültiges Trennzeichen einzugeben
    while delimiter2 not in [",", ";", "\t", "|", ":"]:
        print("Bitte geben Sie ein gültiges Trennzeichen an! (Komma (,), Semikolon (;), Tabulator (\\t), Pipe (|) oder Doppelpunkt (:))")
        delimiter2 = input("Bitte geben Sie das Trennzeichen der zweiten Tabelle an: ")
    
    # Überprüfung, ob die Dateien .csv Dateien sind
    if file1[-4:] != ".csv" or file2[-4:] != ".csv":
        print("Bitte geben Sie eine .csv Datei an.")
        return einlesen()
    
    if file1 == file2:
        print("Bitte geben Sie zwei unterschiedliche Dateien an.")
        return einlesen()
    
    # Einlesen der Dateien und Überprüfung, ob sie leer sind
    try:
        tab1 = pd.read_csv(file1, delimiter=delimiter1)
        tab2 = pd.read_csv(file2, delimiter=delimiter2)
        if tab1.empty or tab2.empty:
            print("Leere Tabelle – bitte versuchen Sie es erneut!")
            return einlesen()
    
    # Fehlerbehandlung für den Fall, dass die Datei nicht im Dateisystem gefunden wird
    except FileNotFoundError:
        print("Datei nicht gefunden – bitte versuchen Sie es erneut!")
        return einlesen()
    
    # Fehlerbehandlung für den Fall, dass die Datei nicht eingelesen werden kann -> mehrere Errors möglich, daher dann allgemeiner Exception-Block
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei: {e}")
        return einlesen()
    
    return tab1, tab2

# Bestimmung des Namens der Ausgabedatei
def name_output():
    # Input des Benutzers für den Namen der Ausgabedatei
    name = input("Bitte geben Sie den Namen der auszugebenden Tabelle an: ")
    
    # Überprüfung, ob der Name leer ist
    if name == "":
        print("Bitte geben Sie einen gültigen Namen ein.")
        return name_output()
    
    # Überprüfung, ob der Name auf .csv endet und ggf. Entfernung der Endung
    if name[-4:] == ".csv":
        name = name[:-4]
    return name + ".csv"

# Kombination der Tabellen und Standardisierung
def mergeTabs(tab1, tab2):
    combined = pd.concat([tab1, tab2], ignore_index=True)
    return combined

# Auswahl des Attributs, nach dem sortiert werden soll
def attribute_waehlen(tab1, tab2):
    att1 = tab1.columns.tolist()
    att2 = tab2.columns.tolist()
    print(f"Die Attribute der ersten Tabelle sind: {att1}")
    print(f"Die Attribute der zweiten Tabelle sind: {att2}")
    gewaehltes_att = input(f"Bitte wählen Sie ein Attribut aus den Tabellen: ")
    
    # Überprüfung, ob das Attribut in beiden Tabellen vorhanden ist
    if gewaehltes_att not in att1 or gewaehltes_att not in att2:
        print("Das Attribut ist nicht vorhanden!")
        return attribute_waehlen(tab1, tab2)
    return gewaehltes_att

# Auswahl der Sortierreihenfolge
def sortierReihenfolge():
    order = input("Möchten Sie aufsteigend (asc) oder absteigend (desc) sortieren? (asc/desc): ").strip().lower()

    # Überprüfung, ob der Benutzer eine gültige Eingabe getätigt hat
    while order not in ["asc", "desc"]:
        print("Bitte geben Sie eine gültige Eingabe (asc oder desc) ein.")
        order = input("Möchten Sie aufsteigend (asc) oder absteigend (desc) sortieren? (asc/desc): ").strip().lower()
    return order

# Bubble Sort Algorithmus
def bubblesort(df, column, ascending=True):
    df = df.copy()
    n = len(df)
    operation_count = 0
    start_time = time.time()

    for i in range(n):
        for j in range(0, n-i-1):
            operation_count += 1
            print(f"Es läuft noch! Count {operation_count}")
            if (df.iloc[j][column] > df.iloc[j+1][column]) == ascending:
                df.iloc[j], df.iloc[j+1] = df.iloc[j+1], df.iloc[j]

    end_time = time.time()
    duration = end_time - start_time
    return df, operation_count, duration

# Selection Sort Algorithmus
def selectionsort(df, column, ascending=True):
    df = df.copy()
    n = len(df)
    operation_count = 0
    start_time = time.time()

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            operation_count += 1
            print(f"Es läuft noch! Count {operation_count}")
            if (df.iloc[j][column] < df.iloc[min_idx][column]) == ascending:
                min_idx = j
        df.iloc[i], df.iloc[min_idx] = df.iloc[min_idx], df.iloc[i]

    end_time = time.time()
    duration = end_time - start_time
    return df, operation_count, duration

# Hauptfunktion
def main():
    print("Dieses Programm ermöglicht die Kombination von zwei Tabellen und sortiert diese nach verschiedenen Attributen mit zwei gegebenen Sortierverfahren.")
    print("Bitte stellen Sie sicher, dass in der ersten Zeile die Attribute stehen!")
    tab1, tab2 = einlesen()
    output_name = name_output()
    combined = mergeTabs(tab1, tab2)
    sort_attribut = attribute_waehlen(tab1, tab2)
    sortier_reihenfolge = sortierReihenfolge() == "asc"
    
    print("Bitte warten Sie während der erste Algorithmus ausgeführt wird...")

    # Ausführung von Bubble-Sort
    try:
        sorted_bubble, bubble_operations, bubble_duration = bubblesort(combined, sort_attribut, ascending=sortier_reihenfolge)
        sorted_bubble.to_csv(f"{output_name}_bubblesort.csv", index=False)
        print(f"{output_name}_bubblesort.csv gespeichert!")

    # Fehlerbehandlung für den Fall, dass der Algorithmus fehlschlägt
    except Exception as e:
        print(f"Der Algorithmus ist fehlgeschlagen. Fehler: {e}")
        with open("bubblesort_error.log", "w") as log_file:
            log_file.write(str(e))
        print("Eine Log-Datei wurde erstellt.")
    
    print("Bitte warten Sie während der zweite Algorithmus ausgeführt wird...")

    # Ausführung von Selection-Sort
    try:
        sorted_selection, selection_operations, selection_duration = selectionsort(combined, sort_attribut, ascending=sortier_reihenfolge)
        sorted_selection.to_csv(f"{output_name}_selectionsort.csv", index=False)
        print(f"{output_name}_selectionsort.csv gespeichert!")
    
    # Fehlerbehandlung für den Fall, dass der Algorithmus fehlschlägt
    except Exception as e:
        print(f"Der Algorithmus ist fehlgeschlagen. Fehler: {e}")
        with open("selectionsort_error.log", "w") as log_file:
            log_file.write(str(e))
        print("Eine Log-Datei wurde erstellt.")
    
    # Speichern der Metriken der Algorithmen
    save_metrics = input("Möchten Sie die Metriken der Algorithmen ebenfalls sichern? (Ja / Nein): ").strip().lower()
    if save_metrics in ["ja", "yes", "y"]:
        metrics_file = f"{output_name}_metrics.txt"
        with open(metrics_file, "w") as f:
            f.write("Metriken der Algorithmen:\n")
            f.write("Bubble Sort:\n")
            f.write(f"Anzahl der Zeilen: {len(sorted_bubble)}\n")
            f.write(f"Anzahl der Spalten: {len(sorted_bubble.columns)}\n")
            f.write(f"Anzahl der Vorgänge: {bubble_operations}\n")
            f.write(f"Benötigte Zeit: {bubble_duration:.6f} Sekunden\n\n")
            f.write("Selection Sort:\n")
            f.write(f"Anzahl der Zeilen: {len(sorted_selection)}\n")
            f.write(f"Anzahl der Spalten: {len(sorted_selection.columns)}\n")
            f.write(f"Anzahl der Vorgänge: {selection_operations}\n")
            f.write(f"Benötigte Zeit: {selection_duration:.6f} Sekunden\n")
        print(f"Metriken gespeichert in: {metrics_file}")
    else:
        print("Metriken wurden nicht gespeichert.")

# Start des Programms
if __name__ == "__main__":
    main()
