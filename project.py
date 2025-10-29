# Pay-per-Use Cloud Cost Estimator
# Supports SDG 12 - Responsible Consumption and Production

# Sample pricing data (USD per unit)
cloud_pricing = {
    "AWS": {
        "compute_per_hour": 0.045,
        "storage_per_gb": 0.023,
        "bandwidth_per_gb": 0.09,
    },
    "Azure": {
        "compute_per_hour": 0.05,
        "storage_per_gb": 0.02,
        "bandwidth_per_gb": 0.085,
    },
    "GCP": {
        "compute_per_hour": 0.043,
        "storage_per_gb": 0.021,
        "bandwidth_per_gb": 0.08,
    }
}

def estimate_cost(provider, compute_hours, storage_gb, bandwidth_gb):
    """Estimate total cloud cost for a given provider."""
    p = cloud_pricing[provider]
    total_cost = (
        compute_hours * p["compute_per_hour"] +
        storage_gb * p["storage_per_gb"] +
        bandwidth_gb * p["bandwidth_per_gb"]
    )
    return round(total_cost, 2)


def compare_cloud_costs(compute_hours, storage_gb, bandwidth_gb):
    """Compare estimated costs across multiple cloud providers."""
    print("\n--- Pay-per-Use Cloud Cost Estimator ---")
    print(f"Usage: {compute_hours} compute hrs, {storage_gb}GB storage, {bandwidth_gb}GB bandwidth\n")

    estimates = {}
    for provider in cloud_pricing.keys():
        cost = estimate_cost(provider, compute_hours, storage_gb, bandwidth_gb)
        estimates[provider] = cost
        print(f"{provider:<10} → Estimated Cost: ${cost}")

    best_provider = min(estimates, key=estimates.get)
    print(f"\n✅ Best Option: {best_provider} (Lowest Cost: ${estimates[best_provider]})")
    return estimates


# Example user input
if __name__ == "__main__":
    compute_hours = float(input("Enter compute hours used: "))
    storage_gb = float(input("Enter storage used (GB): "))
    bandwidth_gb = float(input("Enter bandwidth used (GB): "))

    compare_cloud_costs(compute_hours, storage_gb, bandwidth_gb)
