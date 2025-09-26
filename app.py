from flask import Flask, render_template, request, redirect, url_for
import datetime
import itertools

app = Flask(__name__)

# ====== MENU DATABASE ======
menu = {
    "Breakfast": {
        "Idly": 30,
        "Medu Vada": 35,
        "Ambule": 30
    },
    "Beverages": {
        "Tea Full": 10,
        "Tea Half": 5,
        "Coffee": 20,
        "Black Tea": 10,
        "Water 1L": 20,
        "Water 500ml": 10,
        "Sprite 1L": 40,
        "Sprite 250ml": 20,
        "Cola 1L": 40,
        "Cola 250ml": 20
    }
}

order_counter = itertools.count(1001)   # auto-order IDs

# ====== ROUTES ======

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Order processing
        order_id = next(order_counter)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cart = []

        for category, items in menu.items():
            for item, price in items.items():
                qty = request.form.get(item)
                if qty and qty.isdigit() and int(qty) > 0:
                    qty = int(qty)
                    line_total = qty * price
                    cart.append((item, qty, price, line_total))

        grand_total = sum([c[3] for c in cart])

        return render_template("bill.html", order_id=order_id, 
                               timestamp=timestamp, cart=cart, 
                               grand_total=grand_total)

    return render_template("index.html", menu=menu)

# ====== MAIN RUN ======
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
