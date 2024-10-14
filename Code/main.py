class AdAnalytic:
    def __init__(self, date, tag, sub_type, type, rating, cost, predicted_ctr):
        self.date = date
        self.tag = tag
        self.sub_type = sub_type
        self.type = type
        self.rating = rating
        self.cost = cost
        self.predicted_ctr = predicted_ctr
        self.unique_id = id(self)

    def __str__(self) -> str:
        return_str =  ','.join([str(self.unique_id), 
                                self.date, 
                                self.tag, 
                                self.sub_type, 
                                self.type, 
                                str(self.rating), 
                                str(self.cost), 
                                str(self.predicted_ctr)])
        
        return return_str