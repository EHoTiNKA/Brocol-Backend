# Brokol Backend

This is the Backend part for the Web Brokol website
Created using:
- Python
- Fast api
- Unicorn
- Sqlalchemy
- Tortoise-orm

## Future plans

- Communication of orders and users.
- Create and edit restaurant dishes.
- Convenient id search, getting a list of users and a list of dishes.

## Installation

To transfer the project to yourself, follow these steps:

1. Clone the repository:

```
git clone https://github.com/your-username/Brocol-Backend.git .
```

2. Creating and running a virtual environment:

```
python -m venv env
```
```
source env/Scripts/Activate 
```
```
pip install -r requirements.txt
```

3. Run the dev version:

```
source env/Scripts/Activate 
```
```
cd project/
```
```
uvicorn app.main:app --reload  
```


## Contributing

If you want to contribute to the BrokolBackend, you can:

- Suggest a better implementation of the many to many appeal.
