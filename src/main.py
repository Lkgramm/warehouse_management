from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

from domain.models import Customer, Order, Product
from domain.services import WarehouseService
from infrastructure.database import DATABASE_URL
from infrastructure.orm import Base, CustomerORM, OrderORM, ProductORM
from infrastructure.repositories import (SqlAlchemyCustomerRepository,
                                         SqlAlchemyOrderRepository,
                                         SqlAlchemyProductRepository)
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def main():
    session = SessionFactory()
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)
    customer_repo = SqlAlchemyCustomerRepository(session)

    uow = SqlAlchemyUnitOfWork(session)
    warehouse_service = WarehouseService(product_repo, order_repo, customer_repo)

    print("Welcome to Warehouse Management System!")
    while True:
        print("\nChoose operation:")
        print("1 - Add product")
        print("2 - Add order")
        print("3 - Add customer")
        print("4 - Get customers list")
        print("5 - Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Product name: ").strip()
            if not name:
                print("Product name cannot be empty.")
                continue

            try:
                quantity = int(input("Product quantity: "))
                price = float(input("Product price: "))
            except ValueError:
                print("Invalid input. Quantity and price must be numbers.")
                continue

            if quantity <= 0 or price <= 0:
                print("Quantity and price must be positive.")
                continue

            new_product = warehouse_service.create_product(name=name, quantity=quantity, price=price)
            uow.commit()
            print(f"Product created: {new_product}")

        elif choice == "2":
            ids_input = input("Enter product IDs separated by commas: ")
            product_ids = [id.strip() for id in ids_input.split(",") if id.strip()]
            products = []

            for pid in product_ids:
                try:
                    product = warehouse_service.get_product(int(pid))
                    products.append(product)
                except (ValueError, NoResultFound):
                    print(f"Product with ID {pid} not found. Skipping...")

            if not products:
                print("No valid products selected. Cannot create an empty order.")
                continue

            new_order = warehouse_service.create_order(products=products)
            uow.commit()
            print(f"Order created: {new_order}")

        elif choice == "3":
            customer_name = input("Customer name:")
            order_ids = input("Order ids (separate by comma):")
            orders = []
            for order_id in order_ids.split(","):
                orders.append(warehouse_service.get_order(order_id=int(order_id)))

            new_customer = warehouse_service.create_customer(
                name=customer_name, orders=orders
            )
            uow.commit()
            print(f"New customer created: {new_customer}")
            continue

        elif choice == "4":
            customers = warehouse_service.get_customers_list()
            if not customers:
                print("No customers found.")
                continue

            for customer in customers:
                print(customer)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
