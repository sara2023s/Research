from ticket import TicketSystem

# Create some tickets
TicketSystem.submit_ticket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
TicketSystem.submit_ticket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
TicketSystem.submit_ticket("JOHNS", "John", "john@whitecliffe.co.nz", "Password Change")

# Display the ticket statistics
created, resolved, open = TicketSystem.get_ticket_statistics()
print(f"Tickets Created: {created}\nTickets Resolved: {resolved}\nTickets To Solve: {open}\n")

# Resolve the tickets
TicketSystem.resolve_ticket(2001)
TicketSystem.resolve_ticket(2003)

# Display ticket information and statistics after resolving them
TicketSystem.print_all_tickets()
created, resolved, open = TicketSystem.get_ticket_statistics()
print(f"\nTickets Created: {created}\nTickets Resolved: {resolved}\nTickets To Solve: {open}\n")

# Reopen a ticket and provide a response to it
TicketSystem.reopen_ticket(2001)
TicketSystem.provide_response(2001, "The monitor has been replaced.")

# Display ticket information and statistics after reopening and providing a response
TicketSystem.print_all_tickets()
created, resolved, open = TicketSystem.get_ticket_statistics()
print(f"\nTickets Created: {created}\nTickets Resolved: {resolved}\nTickets To Solve: {open}\n")