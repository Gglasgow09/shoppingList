from models import ShoppingList
from app import Session

session = Session()

def add_shopping_item(name, quantity, user_id):
    if not name:
        print("Name is required")
        return
    
    if not isinstance(quantity, int) or quantity < 0:
        print("Quantity must be a whole non-negative number.")
        return
    
    existing_item = session.query(ShoppingList).filter_by(name=name, user_id=user_id).first()
    if existing_item is None:
        shopping_list_item = ShoppingList(name=name, quantity=quantity, user_id=user_id)
        session.add(shopping_list_item)
        session.commit()
        print(f"Item '{name}' added successfully.")
    else:
        print(f"An item by the name '{name}' already exists for this user.")

def update_item(item_id, new_name):
    if not new_name:
        print("Item name cannot be left blank.")
        return

    item = session.query(ShoppingList).filter_by(id=item_id).first()
    if item:
        item.name = new_name
        session.commit()
        print(f"Item ID '{item_id}' updated successfully.")
    else:
        print(f"Item ID '{item_id}' not found.")

def update_quantity(item_id, new_quantity):
    if not isinstance(new_quantity, int) or new_quantity < 0:
        print("Quantity must be a whole non-negative number.")
        return

    item = session.query(ShoppingList).filter_by(id=item_id).first()
    if item:
        item.quantity = new_quantity
        session.commit()
        print(f"Quantity for item ID '{item_id}' updated successfully.")
    else:
        print(f"Item ID '{item_id}' not found.")
