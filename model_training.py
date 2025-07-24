import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv('Advanced_Company_Data.csv')

X = df[['R&D Spend', 'Administration', 'Marketing Spend', 'State', 'Industry']]
y = df['Profit']

preprocessor = ColumnTransformer([
    ('encoder', OneHotEncoder(), ['State', 'Industry'])
], remainder='passthrough')

model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

model.fit(X, y)
joblib.dump(model, 'profit_predictor.pkl')

print("✅ Model trained and saved as profit_predictor.pkl")
