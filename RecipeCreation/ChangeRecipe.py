import xml.etree.ElementTree as ET

class ChangeRecipe: 
    def __init__(self,new_icp_c1, new_icp_c2, new_table_c1, new_table_c2, path_old_recipe, path_new_recipe):
        self.new_icp_c1 = new_icp_c1
        self.new_icp_c2 = new_icp_c2
        self.new_table_c1 = new_table_c1
        self.new_table_c2 = new_table_c2
        self.path_new_recipe = path_new_recipe

        self.tree = ET.parse(path_old_recipe)
        self.root = self.tree.getroot()

    # Change ProcessStep step in the bosch recipe
    def ChangePreProcess(self):
    # Search for id: 3 in recipestep
        for rec in self.root.iter("recipestep"):
            if rec.get("name") == "Stab and strike":

                # Search for id: RF.Amu1 and RF.Amu2 in devmodifier
                for dev in rec.iter("devmodifier"): 
                    if dev.get("id") == "RF.Amu1":

                        # Search for keyframe: 0 in keyframesetpoint
                        for kfsp in dev.iter("keyframesetpoint"):
                            if kfsp.get("keyframe") == "0":

                                # Search for id: c1 and c2 in setpoiny
                                for sp in kfsp.iter("setpoint"):
                                    if sp.get("id") == "c1":
                                        sp.set("value", str(self.new_table_c1)) # Change string value to new value

                                    if sp.get("id") == "c2":
                                        sp.set("value", str(self.new_table_c2)) # Change string value to new value

                    if dev.get("id") == "RF.Amu2":
                        
                        # Search for keyframe: 0 in keyframesetpoint
                        for kfsp in dev.iter("keyframesetpoint"):
                            if kfsp.get("keyframe") == "0": 

                                # Search for id: c1 and c2 in setpoiny
                                for sp in kfsp.iter("setpoint"):
                                    if sp.get("id") == "c1":
                                        sp.set("value", str(self.new_icp_c1)) # Change string value to new value

                                    if sp.get("id") == "c2":
                                        sp.set("value", str(self.new_icp_c2)) # Change string value to new value

    def ChangeBoschLoop(self):
        for rec in self.root.iter("recipestep"):
            if rec.get("name") == "Bosch loop":

                # Search for id: RF.Amu1 and RF.Amu2 in devmodifier
                for dev in rec.iter("devmodifier"): 
                    if dev.get("id") == "RF.Amu1":

                        # Search for keyframe: 0 in keyframesetpoint
                        for kfsp in dev.iter("keyframesetpoint"):
                            if kfsp.get("keyframe") == "0":

                                # Search for id: c1 and c2 in setpoiny
                                for sp in kfsp.iter("setpoint"):
                                    if sp.get("id") == "c1":
                                        sp.set("value", str(self.new_table_c1)) # Change string value to new value

                                    if sp.get("id") == "c2":
                                        sp.set("value", str(self.new_table_c2)) # Change string value to new value

                    if dev.get("id") == "RF.Amu2":
                        
                        # Search for keyframe: 0 in keyframesetpoint
                        for kfsp in dev.iter("keyframesetpoint"):
                            if kfsp.get("keyframe") == "0": 

                                # Search for id: c1 and c2 in setpoiny
                                for sp in kfsp.iter("setpoint"):
                                    if sp.get("id") == "c1":
                                        sp.set("value", str(self.new_icp_c1)) # Change string value to new value

                                    if sp.get("id") == "c2":
                                        sp.set("value", str(self.new_icp_c2)) # Change string value to new value


    def save(self):
        self.tree.write(self.path_new_recipe, encoding="utf-8", xml_declaration=True) 
        print(f'New recipe saved in directory: {self.path_new_recipe}')