from flask import Flask, render_template, request

app = Flask(__name__)

menu = {
    'tatapunch': 613000,
    'hyundaicreta' : 2200000,
    'marutifronx' : 1300000,
    'mahindra thar' : 1700000,
    'Audi' : 4400000,
    'BMW': 7400000,
    'Honda' : 6300000,
    'landrover' : 10000000,
    'Kia' : 1100000,
    'ferrari': 30000000,
    'lamborghini' : 300000000,
}

@app.route('/')
def home():
    return render_template('index.html', menu=menu)

@app.route('/order', methods=['POST'])
def order():
    item_1 = request.form['car1'].lower()
    item_2 = request.form['car2'].lower() if 'car2' in request.form else None

    order_total = 0
    if item_1 in menu:
        order_total += menu[item_1]
    if item_2 in menu:
        order_total += menu[item_2]
    return f"Total cost of your order: {order_total}"

if __name__ == "__main__":
    app.run(debug=True)
