#BMI tells us a person's weight relative to their height.

def bmi_calculator(weigth,height):
   bmi =weight/(height**2)
   return bmi
 
def bmr_calculator(gender,age,weight,height):
   if gender=="male":
       bmr=(10*weight)+(6.25*height)-(5*age)+5
       return bmr
     
   elif gender=="female":
       bmr=(10*weight)+(6.25*height)-(5*age)-161
       return bmr

#TDEE — Total Daily Energy Expenditure
#TDEE estimates your total daily energy expenditure, including activity.

     
def tdee_calculator(bmr,activity):
      activity_factor={"Sedantary":1.20,
                       "Lightly_Active":1.375,
                       "Moderately_Active":1.5,
                       "Very_Active":1.725,
                       "Extra_Active":1.90
                      }
      tdee=bmr*activity_factor[activity]
      return tdee
    
# This is where your application estimates a daily calorie target based on the user's goal.
# A simple educational model can use:

def calorie_target(tdee,aim):
   if aim=="maintain":
      calorie=tdee
   elif aim=="loss":
     calorie==tdee-400
   elif aim=="gain":
      calorie=tdee+300
   return calorie
 

     
    

   

