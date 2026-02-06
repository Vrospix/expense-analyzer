import matplotlib.pyplot as plt

def plot_category_summary(summary):
    summary.plot(kind='bar')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()

def plot_monthly_trend(monthly):
    monthly.plot(marker='o')
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()