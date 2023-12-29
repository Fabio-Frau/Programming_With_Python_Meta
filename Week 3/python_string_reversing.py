#slice function

trial = "reversal"
new_trial = trial[::-1]

print(trial)
print(new_trial)

#recursion

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
new_trial_recursion = string_reverse(trial)
print(new_trial_recursion)
