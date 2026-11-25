print("===================================")
print("       WELCOME TO FISHERNAV")
print(" Fishing Boat Safety Advisor")
print("===================================")

name = input("Enter your name: ")

print("\nHello", name)
print("Welcome to FisherNav!")

print("\nSelect an option:")
print("1. Weather Awareness")
print("2. Boat Safety Checklist")
print("3. Emergency Preparedness")
print("4. Trip Preparation")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    print("\n--- WEATHER AWARENESS ---")
    print("Check official marine weather forecasts.")
    print("Review wind and wave conditions.")
    print("Follow official marine warnings.")

elif choice == "2":
    print("\n--- BOAT SAFETY ---")
    print("1. Check life jackets.")
    print("2. Check communication equipment.")
    print("3. Check emergency supplies.")
    print("4. Check boat condition.")

elif choice == "3":
    print("\n--- EMERGENCY PREPAREDNESS ---")
    print("Keep emergency contacts available.")
    print("Know local rescue procedures.")
    print("Follow official emergency instructions.")

elif choice == "4":
    print("\n--- TRIP PREPARATION ---")
    print("Check marine weather warnings.")
    print("Review boat equipment.")
    print("Ensure the captain approves the trip.")

else:
    print("Invalid choice. Try again.")

print("\nThank you for using FisherNav!")
