"""
Serializes and Deserializes the current object to a file using pickle.
"""
import pickle


class CustomObject:
    """
    Serializes and Deserializes the current object to a file using pickle.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name} \n"
              f"age:{self.age} \n"
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object to a file using pickle.
        """
        try:
            with open(filename, "wb") as f:
                return pickle.dump(self, f)
        except Exception as e:
            print(e)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from the given filename
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except Exception as e:
            print(f"Deserialization failed: {e}")
            return None
