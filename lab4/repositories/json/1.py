import json

file = open("sample_data.json")

data_s = file.read()

datas = json.loads(data_s)

formatted_output = ("Interface Status\n"
                    "================================================================================\n"
                    "DN                                                 Description           Speed    MTU  \n"
                    "-------------------------------------------------- --------------------  ------  ------")
for i in datas['imdata']:
    attributes = i['l1PhysIf']['attributes']
    formatted_output += f"\n{attributes['dn']:50} {attributes['descr']:20} {attributes['speed']:8} {attributes['mtu']:6}" 
print(formatted_output)