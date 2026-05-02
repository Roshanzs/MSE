import calculate

def main():
    land_calculator = calculate.land()
    
    length = float(input("Enter the length of the land: "))
    width = float(input("Enter the width of the land: "))
    height = float(input("Enter the height of the land: "))
    
    area = land_calculator.calculate_area(length, width, height)
    perimeter = land_calculator.calculate_perimeter(length, width)
    
    land_calculator.print_results(area, perimeter)

if __name__ == "__main__":
    main()