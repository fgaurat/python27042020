

if __name__ == "__main__":
    try:
        x = int(input("Please enter a number for x: "))
        y = int(input("Please enter a number for y: "))
        if y == 12:
            raise ValueError("Division par 12")


        print(x,y,x/y)
    except ValueError as e:
        print("ValueError",e)
    except Exception as e:
        print(e)
        print("erreur")
    finally:
        print("finally")

    