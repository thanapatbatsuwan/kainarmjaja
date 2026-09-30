"""แสดงรายละเอียดเครื่องดื่มที่เลือกจาก data.json"""
import models
import storage

TITLE = "รายละเอียด"


def build(query):
    items = storage.load()
    if len(items) == 0:
        return {"item": None, "index": 0, "count": 0}

    if "i" not in query:
        return {"item": None, "items": items, "list_mode": True}

    # ?i=2 in the URL selects the third item; missing or invalid input uses 0.
    index = 0
    if "i" in query and query["i"].isdigit():
        index = int(query["i"])
    if index >= len(items):
        index = len(items) - 1

    row = items[index]
    sizes = row.get("prices", {"M": row.get("price", 0)})
    size = query.get("size", "M").upper()
    if size not in sizes:
        size = "M" if "M" in sizes else next(iter(sizes))
    price = sizes[size]
    item = models.Item(row["name"], price, row.get("category", ""), size, sizes)
    pictures = {
        "เอสเพรสโซ": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=800&q=80", "ลาเต้": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?auto=format&fit=crop&w=800&q=80", "คาปูชิโน": "https://images.unsplash.com/photo-1534778101976-62847782c213?auto=format&fit=crop&w=800&q=80",
        "ชานมไทย": "https://images.unsplash.com/photo-1558857563-b371033873b8?auto=format&fit=crop&w=800&q=80", "ชามะนาวโซดา": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=800&q=80", "นมช็อกโกแลต": "https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=800&q=80",
        "อเมริกาโน": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=800&q=80", "มอคค่า": "/static/img/mocha.jpg", "คาราเมลมัคคิอาโต": "https://images.unsplash.com/photo-1512568400610-62da28bc8a13?auto=format&fit=crop&w=800&q=80",
        "กาแฟเย็น": "/static/img/iced-coffee.png", "โกโก้เย็น": "/static/img/iced-cocoa.jpg", "โกโก้ร้อน": "https://images.unsplash.com/photo-1517578239113-b03992dcdd25?auto=format&fit=crop&w=800&q=80",
        "ชาเขียวมัทฉะ": "https://images.unsplash.com/photo-1515823064-d6e0c04616a7?auto=format&fit=crop&w=800&q=80", "ชาเขียวมะนาว": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&w=800&q=80", "ชาดำเย็น": "/static/img/black-tea.jpg",
        "ชาพีช": "/static/img/peach-tea.webp", "ชาสตรอว์เบอร์รี": "https://images.unsplash.com/photo-1576092768241-dec231879fc3?auto=format&fit=crop&w=800&q=80", "นมสดเย็น": "https://images.unsplash.com/photo-1553787499-6f9133860278?auto=format&fit=crop&w=800&q=80",
        "นมสดคาราเมล": "/static/img/caramel-milk.jpg", "นมชมพู": "/static/img/pink-milk.webp", "นมเผือก": "/static/img/taro-milk.webp",
        "นมกล้วย": "/static/img/banana-milk.png", "สมูทตีสตรอว์เบอร์รี": "https://images.unsplash.com/photo-1553530666-ba11a7da3888?auto=format&fit=crop&w=800&q=80", "สมูทตีมะม่วง": "https://images.unsplash.com/photo-1623065422902-30a2d299bbe4?auto=format&fit=crop&w=800&q=80",
        "สมูทตีกล้วย": "/static/img/banana-smoothie.png",
    }
    category_pictures = {
        "กาแฟ": pictures["ลาเต้"],
        "ชา": pictures["ชานมไทย"],
        "นม": pictures["นมช็อกโกแลต"],
        "โกโก้": pictures["นมช็อกโกแลต"],
        "ผลไม้": pictures["ชามะนาวโซดา"],
        "โซดา": pictures["ชามะนาวโซดา"],
        "สมูทตี": pictures["ชามะนาวโซดา"],
    }

    return {
        "item": dict(row, size=size, price=price, prices=sizes),
        "picture": pictures.get(row["name"], category_pictures.get(row.get("category"), pictures["เอสเพรสโซ"])),
        "sentence": item.describe(),                     # the class does the talking
        "index": index,
        "prev": index - 1 if index > 0 else None,
        "next": index + 1 if index < len(items) - 1 else None,
        "count": len(items),
    }
