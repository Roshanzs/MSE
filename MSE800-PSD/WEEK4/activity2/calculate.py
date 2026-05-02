
class land:

    def calculate_area(self, length, width, height):
        return length * width * height
    
    def calculate_perimeter(self, length, width):
        return 4 * (length + width)
    
    def print_results(self, area, perimeter):
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
