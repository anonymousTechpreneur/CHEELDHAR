import textwrap

import google.generativeai as genai
from IPython.display import Markdown

import sqlalchemy

from Python_UI_Scripts.Create_database_connection import * 

def gemini_init(key=''):
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    chat = model.start_chat(enable_automatic_function_calling=True)
    return chat

def gemini_call(chat,prompt):
    response = chat.send_message(prompt)
    return str(response.text).strip()

def gemini_add_data(query):
    # outputs = []
    pool, connector = connect()
    db_conn = pool.connect()
    chat = gemini_init(key=)

    # UserQuery = ["Shubham Udsaria phone number +918696731092", "Dindayal chajed phone number 6453745232"]
    all_data = fetchData(db_conn)
    all_data['Name'] = list(map(lambda x: x.lower(), all_data['Name']))
    # for query in UserQuery:
    prompt ='''
            Instructions:
            1. Your role is to extract meaningful data from user text input.
            2. Return data of that customer in json format.
            3. values that are not given pass them as None.
            4. Ignore extra data that is not required.
            4. Important Data Points are : Customer Name, Customer Phone Number, Email, address, gstNumber.
            Output Format example: {"Customer_Name":"shubham","Customer_Phone_Number":"8696731092","Email":"sudsaria94@gmail.com","address":"munti kui","gstNumber":"A000001"}
            Input: 
            ''' + query
    str_old = gemini_call(chat,prompt)
    # print("oldddd: ",str_old)
    # print("newwww: ",str_old[7:-3])
    try:
        output = eval(str_old[7:-3])
    except:
        output = eval("{"+str_old[9:-5]+"}")
    if output['Customer_Name']:
        if not output['Customer_Name'].lower() in all_data['Name']:
            if output['Customer_Phone_Number'] == None:
                output['Customer_Phone_Number'] = 'NULL'
            if output['Email'] == None: 
                output['Email'] = 'NULL'
            if output['address'] == None: 
                output['address'] = 'NULL'
            if output['gstNumber'] == None:
                output['gstNumber'] = 'NULL'
            id = all_data['customerId'][-1]+1
            temp_output = addCustomer(
                db_conn,
                id,
                output['Customer_Name'],
                customer_phone_number = output['Customer_Phone_Number'],
                email = output['Email'],
                address = output['address'],
                gstNumber = output['gstNumber'])
            print("Added New Customer to Database: ",temp_output)
            output['customerId'] = id
        # outputs.append(output)
        else:
            print("Customer details already exist.")
            indexcs = all_data["Name"].index(str(output['Customer_Name'].lower()))
            output['customerId'] = all_data['customerId'][indexcs]
    else:
        print("Customer details wrong.")

    # return db_conn, connector

    try:
        disconnect(connector)
    except:
        print("Done")

    return output

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def fetchData(db_conn):
    dataset = db_conn.execute(sqlalchemy.text("CALL GetCustomerDetails();")).fetchall()
    results = {"customerId":[], "Name":[], "Phone_number":[], "emailID":[], "Address":[], "GSTNumber":[]}
    for row in dataset:
        results["customerId"].append(row[0])
        results["Name"].append(row[1])
        results["Phone_number"].append(row[2])
        results["emailID"].append(row[3])
        results["Address"].append(row[4])
        results["GSTNumber"].append(row[5])
    return results

def addCustomer(
        db_conn,
        customer_id,
        customer_name,
        customer_phone_number = 'NULL',
        email = 'NULL',
        address = 'NULL',
        gstNumber = 'NULL'):  
    
    Query = f"CALL addCustomer('{customer_id}','{customer_name}','{customer_phone_number}','{email}','{address}','{gstNumber}')"
    dataset = db_conn.execute(sqlalchemy.text(Query)).fetchall()
    db_conn.commit()
    results = []
    for row in dataset:
        results.append(row[0])
        results.append(row[1])
        results.append(row[2])
        results.append(row[3])
        results.append(row[4])
        results.append(row[5])
    db_conn.close()
    return results

#, addCustomer else if not then add customer details using addCustomer tool by call addCustomer(CustomerID, Name, PhoneNumber, Email, Address, GSTNUmber) and assign new Customer ID that is not already in fetchData.

# gemini_add_data("ankita udsaria phone number 4321244 close")
