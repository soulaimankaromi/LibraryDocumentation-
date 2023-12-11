# LibraryDocumentation-
The Library Documentation System is a Python program designed to manage and organize information about documentaries and their respective copies in a library. The system consists of two classes: Documentaire and Exemplaire. Here's an overview of each class:

Documentaire Class:
Attributes:

_count: A class variable to keep track of the total number of documentaries. _code: An automatically assigned unique code for each documentary. _titre: The title of the documentary. _date: The date of the documentary. Methods:

init(self, titre, date): Initializes a new documentary with a title and date. Getcode(self): Retrieves the unique code of the documentary. setcode(self, code): Sets a new code for the documentary. Gettitre(self): Retrieves the title of the documentary. settitre(self, titre): Sets a new title for the documentary. Getdate(self): Retrieves the date of the documentary. setdate(self, date): Sets a new date for the documentary. Getcount(self): Retrieves the total count of documentaries. ToString(self): Generates a string representation of the documentary. Equals(self, doc1): Checks if two documentaries are equal based on their codes.
