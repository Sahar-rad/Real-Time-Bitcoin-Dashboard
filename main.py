# Import required libraries
try:
    from azure.eventhub import EventHubProducerClient, EventData
except ImportError:
    !pip install azure-eventhub --quiet
    from azure.eventhub import EventHubProducerClient, EventData
import requests

# API Information (Add your API Key and Base URL here)
API_KEY = "YOUR_API_KEY"  # Replace with your actual API Key
BASE_URL = "https://rest.coinapi.io/v1/exchangerate"
crypto = "BTC"
fiat = "USD"

# Event Hub Information (Add your Event Hub Connection String and Name here)
EVENT_HUB_CONNECTION_STRING = "YOUR_EVENT_HUB_CONNECTION_STRING"  # Replace with your Event Hub connection string
EVENT_HUB_NAME = "YOUR_EVENT_HUB_NAME"  # Replace with your Event Hub name

# Function to get data from the API
def get_api_data(base_url, api_key, crypto, fiat):
    try:
        url = f"{base_url}/{crypto}/{fiat}"
        headers = {"X-CoinAPI-Key": api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return {"crypto": crypto, "rate": data["rate"], "fiat": fiat}
        else:
            print(f"Error fetching data from API: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to send data to Event Hub
def send_to_event_hub(data):
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STRING,
        eventhub_name=EVENT_HUB_NAME
    )
    try:
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData(str(data)))  # Convert data to string
        producer.send_batch(event_data_batch)
        print(f"Data sent successfully! Data: {data}")
    except Exception as e:
        print(f"Error sending data to Event Hub: {e}")
    finally:
        producer.close()

# Main function to fetch data and send to Event Hub
if __name__ == "__main__":
    # Fetch API data
    api_data = get_api_data(BASE_URL, API_KEY, crypto, fiat)
    # Send data to Event Hub
    if api_data:
        send_to_event_hub(api_data)
