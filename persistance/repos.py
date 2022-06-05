from typing import List, Mapping

from sympy import Product
from entities import *


memory_storage: Mapping[str, List[Entity]] = {
    'customers': List[Customer],
    'products': List[Product],
    'orders': List[Order],
    'order_details': List[OrderDetails]
}

def store_in_memory(key: str, values: List[Entity]):
    """
    Store entity in memory storage using key-value mapping
    """
    memory_storage[key] = values

def get_all_from_memory(key: str) -> List[Entity]:
    """
    Get all_entities from memory storage using key
    """
    return memory_storage[key]