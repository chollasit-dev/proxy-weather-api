from app import DevelopmentConfig, Flask, create_app

app: Flask = create_app(DevelopmentConfig)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=6969, debug=True)
