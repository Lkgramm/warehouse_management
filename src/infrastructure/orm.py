from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ProductORM(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)


class OrderORM(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)


class CustomerORM(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)


order_product_assocoations = Table(
    "order_product_assocoations",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id")),
    Column("product_id", ForeignKey("products.id")),
)

customer_order_assocoations = Table(
    "customer_order_assocoations",
    Base.metadata,
    Column("customer_id", ForeignKey("customers.id")),
    Column("order_id", ForeignKey("orders.id")),
)

OrderORM.products = relationship("ProductORM", secondary=order_product_assocoations)
CustomerORM.orders = relationship("OrderORM", secondary=customer_order_assocoations)
