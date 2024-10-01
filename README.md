# Django Base64 Encoding and Decoding Project

This Django project implements a program to encode any payload into a base64 value using a salt key and salt index. The program also decodes the encoded payload using the same salt key and salt index, ensuring that if an incorrect salt key or salt index is provided during decoding, the payload does not decode properly.

## Getting Started

These instructions will guide you through setting up and running the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django

### Installing

1. Clone the repository to your local machine.

    ```sh
    git clone https://github.com/hdr105/python-encode-decode.git
    ```

2. Navigate to the project directory.

    ```sh
    cd encode_decode
    ```


### Running the Server

To run the server, use the following command:

```sh
python manage.py runserver
