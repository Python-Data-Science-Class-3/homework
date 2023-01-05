
class Society:
      def __init__(self):

            pass

      def input_date(self):

            self.society_name = input("Please enter your society_name:")
            self.house_no_of_member = int (input("Please enter your  house number: "))
            self.flat = int(input("Please enter your flat number:"))
            self.income = int(input("Please enter your income:"))



      def allocate_flat(self):
            if self.income>=2500:
                self.flat = "A Type"
            elif self.income>=2000 and self.income<=2500:
                self.flat = "B Type"
            elif self.income>=1500 and self.income<=2000:
                self.flat = "C Type"
            else:
                self.flat = "D Type"

      def show_data(self):
                print(f"\nSociety name : {self.society_name}\nHouse no : {self.house_no_of_member}",
                      f"\nIncome of member : {self.income}\nFlat Type to member : {self.flat}\n")

society_1 = Society()

society_1.input_date()

society_1.show_data()


