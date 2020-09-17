from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates(force_decimal=False)
cc = CurrencyCodes()


class CurrencyChecks:
    def check_currency_and_amount(self, input_currency, output_currency, amount):

        try:
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
            return (
                flash(
                    "Error: Please input a number or decimal for the amount", "error"
                ),
                redirect("/"),
            )
        except Exception as err:
            print(err)
            err = str(err)
            if err == "Currency Rates Source Not Ready":
                return (
                    flash(
                        "Error: Not an acceptable currency! Please try again", "error"
                    ),
                    redirect("/"),
                )
