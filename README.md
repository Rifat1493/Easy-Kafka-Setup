# EASY-KAFKA-SETUP



docker exec -it kafka1 bash

# Add a user called "client" with password "client-secret"
kafka-configs --bootstrap-server kafka1:19092 \
  --alter --add-config 'SCRAM-SHA-256=[password=client-secret]' \
  --entity-type users --entity-name client
