import configparser
import json
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)


def parse_config_file(filename):
    config_data = {}
    try:
        # Parse and read config file and return the output of config file
        config = configparser.ConfigParser()
        config.read(filename)

        for section in config.sections():
            config_data[section] = {}
            for key, value in config.items(section):
                config_data[section][key] = value

    except Exception as e:
        print("Error:", e)
        config_data = None

    return config_data


def read_config_file(configuration_data):
    try:
        # Print configuration file data in defined format
        print("Configuration File Parser Results:")

        for section, values in configuration_data.items():
            print(f"\n{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")

    except Exception as e:
        print("Error: ", e)


def save_to_database(data):
    try:
        # connect with database and fetch the data
        conn = sqlite3.connect('config.db')
        cursor = conn.cursor()

        # check and create table in database
        cursor.execute("create table if not exists configs (id INTEGER PRIMARY KEY, data TEXT)")

        # insert data into database
        cursor.execute("insert into configs (data) values (?)", (json.dumps(data),))

        conn.commit()
        conn.close()

    except Exception as e:
        print("Error: ", e)


def fetch_from_database():
    try:
        # connect with database and fetch the data
        conn = sqlite3.connect('config.db')
        cursor = conn.cursor()

        cursor.execute("select data from configs order by id desc limit 1")
        result = cursor.fetchone()

        # result the data fetched from database
        if result:
            return json.loads(result[0])
        else:
            return None

    except Exception as e:
        print("Error: ", e)
        return None


@app.route('/config', methods=['GET'])
def get_config():
    try:
        # fetch saved data from database
        config_data = fetch_from_database()

        # check the data from database and return it in JSON format
        if config_data:
            return jsonify(config_data)
        else:
            return jsonify({"error": "Failed to fetch config data"}), 500

    except Exception as e:
        print("Error: ", e)


if __name__ == '__main__':
    # import config file
    config_data = parse_config_file('configfile.ini')

    # check data in config file and save it to database
    if config_data:
        read_config_file(config_data)
        save_to_database(config_data)

    # run app to receive the GET API request on port 8080
    app.run(debug=True, port=8080)
