def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return[f"Hello, my name is {name}." for name in names]


def assign_rooms(names):
    new_names = []
    index = 1
    for name in names:
        new_names.append(f"Hello, {name}! You'll be assigned to room {index}!")
        index +=1
    return new_names
    
   


def printer(names):
    # for name in names:
    for name in batch_badge_creator(names):
        print(name)
       
    for name in assign_rooms(names):
        print(name)   
      
