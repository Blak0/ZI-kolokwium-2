from dataclasses import dataclass

class Entity:
    "Class to use as interface for all entities"

class FromDict:
    @classmethod
    def from_dict(cls, d):
        return cls(**d)


@dataclass
class Customer(Entity, FromDict):
    customerNumber: int
    customerName: str
    contactLastName: str
    contactFirstName: str
    phone: str
    addressLine1: str
    addressLine2: str
    city: str
    state: str
    postalCode: str
    country: str
    salesRepEmployeeNumber: int
    creditLimit: float


@dataclass
class Order(Entity, FromDict):
    orderNumber: int
    customerNumber: int
    orderDate: str
    requiredDate: str
    shippedDate: str
    status: str
    comments: str


@dataclass
class OrderDetails(Entity, FromDict):
    orderNumber: int
    productCode: str
    quantityOrdered: int
    priceEach: float
    orderLineNumber: int


@dataclass
class Payment(Entity, FromDict):
    customerNumber: int
    checkNumber: int
    paymentDate: str
    amount: float