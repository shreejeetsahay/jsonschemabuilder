import json

DIFF_TYPES = {"1": ["integer", "null"], "2": ["number", "null"], "3": ["string", "null"], "4": ["object", "null"], "5": ["array", "null"], "6": ["boolean", "null"], "7": ["string", "null"]}
class SchemaBuild:
    def __init__(self):
        self.properties = {}
    
    def makeSchema(self, properties1):
        while True:
            name = input("Enter the name of the property: ")
            type1 = input(f"Enter the type of the property for {name}: \n1: Integer\n2: Number\n3: String\n4: Object\n5: Array\n6: Boolean\n7: Date-Time\n")
            properties1[name] = {"type": DIFF_TYPES[type1]}
            if type1 == "7":
                properties1[name]["format"] = "date-time"
            elif type1 == "4":
                print(f"\n\nGetting into the schema build for {name}...")
                properties1[name]["properties"] = {}
                properties1[name]["properties"] = self.makeSchema(properties1[name]["properties"])
                print(f"\n\nEnding the schema build for {name}...")
            elif type1 == "5":
                type2 = input(f"Enter the type of the items for {name}: \n1: Integer\n2: Number\n3: String\n4: Object\n6: Boolean\n7: Date-Time")
                properties1[name]["items"] = {"type": DIFF_TYPES[type2]}
                if type2 == "7":
                    properties1[name]["items"]["format"] = "date-time"
                elif type2 == "4":
                    print(f"\n\nGetting into the schema build for object type items in array: {name}...")
                    properties1[name]["items"]["properties"] = {}
                    properties1[name]["items"]["properties"] = self.makeSchema(properties1[name]["items"]["properties"])
                    print(f"\n\nEnding the schema build for object type items in array: {name}...")
            choice = input("\n\nDo you wanna enter further properties? ")
            if choice == 'y' or choice == 'Y' or choice=="1":
                continue
            else:
                break

        return properties1

    def consolidate(self, f):
        self.properties = self.makeSchema(self.properties)
        schema = {"type": "object", "properties": self.properties}
        json.dump(schema, f, indent = 3)

obj = SchemaBuild()
filename = input("Enter the name of the file: ")
with open(filename, "w+") as f:
    obj.consolidate(f)



