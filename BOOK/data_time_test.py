from datetime import datetime
import json

weec_day = datetime.today().isoweekday()
#
#
# print(weec_day)
#
# dic_time = {'1':{
#             "00:00": "morning",
#             "09:00": "day",
#             "19:00": "morning"}
#             }
#
# dic_test = {'135': 'time1', '267': 'time 2'}
# weec_day = '4'
# for key in dic_test.keys():
#     if weec_day in key:
#         print(dic_test[key])
#         break
# else:
#     print(dic_test[list(dic_test.keys())[0]])
#
#
#
# # print(dic_test)

# with open('/home/segiy/PycharmProjects/mpc/time.json', 'r', encoding='utf-8') as file_rusult:
#     data = json.load(file_rusult)


data = {'12345': {
          "00:00": "morning",
          "09:00": "day",
          "19:00": "morning"
        },
  '67': {
        "00:00": "morning",
        "09:00": "day",
        "12:00": "morning"
      }
}
print(data)

with open('/home/segiy/PycharmProjects/mpc/timeqqq.json', 'w', encoding='utf-8') as file_rusult:
    json.dump(data, file_rusult)