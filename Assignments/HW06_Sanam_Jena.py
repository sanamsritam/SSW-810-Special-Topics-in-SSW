"""
Author: Sanam Jena
CWID:10454295
Date: 16 October 2020
Objective: Lists & DonutQueue program
"""
from typing import Any, Optional, List


class HomeWork06:
    """In this class, we will be creating all the functions required to solve HomeWork06 except
    for DonutQueue
    """

    def __init__(self) -> None:
        return None

    def list_copy(self, l: List[Any]) -> List[Any]:
        """This function takes a list as a parameter and returns a copy of the list

        Args:
            l (List[Any])

        Returns:
            List[Any]
        """
        if not isinstance(l, List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l must be of type List")
        return [i for i in l]

    def list_intersect(self, l1: List[Any], l2: List[Any]) -> List[Any]:
        """This function takes two lists as  parameters and returns a new list with the values that are included in both lists.

        Args:
            l1 (List[Any]): First List
            l2 (List[Any]): Second List

        Returns:
            List[Any]: New List with intersection elements
        """
        if not isinstance(l1, List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l1 must be of type List")
        if not isinstance(l2, List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l2 must be of type List")
        return [i for i in l1 if i in l2]

    def list_difference(self, l1: List[Any], l2: List[Any]) -> List[Any]:
        """This function takes two lists as  parameters and returns a new list with the values that are  in l1, but NOT in l2.

        Args:
            l1 (List[Any]): first list
            l2 (List[Any]): second list

        Returns:
            List[Any]: new list with values that are in l1 but not in l2.
        """
        if not isinstance(l1, List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l1 must be of type List")
        if not isinstance(l2, List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input l2 must be of type List")
        return [i for i in l1 if i not in l2]

    def remove_vowels(self, string: str) -> str:
        """given a string, splits the string on whitespace into words and returns a new string
        that includes only the words that do NOT begin with vowels.

        Args:
            string (str): Input string

        Returns:
            str: result containing words that do not begin with vowels.
        """
        if not isinstance(string, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input string must be of type str")
        return " ".join([words for words in string.split() if words[0] not in "aeiouAEIOU"])

    def check_pwd(self, password: str) -> bool:
        """This function takes a string as a parameter and returns a boolean value.
        check_pwd(password) returns True if all conditions below are satisfied:
        1. The password includes at least two upper case characters
        2. The password includes at least one lower case characters
        3. The password starts with at least one digit

        Args:
            password (str): password of type string

        Returns:
            bool: return true or false based on criteria
        """
        if not isinstance(password, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input password must be of type str")
        return len(password) >= 4 \
            and password[0].isdigit() \
            and len([c for c in password if c.isupper()]) >= 2 \
            and len([c for c in password if c.islower()]) >= 1


class DonutQueue:
    """In this class we will be implementing DonutQueue that tracks customers as they arrive at the donut shop.
    Customers are added to the queue so they can be served in the order they arrived with the exception that priority customers
    are served before non-priority customers.  Priority customers are served in the order they arrive, but before any non-priority customers.
    Completed after discussing with Rajat Verma
    """
    queue: List

    def __init__(self) -> None:
        self.queue: List = []

    def arrive(self, name: str, vip: bool) -> None:
        """In this function, we are adding new people to the que based on priority

        Args:
            name (str): name is the customer's name
            vip (bool): vip is True if the customer is a priority customer or False
        """
        if len(self.queue) > 0:
            if vip:
                for index, person in enumerate(self.queue):
                    if not person[1]:
                        self.queue.insert(index, [name, vip])
                        break
            else:
                self.queue.append([name, vip])
        else:
            self.queue.append([name, vip])

    def next_customer(self) -> Optional[str]:
        """returns the name of the next customer to be served where all priority customers are served in the order they arrived
        before any non-priority customer

        Returns:
            Optional[str]: None if there are no customers waiting
        """
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)[0]

    def waiting(self) -> Optional[str]:
        """returns a comma separated string with the names of the customers waiting in the order they will be served

        Returns:
            Optional[str]: None if there are no customers waiting
        """
        result: str = ""
        for i in self.queue:
            result += i[0]+", "
        return result[:-2]
