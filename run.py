from app import create_app

app = create_app()

# This is for Vercel
if __name__ == '__main__':
    app.run()