# Easy Kafka Setup

This project provides a simple and straightforward way to set up a Kafka cluster using Docker and Docker Compose. It's designed to be easily deployed on a cloud server (like an AWS EC2 instance) or any local machine.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

*   [Docker](https://docs.docker.com/get-docker/)
*   [Docker Compose](https://docs.docker.com/compose/install/)
*   [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Rifat1493/Easy-Kafka-Setup.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd Easy-Kafka-Setup
    ```

3.  **Start the Kafka cluster:**

    ```bash
    docker-compose up --build
    ```

    This command will build the Docker images and start the Kafka and Zookeeper services.

## Usage

*   **Kafka UI:**

    Once the services are running, you can access the Kafka UI in your web browser at `http://<your-server-ip>:8080`.

*   **Python Client:**

    The `client.py` script provides a simple example of a Kafka producer and consumer. To run the client, you'll need to have the `kafka-python` library installed:

    ```bash
    pip install kafka-python
    ```

    Then, you can run the client:

    ```bash
    python client.py
    ```

    **Note:** If you are running the client from a different machine than the one hosting the Kafka cluster, make sure to configure your security groups (e.g., in AWS EC2) to allow inbound and outbound traffic on the necessary ports.

## Future Work

*   Integrate with Kubernetes (EKS) for more robust and scalable deployments.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
