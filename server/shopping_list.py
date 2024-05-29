from models import ShoppingListItem
from app import Session 

session = Session()

def add_shopping_item(name, quantity):
    if not name:
        print("Name is required")
        return
    
    if not isinstance(quantity, int) or quantity < 0:
        print("Quanttity must be a whole non-negative number.")
    
    existing_item = session.query(ShoppingListItem).filter_by(name=name).first()
    if existing_item is None:
        shoppingListItem = ShoppingListItem(name=name) 
        session.add(shoppingListItem)
        session.commit()
    else:
        print(f"A item by the name {name} already exists.")

def update_item(item_id, new_name):
    if not isinstance(new_name):
        print("Item cannot be left blank.")

    item = session.query(ShoppingListItem).filter_by(id=item_id).first()
    if item:
        item.name = new_name
        session.commit()

        
