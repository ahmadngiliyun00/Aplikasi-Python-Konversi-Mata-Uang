from flask import Flask, render_template, request

app = Flask(__name__)

# Kurs tetap
exchange_rates = {
    'usd': 0.000067,
    'eur': 0.000061,
    'jpy': 0.010
}

currency_names = {
    'usd': 'USD',
    'eur': 'EUR',
    'jpy': 'JPY'
}

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    currency_name = ""

    if request.method == 'POST':
        amount = float(request.form['amount'])
        currency = request.form['currency']

        # Hitung konversi
        rate = exchange_rates[currency]
        result = amount * rate
        currency_name = currency_names[currency]

    return render_template('index.html', result=result, currency_name=currency_name)

if __name__ == '__main__':
    app.run(debug=True)
