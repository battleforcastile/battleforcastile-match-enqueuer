from battleforcastile_match_enqueuer import create_app

app = create_app(config_filename='development_config.py')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3500)
