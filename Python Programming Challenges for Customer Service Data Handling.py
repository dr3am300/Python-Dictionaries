# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
# Problem Statement: Develop a program that:
# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
def open_ticket(ticket_id, customer_name, issue_description):
    service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
def update_ticket_status(ticket_id, status):
    service_tickets[ticket_id]["Status"] = status
def display_tickets(status=None):
    if status:
        for ticket_id, ticket in service_tickets.items():
            if ticket["Status"] == status:
                print(ticket_id, ticket)
    else:
        for ticket_id, ticket in service_tickets.items():
            print(ticket_id, ticket)
open_ticket("Ticket003", "Charlie", "Website down")
update_ticket_status("Ticket001", "closed")
display_tickets()
display_tickets("open")
display_tickets("closed")

for ticket_id, ticket in service_tickets.items():
    print(ticket_id, ticket)
for ticket_id, ticket in service_tickets.items():
    print(ticket_id, ticket["Customer"])
for ticket_id, ticket in service_tickets.items():
    print(ticket_id, ticket["Issue"])
for ticket_id, ticket in service_tickets.items():
    print(ticket_id, ticket["Status"])
    
