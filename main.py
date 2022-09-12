import json

json_string = '''
   {
         "students":[
             {
               "id" : 1,
               "firstName" : "Amantur",
               "lastName" : "Alikeev",
               "age" : 24,
               "progLanguage" : "Python",
               "contacts" : {
                                "phoneNumber" : 996771124418,
                                "telegram" : "@amanturalikeev",
                                "email" : "amanturalikeev@gmail.com",
                                "github" : "alikeev-amantur"
                             }
             }
        ]
    }
'''

data = json.loads(json_string)
personal_info = json.dumps(data, indent=4)
print(personal_info)
