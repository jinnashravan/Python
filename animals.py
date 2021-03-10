class AnimalsClass:
    
    def dog(self):
        dog=2
        return dog
    
    def cat(self):
        cat=3
        return cat
    
    def mouse(self):
        mouse=4
        return mouse
        
    def run(self):
        total=self.dog()+self.cat()+self.mouse()
        print(f"dog={self.dog()},cat={self.cat()},mouse={self.mouse()},total={total}")

AnimalsClass().run()
