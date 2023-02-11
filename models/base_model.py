#!/usr/bin/python3                                                        
                                                                          
import uuid                                                               
from datetime import datetime                                             
                                                                          
class BaseModel:                                                          
    """ a class that defines attribute id"""                              
                                                                          
    def __init__(self):                                                   
        """constructor for class attribute id created_at, updated_at and m
ethod"""                                                                  
        self.id = str(uuid.uuid4())                                       
        self.created_at = datetime.now()                                  
        self.updated_at = datetime.now()                                  
                                                                          
    def __str__(self):                                                    
        """returns string representation of aclass"""                     
                                                                          
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__} "
)                                                                         
                                                                          
    def save(self):                                                       
        """updates the updated attributes"""                              
                                                                          
        self.update_at = datetime.now()                                   
                                                                          
    def to_dict(self):                                                    
        """returns dictionary representationof an instance"""             
                                                                          
        my_dict = self.__dict__.copy()                                    
        my_dict["__class__"] : self.__class__.__name__,                   
        my_dict["updated_at"] : self.updated_at.isoformat(),              
        my_dict["created_at"] : self.created_at.isoformat()               
        return my_dict 
