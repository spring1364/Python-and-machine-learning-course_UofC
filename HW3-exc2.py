import matplotlib.pyplot as plt
import pandas as pd

# Exc1 #############################################################
company_data = pd.read_csv('company_sales_data_matplotlib.csv')
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.set_xlabel('Month number')
ax1.set_ylabel('Total profit')
plt.title('Company profit per month')
ax1.plot(company_data['month_number'], company_data['total_profit'])

# Exc2 #############################################################
fig2, ax2 = plt.subplots(figsize=(8, 6))
plt.title('Company sales data of last year')
setting = dict(linewidth=3, marker='o', markerfacecolor='k', linestyle=':', color='r',
               label='Profit data of the last year')
ax2.set_xlabel('Month number')
ax2.set_ylabel('Sold unit numbers')
ax2.plot(company_data['month_number'], company_data['total_profit'], **setting)
lg = ax2.legend(loc=4)

# Exc3 #############################################################
fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.set_xlabel('Month number')
ax3.set_ylabel('Sales unit in number')
plt.title('Sales data')
setting1 = dict(linewidth=3, marker='o')
ax3.plot(company_data['month_number'], company_data['facecream'], label='Face cream sales data', **setting1)
ax3.plot(company_data['month_number'], company_data['facewash'], label='Face wash sales data', **setting1)
ax3.plot(company_data['month_number'], company_data['toothpaste'], label='Toothpaste sales data', **setting1)
ax3.plot(company_data['month_number'], company_data['bathingsoap'], label='Bathingsoap sales data', **setting1)
ax3.plot(company_data['month_number'], company_data['shampoo'], label='Shampoo sales data', **setting1)
ax3.plot(company_data['month_number'], company_data['moisturizer'], label='Moisturizer sales data', **setting1)
lg = ax3.legend(loc=2)

# Exc4 #############################################################
fig4, ax4 = plt.subplots(figsize=(8, 6))
ax4.set_xlabel('Month number')
ax4.set_ylabel('Sales unit in number')
plt.title('Tooth paste sales data')
ax4.scatter(company_data['month_number'], company_data['toothpaste'])
plt.grid(linestyle='--')

# Exc5 #############################################################
fig5, ax5 = plt.subplots(figsize=(8, 6))
ax5.set_xlabel('Month number')
ax5.set_ylabel('Sales unit in number')
plt.title('Face wash and face cream sales data')
bar_width = 0.35
ax5.bar(company_data['month_number'], company_data['facewash'], bar_width, label='Face wash sales data')
ax5.bar(company_data['month_number'] + bar_width, company_data['facecream'], bar_width, label='Face cream sales data')
plt.grid(linestyle='--')
lg = ax5.legend(loc=2)

# Exc6 #############################################################
fig6, ax6 = plt.subplots(figsize=(8, 6))
ax6.set_xlabel('Month number')
ax6.set_ylabel('Sales unit in number')
plt.title('Bathing soap sales data')
bar_width = 0.5
ax6.bar(company_data['month_number'], company_data['facewash'], bar_width)
plt.grid(linestyle='--')

# Exc7 #############################################################
fig7, ax7 = plt.subplots(figsize=(8, 6))
ax7.set_xlabel('Profit range in $')
ax7.set_ylabel('Actual profit in dollar')
plt.title('Profit data')
ax6.hist(company_data['total_profit'], bins=[150000, 200000, 250000, 300000, 350000])
plt.show()

# Exc8 #############################################################
fig8, ax8 = plt.subplots(figsize=(8, 6))
plt.title('Sales data')
ax6.pie(company_data['total_profit'])
plt.show()

