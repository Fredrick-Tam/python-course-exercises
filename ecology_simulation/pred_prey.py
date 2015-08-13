########################################
# Fredrick Kofi Tam                   ##
# UNI: fkt2105                        ##
# Question 1                          ##
########################################

### Now we construct the functions the model the relationship for QUESTION 1

### This function gives you the prey population after one period
def prey_next( pred_now, prey_now, a, b):
    'Returns the prey population after 1 period'
    return  prey_now * (1 + a - b * pred_now)



### This function gives you the predator population after one period
def pred_next( pred_now, prey_now, c, d):
    'Returns the predator population after one period'
    return  pred_now * (1 - c + d * prey_now)

### This function gives you the prey population after one period
def prey_future(pred_now, prey_now, a, b, c,d, n):
    for m in range(0,n):
        prey_now = prey_now * (1 + a - b * pred_now)
        pred_now = pred_now * (1 - c + d * prey_now)
    return prey_now
        
### This function gives you the predator population after one period
def pred_future(pred_now, prey_now, a, b,c, d, n):
    ' Returns the predator population after n periods into the future '
    for m in range(0,n):
        pred_now =  pred_now * (1 - c + d* prey_now)
        prey_now =  prey_now * (1 + a - b * pred_now)
    return pred_now 
