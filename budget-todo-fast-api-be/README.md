- Create virtual environment
    - python -m venv venv
- Activate virtual environment
    - source venv/bin/activate (MacOS)
    - source venv/Scripts/activate (Windows)
- Install dependencies
    - pip install -r requirements.txt

- Run the application
    - uvicorn main:app --reload


DOCKER: 
- Run docker composer:
    Note: Start the docker desktop before running the below command and stop mysql server manually if already install MySQL service in your local.
    - docker-compose up --build 
    (or) 
    - sudo docker-compose up --build
- To run mysql server if you run docker 
    - docker exec -it <container_name_or_id> mysql -u <user> -p