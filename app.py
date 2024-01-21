from api import configure_app

app = configure_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5555)
