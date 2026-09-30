"""แสดงรายการเครื่องดื่มและคำนวณราคาตามประเภทกับขนาด"""
import storage

TITLE = "รายการน้ำคาเฟ่"


def build():
    items = storage.load()

    numbered = []
    number = 1
    for item in items:
        item["prices"] = item.get("prices", {"S": item.get("price", 0)})
        item["price"] = item["prices"].get("M", next(iter(item["prices"].values())))
        item["no"] = number
        numbered.append(item)
        number = number + 1

    return {"items": numbered, "count": len(numbered)}