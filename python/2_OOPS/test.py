class School:
    # INSTANCE METHOD
    def __init__(self,name,location):
        self.name = name
        self.location = location

    # INSTANCE METHOD
    def students(self, name, roll_no):
        students_info = {"school_name": None, "location": None ,"name": None, "roll_no": None}
        if name and roll_no:
            students_info["school_name"] = self.name
            students_info["location"] = self.location
            students_info["name"] = name
            students_info["roll_no"] = roll_no

    # CLASS METHOD 
    def trustee():
        return ""