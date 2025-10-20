//
def main():
    print("=" * 50)
    print("Price Calculator with Tiered Pricing")
    print("=" * 50)
    
    try:
        quantity = int(input("\nEnter the quantity of items: "))
        
        if quantity < 0:
            print("Error: Quantity cannot be negative.")
            return
        
        if quantity >= 1000:
            unit_price = 3.00
        else:
            unit_price = 5.00
        
        extended_price = quantity * unit_price
        tax = extended_price * 0.07
        total = extended_price + tax
        
        print("\n" + "=" * 50)
        print("CALCULATION RESULTS")
        print("=" * 50)
        print(f"Quantity:        {quantity:,}")
        print(f"Unit Price:      ${unit_price:.2f}")
        print(f"Extended Price:  ${extended_price:,.2f}")
        print(f"Tax (7%):        ${tax:,.2f}")
        print(f"Total:           ${total:,.2f}")
        print("=" * 50)
        
    except ValueError:
        print("Error: Please enter a valid number.")
if __name__ == "__main__":
    main()
