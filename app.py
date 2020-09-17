from flask import Flask, request, render_template, redirect, session, jsonify, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
from currency import CurrencyChecks

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"
c = CurrencyRates(force_decimal=False)
cc = CurrencyCodes()


@app.route("/",)
def home_page():
    """Displays the homepage for the currency converter"""

    return render_template("home.html")


@app.route("/result", methods=["POST"])
def display_results():
    input_currency = request.form["inputcurrency"]
    output_currency = request.form["outputcurrency"]

    try:
        amount = float(request.form["amount"])

        input_symbol = cc.get_symbol(input_currency)
        output_symbol = cc.get_symbol(output_currency)
        input_name = cc.get_currency_name(input_currency)
        output_name = cc.get_currency_name(output_currency)

        converted = c.convert(input_currency, output_currency, amount)
        converted = format(converted, ".2f")
        amount = format(amount, ".2f")

        return render_template(
            "results.html",
            amount=amount,
            converted=converted,
            input_symbol=input_symbol,
            output_symbol=output_symbol,
            input_name=input_name,
            output_name=output_name,
        )
    except ValueError:
        flash("Error: Please input a number or decimal for the amount", "error")
        return redirect("/")
    except Exception as err:
        print(err)
        err = str(err)
        if err == "Currency Rates Source Not Ready":
            flash("Error: Not an acceptable currency! Please try again", "error")
        return redirect("/")
