def show_menu():
    print("\n AMAZON PRIME")
    print("select a genre: ")
    print("1. Historical")
    print("2. Horror")
    print("3. SCFI")

def get_genre():
    genre = input("\nOption: ")
    return genre

def recommend_content(genre):
    if genre == "1":
        print("T-34")
        print("last tigger") 
        print("KV1: Soul Iron")
    elif genre == "2":   
        print("IT") 
        print("SAW") 
        print("terrifier")
    elif genre == "3":
        print("Spider-Noir") 
        print("thr boys") 
        print("in Time")
    else:
        print("Invalid option.")

def rate_content():
    rating = input("CRate the content (1-5): ")
    if rating >= "1" and rating <= "5":
        print("Thanks! you gave it a " + rating + "/5")
    else:
        print("invalid rating.")

def main():
    while True:
        show_menu()
        genre = get_genre()

        print("\nRecommendations:")
        recommend_content(genre)

        rate_content()

        again = input ("\nSearch another genre? (Y/N): ")
        if again.upper() !="Y":
            print("Goodbye!")
            break
if __name__=="__main__":
    main()
