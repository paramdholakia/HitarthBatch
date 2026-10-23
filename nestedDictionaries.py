""" 
{   
    key : {
            key : value,
            key : value,
            key : value,
            
        },
    key : {
            key : value,
            key : value,
            key : value,
            
        },
    key : {
            key : value,
            key : value,
            key : value,
            
        },
    key : {
            key : value,
            key : value,
            key : value,
            
        },
}
""" 
# students = {
#     1: {
#         "name": "Raj",
#         "age": 20,
#         "marks": 85
#     },

#     2: {
#         "name": "Ankita",
#         "age": 21,
#         "marks": 92
#     }
# }
""" 
students[1]["marks"]
         ↓      ↓
        outer   inner
         key     key
         
print(students.get(2).get("age"))
                ↓      ↓
              outer   inner
               key     key      
"""






# -----------------------------------------------------

students = {
    1: {
        "name": "Raj",
        "age": 20,
        "marks": 85
    },

    2: {
        "name": "Ankita",
        "age": 21,
        "marks": 92
    }
}

# students[3] = { 
#                "name": "Rohit",
#                "age": 22,
#                 "marks": 88,
#                 "phone": 9876543210
#                }

# students[1]["phone"] = 1234567890
# print(students)