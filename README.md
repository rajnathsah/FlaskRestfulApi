# Flask RESTful Api

### Sample Flask RESTful Api example with database connectivity and basic authentication

Flask-RESTful is an extension for flask that adds supports for quickly building REST APIs.

1. Install required depencies using 
    ```
    pip install -r requirements.txt
    ```
2. Download Postman for testing api [Postman](https://www.getpostman.com/downloads/)
3. Run sqlscript.py to create login and employee table and populate sample data.
4. Start the app by running app.py from command prompt or terminal
    ```
    python app.py
    ```
5. Open Postman and enter url http://127.0.0.1:5000/employee/api/v1.0/all, In authorization tab, select basic auth and enter username and password. Hit send button to get all the employee data.
6. To add one or more employee data enter url http://127.0.0.1:5000/employee/api/v1.0/all, In authorization tab, select basic auth and enter username and password. Under body tab, select raw and change data as JSON(application/json) and enter data in below format.
Add two employee data  
    ```
      {
          "employee": [
              {
                  "employee_name": "Rohan",            
                  "employee_sal": 10001
              },
              {
                  "employee_name": "Ram",            
                  "employee_sal": 15001
              }
          ]
      }
    ```  
7. Repeat step 5 to view data.
