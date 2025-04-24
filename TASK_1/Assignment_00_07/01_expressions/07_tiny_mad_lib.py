SENTENCE_START : str = "Panaversity is fun. I Learned to program and used python to make my "

def main():
    adjective: str = input("Enter an adjective:")
    noun: str = input("Enter a noun:")
    verb: str = input("Enter a verb:")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + ".")

if __name__ == "__main__":
    main()    