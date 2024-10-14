class AdAnalytic:
    
    date = ""
    tag = ""
    sub_type = ""
    type = ""
    rating  = ""
    cost = 0
    predicted_ctr = 0
     
    def __init__(self) -> None:
        self.unique_id = str(id(self))
    
    def __str__(self) -> str:
        return_str =  ','.join([self.unique_id, 
                                self.date, 
                                self.tag, 
                                self.sub_type, 
                                self.type, 
                                self.rating, 
                                str(self.cost), 
                                str(self.predicted_ctr)])
        
        return return_str
    

obj1 = AdAnalytic()

obj1.date = "NewDate"
obj1.tag = "NoTag"
obj1.sub_type = "NoSubType"
obj1.type = "NoType"
obj1.rating  = "NoRating"
obj1.cost = 0
obj1.predicted_ctr = 0

print(obj1.__str__())

