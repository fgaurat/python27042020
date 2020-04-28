from pprint import pprint

if __name__ == "__main__":

    data = [
            ['user3','passw3','Fred','durand'],
            ['user4','passw4','Steve','durand'],
            ['user5','passw5','Michael','durand'],
            ['user6','passw6','Andrews','durand'],
            ['user7','passw7','Marcelle','durand'],
            ['user8','passw7','Cédric','durand'],
            ['user9','passw7','Yann','durand']
    ]

    with open("data.csv","w") as f:    
        for l in data:
            # s = ";".join(l)
            # s+="\n"
            s = "{};{};{};{}\n".format(*l)
            f.write(s)
    
    print("after open")
    data_in =[]
    with open("data.csv","r") as f:
        for line in f:
            line = line.strip()
            the_list = line.split(';')
            data_in.append(the_list)
            print("=>",repr(line))
    

    


    