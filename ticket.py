
class Ticket:
    counter = 2000  # Static field for ticket number counter

    def __init__(self, staff_id, ticket_creator_name, contact_email, description):
        self.ticket_number = Ticket.counter
        Ticket.counter += 1
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def generate_password(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.ticket_creator_name[:3]
            self.response = f"New password generated: {new_password}"

    def resolve_ticket(self):
        self.status = "Closed"

    def reopen_ticket(self):
        self.status = "Reopened"

    def provide_response(self, response):
        self.response = response

    def get_ticket_info(self):
        return f"Ticket Number: {self.ticket_number}\n" \
               f"Ticket Creator: {self.ticket_creator_name}\n" \
               f"Staff ID: {self.staff_id}\n" \
               f"Email Address: {self.contact_email}\n" \
               f"Description: {self.description}\n" \
               f"Response: {self.response}\n" \
               f"Ticket Status: {self.status}\n"


class TicketSystem:
    tickets = []

    @classmethod
    def submit_ticket(cls, staff_id, ticket_creator_name, contact_email, description):
        ticket = Ticket(staff_id, ticket_creator_name, contact_email, description)
        ticket.generate_password()
        cls.tickets.append(ticket)

    @classmethod
    def resolve_ticket(cls, ticket_number):
        for ticket in cls.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.resolve_ticket()

    @classmethod
    def reopen_ticket(cls, ticket_number):
        for ticket in cls.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.reopen_ticket()

    @classmethod
    def provide_response(cls, ticket_number, response):
        for ticket in cls.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.provide_response(response)

    @classmethod
    def get_ticket_statistics(cls):
        created_tickets = len(cls.tickets)
        resolved_tickets = sum(1 for ticket in cls.tickets if ticket.status == "Closed")
        open_tickets = sum(1 for ticket in cls.tickets if ticket.status == "Open")
        return created_tickets, resolved_tickets, open_tickets

    @classmethod
    def print_all_tickets(cls):
        for ticket in cls.tickets:
            print(ticket.get_ticket_info())

