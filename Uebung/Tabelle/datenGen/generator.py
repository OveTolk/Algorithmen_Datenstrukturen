import pandas as pd
import numpy as np

# Generator für Testdaten
def generate_test_data(filename, num_entries=5000):
    products = [
        'Hammer', 'Nagel', 'Bohrmaschine', 'Axt', 'Schraube', 'Säge', 'Holz',
        'Stein', 'Meißel', 'Dübel', 'Holzpellets', 'Schachtabdeckung',
        'Linienentwässerung', 'Rigipsplatten', 'Rohr', 'Spiegel', 'Spachtel',
        'Lampe', 'Fliese', 'Fenster', 'Staubsauger'
    ]
    num_products = len(products)
    
    data = {
        'Teilenummer': np.arange(1, num_entries + 1),
        'Bezeichnung': [products[i % num_products] for i in range(num_entries)],
        'Hoehe': np.round(np.random.uniform(0.01, 10.0, num_entries), 2),
        'Breite': np.round(np.random.uniform(0.01, 5.0, num_entries), 2),
        'Gewicht': np.round(np.random.uniform(0.04, 40.0, num_entries), 2)
    }
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, sep=',')
    print(f"Generated {num_entries} entries in {filename}")

# Erzeuge leere Tabelle für Testfall 1
def create_empty_table(filename='empty.csv'):
    empty_df = pd.DataFrame()
    empty_df.to_csv(filename, index=False)
    print(f"Generated empty table in {filename}")

# Erzeuge Tabellen für Testfall 2
def create_tables_with_same_attributes():
    generate_test_data('test2_tab1.csv', 5000)
    generate_test_data('test2_tab2.csv', 5000)
    print("Generated tables with same attributes for Test 2")

# Erzeuge Tabellen für Testfall 3
def create_tables_with_partial_attributes():
    generate_test_data('test3_tab1.csv', 5000)
    
    # Für Tabelle 2 ersetzen wir 'Teilenummer' durch 'Artikelnummer'
    df2 = pd.read_csv('test3_tab1.csv')
    df2.rename(columns={'Teilenummer': 'Artikelnummer'}, inplace=True)
    df2.to_csv('test3_tab2.csv', index=False, sep=',')
    print("Generated tables with partial attributes for Test 3")

# Erzeuge unstrukturierte Tabellen für Testfall 4
def create_unstructured_tables():
    df1 = pd.DataFrame({
        'Teilenummer': np.arange(1, 1001),
        'Bezeichnung': ['Produkt_' + str(i) for i in range(1, 1001)],
        'Hoehe': np.round(np.random.uniform(0.01, 10.0, 1000), 2)
    })
    df1.to_csv('test4_tab1.csv', index=False, sep=',')

    df2 = pd.DataFrame({
        'Teilenummer': np.arange(1001, 2001),
        'Bezeichnung': ['Produkt_' + str(i) for i in range(1001, 2001)],
        'Hoehe': np.round(np.random.uniform(0.01, 10.0, 1000), 2),
        'Breite': np.round(np.random.uniform(0.01, 5.0, 1000), 2),
        'Gewicht': np.round(np.random.uniform(0.04, 40.0, 1000), 2)
    })
    df2.to_csv('test4_tab2.csv', index=False, sep=',')
    print("Generated unstructured tables for Test 4")

if __name__ == "__main__":
    # Generiere die erforderlichen Testdateien
    create_empty_table()
    create_tables_with_same_attributes()
    create_tables_with_partial_attributes()
    create_unstructured_tables()
