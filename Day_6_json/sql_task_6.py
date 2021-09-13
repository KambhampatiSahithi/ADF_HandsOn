import re
import logging
from datetime import date
from datetime import datetime
import config as conf
import mysql.connector
import json


def connection_establish():
    """establish connection to database"""
    global mydb
    try:
        mydb = mysql.connector.connect(host=conf.mysql["host"],
                                       user=conf.mysql["user"], password=conf.mysql["password"],
                                       database=conf.mysql["database"])
        logging.info("Connected to database")
    except Exception:
        logging.error("Unable to connect to database")


class AddingUser:
    reason = ""

    def __init__(self):
        self.firstname = None
        self.middle_name = None
        self.lastname = None
        self.dob = None
        self.gender = None
        self.nationality = None
        self.city = None
        self.state = None
        self.pincode = None
        self.qualification = None
        self.salary = None
        self.pan_number = None
        self.failure_check = None
        self.request_id = None

    def get_details(self):
        """get details of users as input"""
        firstname = input("Enter first name")
        self.validate_firstname(firstname)
        middle_name = input("Enter middle name")
        self.validate_mid_name(middle_name)
        lastname = input("Enter last name")
        self.validate_lastname(lastname)
        dob = input("Enter date in date format(YYYY/MM/DD)")
        self.validate_dob(dob)
        gender = input("Enter your gender: ")
        self.validate_gender(gender)
        self.validate_age_gender(dob, gender)
        nationality = input("Enter natinality")
        self.validate_nationality(nationality)
        city = input("Enter city")
        self.validate_city(city)
        state = input("Enter state")
        self.validate_state(state)
        pincode = input("Enter pincode")
        self.validate_pin(pincode)
        qualification = input("Enter qualification")
        self.validate_qualif(qualification)
        salary = input("Enter salary")
        self.validate_Salary(salary)
        pan_number = input("Enter pannumber")
        self.validate_pan(pan_number)
        self.validate_last5_days(pan_number)
        self.validate_sucess_fail()

    def validate_firstname(self, firstname):
        """validate firstname"""
        self.firstname = ""
        res = False
        if firstname == "":
            self.reason += "First name is empty."
        else:
            self.firstname = firstname
            res = True
        logging.info("validated firstname")
        return res

    def validate_lastname(self, lastname):
        """validate lastname"""
        self.lastname = ""
        res = False
        if lastname == "":
            self.reason += "Last name is empty."
        else:
            self.lastname = lastname
            res = True
        logging.info("validated lastname")
        return res

    def validate_mid_name(self, middle_name):
        """validate middle name (optional)"""
        self.middle_name = middle_name
        logging.info("validated middlename")
        return True

    def validate_dob(self, dob):
        """validate daeofbirth (should be in specified format)"""
        res = True
        try:
            format = "%Y/%m/%d"
            self.dob = datetime.strptime(dob, format)
            print("Correct date format")
        except ValueError:
            return "Enter date in format(YYYY/MM/DD)"
            self.reason += "Invalid date of birth"
            res = False
        logging.info("validated dateofbirth format")
        return res

    def validate_gender(self, gender):
        """validate gender('F' or 'M')"""
        self.gender = ""
        res = True
        if gender == "F" or gender == "M":
            self.gender = gender
        else:
            self.reason += "Gender is invalid."
            res = False
        logging.info("validated gender")
        return False

    def validate_nationality(self, nation):
        """nationality should from specified list"""
        self.nationality = ""
        res = True
        if nation == "":
            self.reason += "Nationality is empty."
            res = False
        elif nation not in ("Indian", "American"):
            self.nationality = nation
            self.reason = "Nationality should be Indian or American."
            res = False
        else:
            self.nationality = nation
        logging.info("validated Nationality")
        return res

    def validate_city(self, city):
        """validate city(mandatory)"""
        self.city = ""
        res = True
        if city == "":
            self.reason = "City is Empty."
            res = False
        else:
            self.city = city
        logging.info("validated city")
        return res

    def validate_state(self, st):
        """state should be take from specified listof names"""
        l = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
             "Chhattisgarh", "Karnataka", "Madhya Pradesh",
             "Odisha", "Tamil Nadu", "Telangana", "West Bengal"]
        self.state = " "
        res = True
        if st == "":
            self.reason += "State is empty."
            res = False
        elif st not in l:
            self.state = st
            self.reason += "Entered state is invalid."
            res = False
        else:
            self.state = st
        logging.info("validated firstname")
        return res

    def validate_pin(self, pin):
        """validate pin should have 6 digits"""
        reg = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
        p = re.compile(reg)
        res = True
        if (pin == ''):
            self.reason += "pin is empty"
            res = False
        m = re.match(p, pin)
        if m is None:
            res = False
        else:
            self.pincode = int(pin)
            res = True
        logging.info("validated pinode")
        return res

    def validate_qualif(self, qualification):
        """validate qulaification(should be string)"""
        self.qualification = ""
        res = True
        if qualification.replace(" ", "").isalpha():
            self.qualification = qualification
            res = True
        else:
            self.reason += "qualification empty"
        logging.info("validated qualification")
        return res

    def validate_Salary(self, salary):
        """validate salary between 10000 and 90000"""
        self.salary = 0
        res = True
        if (salary == ""):
            self.reason += "salary is empty"
            res = False
        elif int(salary) < 10000:
            self.reason += "Salary is less than 10000"
            res = False
        elif int(salary) > 90000:
            self.reason += "salary is greater than 90000"
            res = False
        else:
            self.salary = int(salary)
        logging.info("validated salary")
        return res

    def validate_age_gender(self, dob, gender):
        """validate age with gender
        female age should be greater than 18
        male age should be greater than 18"""
        l = list(map(int, dob.split("/")))
        u_dob = date(l[0], l[1], l[2])
        today = date.today()
        age_user = today.year - u_dob.year - ((today.month, today.day) < (u_dob.month, u_dob.day))
        if age_user < 18 and gender == "F":
            self.reason += "Age should be 18 or above for female. "
        if age_user < 21 and gender == "M":
            self.reason += "Age should be 21 or above for male. "
        logging.info("validated age_gender")

    def validate_pan(self, pan):
        """validate pan should have 10 digits
        first5 capital letters and 4 digits
         and last charachter should be capital"""
        logging.info("validated pan")
        reg = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
        p = re.compile(reg)
        if (pan == None):
            self.reason += "Pan is empty"
            return False
        if re.search(p, pan) and len(pan) == 10:
            self.pan_number = pan
            return True
        else:
            self.reason = "pan should be 10 digits"
            return False

    def validate_last5_days(self, pan):
        """validate with pin
        recently received request in last 5 days"""
        res = True
        diff = datetime.now()
        mycursor = mydb.cursor()
        query1 = "select pan_number,request_receive_date from training.request_info"
        mycursor.execute(query1)
        records = mycursor.fetchall()
        for row in records:
            diffdays = (row[1] - datetime.now()).days
            if row[0] == pan and diffdays <= 5:
                self.reason += "Recently request received in last5days"
                res = False
        logging.info("validated recent days users pin")
        return res

    def validate_sucess_fail(self):
        """success or failure based on reason """
        if self.reason == "":
            self.failure_check = "Success"
            self.reason = "-"
        else:
            self.failure_check = "Failure"
        logging.info("checked success or failure for eligibility")

    def push_request_to_db(self):
        """push userdata to table request_info"""
        mycur = mydb.cursor()
        add_user = ("insert into Request_info(first_name, middle_name,last_name,"
                    " dob, gender, nationality, city, state, pincode, "
                    "qualification, salary,pan_number)"
                    " values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data = (self.firstname, self.middle_name, self.lastname,
                self.dob, self.gender, self.nationality,
                self.city, self.state, self.pincode,
                self.qualification, self.salary, self.pan_number)
        mycur.execute(add_user, data)
        self.request_id = mycur.lastrowid
        mydb.commit()
        logging.info("pushed request data to request table sucessfuly")

    def push_response_to_db(self):
        """push response to the table response_info"""
        mycursor = mydb.cursor()
        add_response = ("Insert into response_info(request_id, response, reason)"
                        "Values(%s, %s, %s)")
        data_response = (self.request_id, self.failure_check, self.reason)
        mycursor.execute(add_response, data_response)

        mydb.commit()
        logging.info("Pushed response data to response table sucessfully")

    def convert_to_json(self):
        """converted into json format and
        store into json_response.txt file"""
        t = {"Request_id": self.request_id, "Response": self.failure_check,
             "Reason": self.reason}
        with open("json_respose.txt", 'a', encoding="UTF-8") as filehandle:
            filehandle.write(json.dumps(t))
            filehandle.write("\n")
            filehandle.close()
        print(json.dumps(t))
        logging.info("Converted response to JSON format and store it in textfile")


if __name__ == '__main__':
    logging.basicConfig(filename="logger.txt",
                        filemode="a",
                        format='%(asctime)s %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.info("Started execution")
    connection_establish()
    user = AddingUser()
    user.get_details()
    user.push_request_to_db()
    user.push_response_to_db()
    user.convert_to_json()
