import pandas as pd
import random

def generate_data():
    services = ["auth-service", "payment-gateway", "inventory-api", "order-processor", "notification-hub", "search-engine"]
    severities = ["Critical", "High", "Medium", "Low"]
    priorities = ["P0", "P1", "P2", "P3"]
    
    # Templates for internal defects (50)
    # Each template: (internal_desc, vendor_paraphrase)
    templates = [
        ("Redis connection pool exhausted in {service}.", "Checkout app unable to acquire session from cache in {service} due to limit reach."),
        ("Kafka consumer lag exceeding 10k messages in {service}.", "{service} processing delay: message queue backlog detected."),
        ("Auth service returning 500 on valid JWT validation.", "Internal server error during login token verification in {service}."),
        ("OOM kill detected in {service} pod on cluster node.", "Container restarted in {service} due to memory exhaustion."),
        ("Latencies above 2s on /api/v1/status endpoint in {service}.", "Slow response times for status check in {service} subsystem."),
        ("Database lock contention in {service} during peak load.", "Query timeouts in {service} backend due to database blocking."),
        ("S3 bucket permissions error in {service} file upload.", "Unable to save uploaded files in {service}: Access Denied."),
        ("Service mesh sidecar injection failing for {service}.", "Network connectivity issues in {service} pod: proxy not starting."),
        ("Stale data being served from {service} local cache.", "Consistency issue in {service}: old records appearing in results."),
        ("Circuit breaker open for {service} downstream calls.", "Requests failing to external dependency from {service}."),
    ]
    
    # Unique vendor noise templates (100)
    noise_templates = [
        "UI CSS alignment issue on {service} dashboard.",
        "Update documentation for {service} API endpoints.",
        "Minor spelling error in {service} logs.",
        "Feature request: add more logging to {service}.",
        "Slow loading of static assets in {service}.",
        "Broken link in {service} footer.",
        "Color contrast check failed for {service} UI.",
        "Duplicate headers in {service} response.",
        "Request for architectural review of {service}.",
        "Weekly performance report for {service} ready.",
    ]

    internal_records = []
    vendor_records = []
    
    # 1. Generate 50 Internal Defects and 50 Matching Vendor Defects
    for i in range(50):
        service = random.choice(services)
        template = random.choice(templates)
        
        # Internal
        internal_records.append({
            "Defect ID": f"INT-{i+1:03d}",
            "Service Name": service,
            "Severity": random.choice(severities),
            "Description": template[0].format(service=service)
        })
        
        # Vendor Match
        vendor_records.append({
            "Vendor Ticket ID": f"VEN-{i+1001:03d}",
            "Component": service,
            "Priority": random.choice(priorities),
            "Summary": template[1].format(service=service)
        })
        
    # 2. Generate 100 Unique Vendor Defects (Noise)
    for i in range(100):
        service = random.choice(services)
        vendor_records.append({
            "Vendor Ticket ID": f"VEN-{i+2001:03d}",
            "Component": service,
            "Priority": random.choice(priorities),
            "Summary": random.choice(noise_templates).format(service=service)
        })
        
    # Save to CSV
    pd.DataFrame(internal_records).to_csv("internal_defects.csv", index=False)
    pd.DataFrame(vendor_records).to_csv("vendor_defects.csv", index=False)
    print("Generated internal_defects.csv (50) and vendor_defects.csv (150)")

if __name__ == "__main__":
    generate_data()
