from src.domain.customer.Customer import Customer
from src.domain.customer.Customers import Customers
from src.domain.menu.MainMenu import MainMenu

customer_service = Customers.get_instance()
main_menu = MainMenu.get_instance()

for i in range(20):
    customer_service.add_customer(customer_service.add_customer(Customer("test" + str(i), "test" + str(i), i+10,i+15)))

while True:
    main_menu.print_menu()
