# 🚀 Clairsense Regional Backend API 🎉

## Setup & Run 🏃‍♂️

To set this baby up:

If you don't have one yet, set up a .env file with your configuration.  For a basic version for local testing use:  
```bash
cp dot-env-template .env
```
Be aware that .env is *excluded from git* because it contains secrets, API keys and so on.  **Never put your .env file into git.**

Then build and start the test/debug stack with:
```bash
docker-compose up --build
```

Then:
- Visit http://localhost:4000/docs for the interactive API docs (Swagger). For initial super-username and password to first authenticate see your **.env** file.
- Modify your code, which is linked into the *fastapi-app* container and watch uvicorn auto-restart your app when changes have been made.
- Run pytest in your container with `docker exec fastapi-app bash ./test.sh [optional parameters]`
- Visit http://localhost:5050/ for the PostgreSQL administrator. Upon first use you'll need to register your DB server using your **.env** file.



## Database Migration with Alembic 🗂️

To force a new table generation based on the new data models, you need to create a new Alembic migration script and apply it. Here are the steps:

1. **Access the Docker Container Terminal**:
   Before generating a new Alembic migration script, you need to access the terminal of the Docker container running your FastAPI application. Use the following command:
   ```bash
   docker exec -it fastapi-app /bin/bash
   ```
   This will give you a command line inside the `fastapi-app` container.

2. **Generate a New Alembic Migration Script**:
   Inside the Docker container, run the following command:
   ```bash
   alembic revision --autogenerate -m "description of your changes"
   ```
   This command will create a new migration script in your `alembic/versions` directory. The script will contain the changes detected in your models.

3. **Review the Generated Script**:
   Make sure the changes in the newly generated script reflect what you expect. The script will have two main functions: `upgrade()` and `downgrade()`. The `upgrade()` function applies the changes to the database, while the `downgrade()` function reverts them.

4. **Apply the Migration**:
   Still inside the Docker container, run the following command to apply the migration:
   ```bash
   alembic upgrade head
   ```

After completing these steps, you can exit the Docker container terminal by typing `exit`.