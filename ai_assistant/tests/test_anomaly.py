

from services.anomaly_service import AnomalyService

service = AnomalyService()

print("Long Resolution")
print(service.long_resolution_time().shape)

print("Slow Response")
print(service.slow_response_time().shape)

print("Old Unresolved")
print(service.old_unresolved_high_priority().shape)

print("Low Rating")
print(service.low_customer_rating().shape)