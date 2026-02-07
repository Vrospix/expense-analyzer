def detect_anomalies(monthly, threshold=1.5):
    mean = monthly.mean()
    std = monthly.std()
    anomalies = monthly[(monthly > mean + threshold * std) |
                        (monthly < mean - threshold * std)]
    return anomalies