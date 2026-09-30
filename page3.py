"""คำนวณราคาเครื่องดื่มจากรายการใน data.json"""
import storage

TITLE = "คำนวณราคาเครื่องดื่ม"


def read_number(text, default):
    """Number from the URL text, or the default when empty/garbage."""
    try:
        value = float(text)
    except ValueError:
        return default
    if value != value:                    # nan
        return default
    return value


def build(query):
    items = storage.load()
    product_index = int(read_number(query.get("product", ""), 0))
    if product_index < 0 or product_index >= len(items):
        product_index = 0

    quantity = int(read_number(query.get("quantity", ""), 1))
    if quantity < 1:
        quantity = 1

    discount = read_number(query.get("discount", ""), 0)
    if discount < 0:
        discount = 0
    if discount > 100:
        discount = 100

    product = items[product_index] if items else {"name": "ไม่มีสินค้า", "prices": {"M": 0}}
    sizes = product.get("prices", {"M": product.get("price", 0)})
    size = query.get("size", "M").upper()
    if size not in sizes:
        size = "M" if "M" in sizes else next(iter(sizes))
    product = dict(product, size=size, price=sizes[size], prices=sizes)
    subtotal = product["price"] * quantity
    discount_amount = subtotal * discount / 100
    after_discount = subtotal - discount_amount
    total = after_discount

    rows = []
    for item in items:
        item_prices = item.get("prices", {"M": item.get("price", 0)})
        rows.append({"name": item["name"], "price": item_prices.get("M", next(iter(item_prices.values()))), "prices": item_prices})

    return {
        "items": rows,
        "product_index": product_index,
        "product": product,
        "size": size,
        "quantity": quantity,
        "discount": discount,
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "after_discount": after_discount,
        "total": total,
    }
