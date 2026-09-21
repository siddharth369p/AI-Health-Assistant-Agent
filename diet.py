#BMI tells us a person's weight relative to their height.

def bmi_calculator(weight,height):
   bmi =weight/((height/100)**2)
   return round(bmi,2)
 
def bmr_calculator(gender,age,weight,height):
   if gender=="Male":
       bmr=(10*weight)+(6.25*height)-(5*age)+5
       return bmr
     
   elif gender=="Female":
       bmr=(10*weight)+(6.25*height)-(5*age)-161
       return bmr
   else:
      raise ValueError(f"Invalid gender: {gender}")
   
#TDEE — Total Daily Energy Expenditure
#TDEE estimates your total daily energy expenditure, including activity.

     
def tdee_calculator(bmr,activity):
      activity_factor={"Sedentary":1.20,
                       "Lightly_Active":1.375,
                       "Moderately_Active":1.5,
                       "Very_Active":1.725,
                       "Extra_Active":1.90
                      }
      tdee=bmr*activity_factor[activity]
      return round(tdee,2)
    
# This is where your application estimates a daily calorie target based on the user's goal.
# A simple educational model can use:

def calorie_target(tdee,aim):
   if aim=="Weight maintain":
      calorie=tdee
   elif aim=="Weight loss":
     calorie=tdee-400
   elif aim=="Weight gain":
      calorie=tdee+300
   return round(calorie,2)


# print(f"bmi is :{bmi_calculator(74,166)}")
# bmr=bmr_calculator("male",24,74,166)
# tdee=tdee_calculator(bmr,"Extra_Active")
# print("killo calorie you need is:",calorie_target(tdee,"weight gain"))


   
    

   

