import sys

def cake_calculator(flour: int, sugar: int) -> list:
    """
    Calculates the maximum number of cakes that can be made and the leftover ingredients.
    Each cake requires:
    - 100 grams of flour
    - 50 grams of sugar
    
    Args:
        flour: Amount of available flour in grams (must be positive integer)
        sugar: Amount of available sugar in grams (must be positive integer)
        
    Returns:
        List containing three integers:
        [0] - Number of cakes that can be made
        [1] - Leftover flour in grams
        [2] - Leftover sugar in grams
        
    Raises:
        ValueError: If either input is negative
    """
    # Recipe requirements per cake
    flour_needed_per_cake = 100
    sugar_needed_per_cake = 50

    # Validate inputs
    if flour < 0 or sugar < 0:
        raise ValueError("Inputs must be non-negative integers")

    # Calculate maximum possible cakes from each ingredient
    cakes_from_flour = flour // flour_needed_per_cake
    cakes_from_sugar = sugar // sugar_needed_per_cake
    
    # The limiting factor is the ingredient we have least of (in cake portions)
    num_cakes = min(cakes_from_flour, cakes_from_sugar)
    
    # Handle case where we can't make any cakes
    if num_cakes == 0:
        return [0, flour, sugar]  # Return original amounts
    
    # Calculate remaining ingredients after making cakes
    flour_left = flour % flour_needed_per_cake
    sugar_left = sugar % sugar_needed_per_cake
    
    return [num_cakes, flour_left, sugar_left]

if __name__ == "__main__":
    try:
        print("Cake Calculator")
        print("---------------")
        print("Each cake requires 100g flour and 50g sugar")
        
        # Get user input with clear prompts
        flour = int(input("Enter flour amount (grams): ").strip())
        sugar = int(input("Enter sugar amount (grams): ").strip())
        
        # Calculate and display results
        cakes, flour_left, sugar_left = cake_calculator(flour, sugar)
        
        print("\nResults:")
        if cakes == 0:
            print("- Cannot make any cakes (need at least 100g flour and 50g sugar)")
        print(f"- Cakes you can make: {cakes}")
        print(f"- Leftover flour: {flour_left}g")
        print(f"- Leftover sugar: {sugar_left}g")
        
    except ValueError as e:
        print(f"\nError: {e}", file=sys.stderr)
        print("Please enter valid whole numbers (e.g. 500)", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}", file=sys.stderr)
        sys.exit(1)
