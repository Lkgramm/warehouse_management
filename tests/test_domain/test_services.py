import pytest
from domain.models import Product, Customer
from domain.services import WarehouseService
from infrastructure.repositories import SqlAlchemyProductRepository, SqlAlchemyCustomerRepository
from infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from sqlalchemy.orm import Session

def test_create_product(session: Session):
    product_repo = SqlAlchemyProductRepository(session)
    customer_repo = SqlAlchemyCustomerRepository(session)
    service = WarehouseService(product_repo, customer_repo)
    with SqlAlchemyUnitOfWork(session):
        product = service.create_product("Laptop", 10, 1500.0)
        assert product.id is not None
        assert product.name == "Laptop"

def test_create_customer(session: Session):
    product_repo = SqlAlchemyProductRepository(session)
    customer_repo = SqlAlchemyCustomerRepository(session)
    service = WarehouseService(product_repo, customer_repo)
    with SqlAlchemyUnitOfWork(session):
        customer = service.create_customer("Alice", "alice@example.com")
        assert customer.id is not None
        assert customer.name == "Alice"