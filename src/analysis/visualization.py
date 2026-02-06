import matplotlib.pyplot as plt

def plot_category_summary(summary):
    summary.plot(kind='bar')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()