## STEPS
- Create Influxdb container (source: https://docs.influxdata.com/influxdb/v2/install/use-docker-compose/)
- Create Grafana container (source: https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)
- Create Python script to make API calls to pycno servers to query sensor data.
- Create line protocol file with point data to store in bucket in influxdb (source: https://www.influxdata.com/blog/import-json-data-influxdb-using-python-go-javascript-client-libraries/)
- Connect InfluxDB as a data source to Grafana.
- Run a simple query in Grafana to visualize the data.

## Resources
- Data layout and schema for influxdb (source: https://www.influxdata.com/blog/data-layout-and-schema-design-best-practices-for-influxdb/)
