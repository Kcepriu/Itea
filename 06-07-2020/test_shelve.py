import shelve


SHELVE_FILE = 'SHELVE_DB'
counties = shelve.open(SHELVE_FILE)

# counties['Ukraine'] = 'Kiyiv'
print(tuple(counties.items()))

counties.close()


