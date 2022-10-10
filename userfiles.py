import inspect
from inspect import currentframe, getframeinfo
import os


class File:
    opened_file = []


class userfiles:
    @staticmethod
    def read(file: str):
        if not os.path.exists(file):
            frameinfo = getframeinfo(currentframe())
            raise Exception(f"Error on line {frameinfo.lineno - 1}\n{file} does not exist.")

        if not file.lower().endswith(".userfiles"):
            frameinfo = getframeinfo(currentframe())
            raise Exception(f"Error on line {frameinfo.lineno - 1}\nCannot read invalid file type\n{file}.")
        
        File.opened_file.clear()
        File.opened_file.insert(0, file)

    @staticmethod
    def get_file():
        if File.opened_file:
            return File.opened_file[0]
        
        return None
    
    @staticmethod
    def add_item(cat, item, value):
        categories = userfiles.get_categories()
        if cat not in categories:
            frameinfo = getframeinfo(currentframe())
            raise Exception(f"Error on line {frameinfo.lineno - 1}\nCategory '{cat}' not available.")

        data = []
        
        for category in categories:
            if category != cat:
                data.append(f'category:[{category}]:data:')
                data.append("\n".join(userfiles.get_category_items(category)))

            else:
                data.append(f'category:[{cat}]:data:')
                category_data = userfiles.get_category_items(category)
                data.append("\n".join(userfiles.get_category_items(category)))
                data.append(f"{item} = {value}")
        
        new_data = "\n".join(data)
        with open(userfiles.get_file(), 'w') as file:
            file.write(new_data)
            file.close()
            
    @staticmethod
    def remove_item(cat, item):
        categories = userfiles.get_categories()
        if cat not in categories:
            frameinfo = getframeinfo(currentframe())
            raise Exception(f"Error on line {frameinfo.lineno - 1}\nCategory '{cat}' not available.")

        data = []
        
        for category in categories:
            if category != cat:
                data.append(f'category:[{category}]:data:')
                data.append("\n".join(userfiles.get_category_items(category)))
            
            else:
                data.append(f'category:[{category}]:data:')
                cat_data = userfiles.get_category_items(category)
                for data_ in cat_data:
                    try:
                        if data_.split('=')[0].strip() == item:
                            pass
                        else:
                            data.append(f'{data_}')
                    except:
                        pass
                
        new_data = "\n".join(data)
        
        with open(userfiles.get_file(), 'w') as file:
            file.write(new_data)
            file.close()
                    
    
    @staticmethod
    def edit_item(cat, item, value):
        categories = userfiles.get_categories()
        if cat not in categories:
            frameinfo = getframeinfo(currentframe())
            raise Exception(f"Error on line {frameinfo.lineno - 1}\nCategory '{cat}' not available.")

        data = []
        
        for category in categories:
            if category != cat:
                data.append(f'category:[{category}]:data:')
                data.append("\n".join(userfiles.get_category_items(category)))
            
            else:
                data.append(f'category:[{category}]:data:')
                cat_data = userfiles.get_category_items(category)
                for data_ in cat_data:
                    try:
                        if data_.split('=')[0].strip() == item:
                            data.append(f'{item} = {value}')
                        else:
                            data.append(f'{data_}')
                    except:
                        pass
                
        new_data = "\n".join(data)
        
        with open(userfiles.get_file(), 'w') as file:
            file.write(new_data)
            file.close()
    
    @staticmethod
    def get_categories():
        cats = []
        file_data = open(userfiles.get_file(), 'r').read()
        for index, data in enumerate(file_data.split('category:')):
            log = data.split(":data:")
            if not log[0] == "":
                cats.append(log[0].replace("[", "").replace("]", ""))
                
        return cats
    
    @staticmethod
    def get_category_items(cat):
        data = []
        categories = userfiles.get_categories()
        if cat not in categories:
            frameinfo = getframeinfo(currentframe())
            raise Exception(f"Error on line {frameinfo.lineno - 1}\nCategory '{cat}' not available.")

        file_data = open(userfiles.get_file(), 'r').read()
        log = file_data.split(":data:")
        for line in log[1].splitlines():
            if line and line != "":
                data.append(line)
        
        return data
    
    @staticmethod
    def get(cat, item):
        category_data = userfiles.get_category_items(cat)
        for data in category_data:
            try:
                if data.split("=")[0].strip() == item:
                    return data.split("=")[1].strip()
                
            except:
                pass
        
        frameinfo = getframeinfo(currentframe())
        raise Exception(f"Error on line {frameinfo.lineno - 7}\nCategory '[{cat}] {item}' is not available.")
    
    @staticmethod
    def add_category(cat):
        with open(userfiles.get_file(), 'a') as file:
            file.write(f"\ncategory:[{str(cat)}]:data:\n")
            file.close()
    
    def remove_category(cat):
        categories = userfiles.get_categories()
        if cat not in categories:
            frameinfo = getframeinfo(currentframe())
            raise Exception(f"Error on line {frameinfo.lineno - 1}\nCategory '{cat}' not available.")

        data = []
        
        for category in categories:
            if category != cat:
                data.append(f'category:[{category}]:data:')
                data.append("\n".join(userfiles.get_category_items(category)))

        new_data = "\n".join(data)
        
        with open(userfiles.get_file(), 'w') as file:
            file.write(new_data)
            file.close()
