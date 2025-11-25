import sys
from clustering import selecteer_bestand_en_straal

def main():
    with open("clustering_log.txt", "a", encoding="utf-8") as f:
        f.write("Main() wordt uitgevoerd\n")
    selecteer_bestand_en_straal()

if __name__ == "__main__":
    main()