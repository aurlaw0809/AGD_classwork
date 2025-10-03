#import warnings

def calc_grade(p_score):#: int) -> str:
    grade = ""
    
    if isinstance(p_score, str):
        #warnings.warn("Score cannot be string. Try entering again.", UserWarning)
        #return None
        raise TypeError('no strings')
    elif isinstance(p_score, float):
        #warnings.warn("Score cannot be float. Try entering again.", UserWarning)
        #return None
        raise TypeError('no floats')
    elif p_score < 0 or p_score > 350:
        #warnings.warn("Score must be between 0 and 350 inclusive. Try entering again.", UserWarning)
        #return None
        raise ValueError('out of range')
    elif p_score >= 264:
        grade = "A*"
    elif p_score >= 229:
        grade = "A"
    elif p_score >= 189:
        grade = "B"
    elif p_score >= 150:
        grade = "C"
    elif p_score >= 111:
        grade = "D"
    elif p_score >= 72:
        grade = "E"
    elif p_score >= 0:
        grade = "U"
    else:
        return None
        
    return grade

if __name__  == '__main__':
    print(calc_grade(234))

#score = "a"
#score = input("Enter score: ")
#valid = False

#while not valid:
 #   if score.isdigit():
  #      if int(score) >= 0 and int(score) <= 350:
   #         valid = True
    #if not valid:
     #   print("Invalid, please enter a valid score")
      #  print("")
       # score = input("Enter score: ")
          
#print(f"Your grade is {calc_grade(int(score))}")
