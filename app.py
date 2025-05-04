from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    try:
        assets = float(request.form["assets"])
        turnover = float(request.form["turnover"])
        sd = float(request.form["sd"])
        sharpe = float(request.form["sharpe"])
        return1yr = float(request.form["return1yr"])
        return5yr = float(request.form["return5yr"])
        return10yr = float(request.form["return10yr"])
        expense = float(request.form["expense"])
        star_rating = request.form["star_rating"]

        # Ordinal encode inputs manually
        market_cap_dict = {"Small": 0, "Mid-Cap": 1, "Large": 2}
        fund_type_dict = {"Value": 0, "Growth": 1}
        risk_dict = {"Low": 0, "Average": 1, "High": 2}
        star_dict = {"One": 0, "Two": 1, "Three": 2, "Four": 3, "Five": 4}

        star_val = star_dict[star_rating]
        best_return = -np.inf
        best_combo = ()

        for market_cap, mval in market_cap_dict.items():
            for fund_type, fval in fund_type_dict.items():
                for risk, rval in risk_dict.items():
                    input_data = np.array(
                        [
                            [
                                mval,
                                fval,
                                rval,
                                assets,
                                turnover,
                                sd,
                                sharpe,
                                return1yr,
                                return5yr,
                                return10yr,
                                expense,
                                star_val,
                            ]
                        ]
                    )
                    predicted_return = model.predict(input_data)[0]
                    if predicted_return > best_return:
                        best_return = predicted_return
                        best_combo = (market_cap, fund_type, risk)

        result = f"Best combo: Market Cap = {best_combo[0]}, Fund Type = {best_combo[1]}, Risk = {best_combo[2]} ➤ Predicted 3Yr Return = {best_return:.2f}%"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
