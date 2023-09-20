#This is the second version of the Help Desk Ticketing system.
#This version gives the user the ability to create, resolve, reopen, respond and display ticket information.
#Its very user friendly and can be used by either staff, or the IT Team.

from ticket import TicketSystem

def main():
    print("Welcome to the Help Desk Ticketing System Prototype")
    
    while True:
        print("\nOptions:")
        print("1. Create a Ticket")
        print("2. Resolve a Ticket")
        print("3. Reopen a Ticket")
        print("4. Provide Response to a Ticket")
        print("5. Display Ticket Statistics")
        print("6. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            staff_id = input("Enter Staff ID: ")
            creator_name = input("Enter Ticket Creator Name: ")
            contact_email = input("Enter Contact Email: ")
            description = input("Enter Description of the Issue: ")
            TicketSystem.submit_ticket(staff_id, creator_name, contact_email, description)
            print("The ticket has been created successfully")
        
        elif choice == '2':
            ticket_number = int(input("Enter Ticket Number to Resolve: "))
            TicketSystem.resolve_ticket(ticket_number)
            print(f"Ticket {ticket_number} resolved.")
        
        elif choice == '3':
            ticket_number = int(input("Enter Ticket Number to Reopen: "))
            TicketSystem.reopen_ticket(ticket_number)
            print(f"Ticket {ticket_number} reopened.")
        
        elif choice == '4':
            ticket_number = int(input("Enter Ticket Number to Provide Response: "))
            response = input("Enter Response: ")
            TicketSystem.provide_response(ticket_number, response)
            print(f"Response added to Ticket {ticket_number}.")
        
        elif choice == '5':
            created, resolved, open = TicketSystem.get_ticket_statistics()
            print(f"Tickets Created: {created}")
            print(f"Tickets Resolved: {resolved}")
            print(f"Tickets To Solve: {open}")
        
        elif choice == '6':
            print("Exiting the Help Desk Ticketing System.")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")

if __name__ == "__main__":
    main()

