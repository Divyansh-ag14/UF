def main():
    
    text_file = open("world_cup_champions.txt", "r")
    #complete_text = text_file.read()
    #print(complete_text)
    lines = text_file.readlines()

    my_dict={}
    countries = []
    years = []

    for line in lines[1:]: # skip the header
        
        countries.append(line.split(",")[1])
        years.append(int((line.split(",")[0])))

    # print(countries)
    # print(years)

    for country, year in zip(countries, years):
        if country in my_dict.keys():
            my_dict[country].append(year)
        else:
            my_dict[country]= []
            my_dict[country].append(year)

    print("Country      Wins      Years")
    print("=======      ====      =====")

    for country, years in sorted(my_dict.items()):
        str_year = ", ".join(map(str, years)) #  strings are left-aligned by default
        print(f"{country:12} {str(len(years)):9} {str_year}")

    text_file.close()

    #print(my_dict.items())

if __name__ == "__main__":

    print("FIFA World Cup Winners")
    main()