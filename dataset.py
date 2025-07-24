import pandas as pd
import random

companies = [f"Company_{i}" for i in range(1, 101)]
industries = ['Tech', 'Automotive', 'Retail', 'Healthcare', 'Finance']
states = ['New York', 'California', 'Florida', 'Texas']
years = list(range(2015, 2026))

data = []

for company in companies:
    industry = random.choice(industries)
    state = random.choice(states)
    base_rd = random.randint(20000, 150000)
    base_admin = random.randint(30000, 200000)
    base_marketing = random.randint(20000, 500000)
    growth = random.uniform(0.95, 1.12)  # some decline, some fast growth

    for year in years:
        rd = int(base_rd * (growth ** (year - 2015)))
        admin = int(base_admin * (growth ** (year - 2015)))
        marketing = int(base_marketing * (growth ** (year - 2015)))
        profit = (0.7 * rd) + (0.15 * admin) + (0.1 * marketing) + random.randint(-8000, 15000)
        data.append([company, industry, state, year, rd, admin, marketing, profit])

df = pd.DataFrame(data, columns=[
    'Company Name', 'Industry', 'State', 'Year',
    'R&D Spend', 'Administration', 'Marketing Spend', 'Profit'
])
df.to_csv('Advanced_Company_Data.csv', index=False)
print("✅ Advanced Dataset Created!")
