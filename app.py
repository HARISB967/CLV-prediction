from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def clv_analysis():
    # Load the CLV predictions from the CSV file
    clv_csv = pd.read_csv('clv_predictions.csv')

    # Load the actual credit points from the CSV file
    actual_csv = pd.read_csv('monthly_credit_points.csv')

    # Extract data for line chart
    clv_data = {
        'dates': clv_csv['Month'].tolist(),
        'clv_values': clv_csv['Predicted_Credit_Points'].tolist()
    }
    
    actual_data = {
        'dates': actual_csv['Month'].tolist(),
        'actual_values': actual_csv['Credit_Points'].tolist()
    }

    # Convert the CLV predictions data to a list of dictionaries for rendering in the table
    table_data = clv_csv.to_dict(orient='records')

    return render_template('index.html', 
                           clv_data=table_data,
                           clv_csv=clv_data,
                           actual_csv=actual_data)

if __name__ == '__main__':
    app.run(debug=True)
