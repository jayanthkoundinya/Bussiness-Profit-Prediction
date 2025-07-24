from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('profit_predictor.pkl')
df = pd.read_csv('Advanced_Company_Data.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_df = pd.DataFrame([[
        data['rd'], data['admin'], data['marketing'], data['state'], data['industry']
    ]], columns=['R&D Spend', 'Administration', 'Marketing Spend', 'State', 'Industry'])
    prediction = round(model.predict(input_df)[0], 2)
    return jsonify({'predicted_profit': prediction})

@app.route('/trend/<company_name>')
def trend(company_name):
    company_data = df[df['Company Name'] == company_name].sort_values(by='Year')
    if company_data.empty:
        return jsonify({'error': 'No data found'})
    return jsonify({
        'years': company_data['Year'].tolist(),
        'profits': company_data['Profit'].tolist()
    })

@app.route('/top_companies/<int:year>')
def top_companies(year):
    top10 = df[df['Year'] == year].sort_values(by='Profit', ascending=False).head(10)
    return jsonify(top10.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
