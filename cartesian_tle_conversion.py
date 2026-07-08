
"""take in a tle"""
def elements_from_tle(file):
    tot = open(file)
    print(tot.read())

if __name__ == "__main__":
    elements_from_tle(r"C:\Users\Cecilie.Bamer\Documents\NUSTAR.txt")