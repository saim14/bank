import credit_card
#Inheritance
class PredatoryCreditCard(credit_card.CreditCard):
  #Add a new field to subclass
  def __init__(self, bank, client, account, limit, apr):
    super().__init__(bank, client, account, limit)
    self._apr = apr
    #you can add more field
  
  #Override the function charge(price)
  def charge(self, price):
    success = super().charge(price):
 
  #you can create new method here, no special syntax is needed
  def subliminary(self,sub_name):
    self.sub_name = sub_name
    return f"{self.sub_name} is added as Subliminary"

