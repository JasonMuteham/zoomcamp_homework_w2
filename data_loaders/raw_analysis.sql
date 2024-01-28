SELECT pickup_datetime::DATE as pickup_date, SUM(passenger_count), SUM(trip_distance), ANY_VALUE(pickup_datetime[:10]) as Date
FROM raw.green_taxi
WHERE pickup_date < '2020-10-01' or pickup_date > '2020-12-31'
GROUP BY pickup_date
