# Address Book Using FastAPI

    **Versions**
    ```
    > [Python](https://www.python.org/) 3.10 and above
    > [FastAPI](https://fastapi.tiangolo.com/) 0.73.0
    ```

###### EndPoints:

```
**1. GET**    <=> '/'
**2. GET**    <=> '/address/{address_id}'
**3. GET**    <=> '/address?lat={latitude}&lon={lomgitude}&distance_range={distance_in_kilometers}'
**4. POST**   <=> '/create_address'
**5. PATCH**  <=> '/address/{address_id}'
**6. DELETE** <=> '/address/{address_id}'
```

**[Find Latitude & Longitude of any Location Here](https://www.distancesto.com/coordinates.php)**

###### To run Project

```
1. git clone [https://github.com/pranavv999/FastAPI-Address-Book.git](https://github.com/pranavv999/FastAPI-Address-Book.git)
2. cd FastAPI-Address-Book
3. create [python virtual environment](https://docs.python.org/3/tutorial/venv.html) if necessary & activate.
4. Install dependancies
    > pip install -r requirements.txt
5. Start Development Server.
    > uvicorn address_book.main:app --reload
6. Open [FastAPI - Swagger UI](http://127.0.0.1:8000/docs) http://127.0.0.1:8000/docs
```
