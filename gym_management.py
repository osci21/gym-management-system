# GYM MANAGEMENT SYSTEM

import pandas as pd
import matplotlib.pyplot as plt

#Load existing data
df=pd.read_csv("gym_data.csv")

while True:
    print("---------- GYM MANAGEMENT SYSTEM ----------")
    print("              1. View all members")
    print("              2. Add a new member")
    print("              3. Delete a member")
    print("              4. Modify member details")
    print("              5. Visualize data (Bar Graph)")
    print("              6. Exit")
    print("=====================================")
    
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        print("\n----- All Member Records -----")
        print(df)
    
    elif choice == 2:
        print("\n----- Add a New Member -----")
        id_no = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        weight = float(input("Enter Weight (kg): "))
        height = float(input("Enter Height (cm): "))
        mtype = input("Enter Membership Type (Gold/Silver/Platinum): ")
        fee = int(input("Enter Fee: "))

        # Create a new row
        new_row = {'ID': id_no, 'Name': name, 'Age': age, 'Weight': weight, 'Height': height, 'Membership_Type': mtype, 'Fee': fee}

        # Add it safely to dataframe
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    
    elif choice == 3:
        print("\n----- Delete Member -----")
        name = input("Enter the name of member to delete: ")
        df = df[df['Name'] != name]
        df.to_csv("gym_data.csv", index=False)
        print("Member deleted successfully!")
    
    elif choice == 4:
        print("\n----- Modify Member Details -----")
        name = input("Enter member name to modify: ")
        if name in df['Name'].values:
            print("Which detail do you want to modify?")
            print("1. Age  2. Weight  3. Height  4. Fee  5. Membership")
            ch = int(input("Enter your choice: "))
            
            if ch == 1:
                new_age = int(input("Enter new Age: "))
                df.loc[df['Name'] == name, 'Age'] = new_age
            elif ch == 2:
                new_weight = float(input("Enter new Weight: "))
                df.loc[df['Name'] == name, 'Weight'] = new_weight
            elif ch == 3:
                new_height = float(input("Enter new Height: "))
                df.loc[df['Name'] == name, 'Height'] = new_height
            elif ch == 4:
                new_fee = int(input("Enter new Fee: "))
                df.loc[df['Name'] == name, 'Fee'] = new_fee
            elif ch == 5:
                new_membership = input("Enter new Membership: ")
                df.loc[df['Name'] == name, 'Membership_Type'] = new_membership
            else:
                print("Invalid option!")
            
            df.to_csv("gym_data.csv", index=False)
            print("Details updated successfully!")
        else:
            print("Member not found!")
    
    elif choice == 5:
        print("\n----- Data Visualization -----")
        print("1. Name vs Weight")
        print("2. Name vs Fee")
        graph_choice = int(input("Enter your choice: "))
        
        if graph_choice == 1:
            plt.bar(df['Name'], df['Weight'])
            plt.xlabel("Member Name")
            plt.ylabel("Weight (kg)")
            plt.title("Member Weight Comparison")
            plt.show()
        elif graph_choice == 2:
            plt.bar(df['Name'], df['Fee'])
            plt.xlabel("Member Name")
            plt.ylabel("Fee")
            plt.title("Membership Fee Comparison")
            plt.show()
        else:
            print("Invalid choice!")
    
    elif choice == 6:
        print("Exiting program, Goodbye!")
        break
    
    else:
        print("Invalid input! Please enter between 1-6.")
