import inspect
from inspect import currentframe, getframeinfo

opened_file = []
def read(file):
    for data in opened_file:
        opened_file.remove(data)
    if (file.endswith(".userfiles")):
        opened_file.append(file)
    else:
        raise Exception("Could not read invalid file type.")
    
def get_file():
    if len(opened_file) == 1:
        return opened_file[0]
    else:
        return None

def add_item(id_, item_):
    try:
        frameinfo = getframeinfo(currentframe())
    
        file_ = get_file()
        if not file_:
            raise Exception(f"Traceback: Error on line {frameinfo.lineno} in the function 'add_item'.\nError: No file has been read.")
        id_ = str(id_).lower()
        new_string = ""
        current_cats = get_catagories()
        if f"[{id_}]" in current_cats:
            for cat in current_cats:
                if cat == f"[{id_}]":
                    cat_data = get_category_items(id_)
                    new_string += f"\ncategory:[{id_}]:data:\n"
                    for index, line in enumerate(cat_data):
                        line = str(line).replace("\n", "")
                        new_string += f"{line}\n"
                    new_string += f"{item_}\n"
                else:
                    cat_data = get_category_items(cat.replace("[","").replace("]",""))
                    new_string += f"\ncategory:{cat}:data:\n"
                    for index, line in enumerate(cat_data):
                        new_string += f"{line}\n"
            with open(file_, 'w') as f:
                f.write(new_string)        
            
            
        else:   
            raise Exception(f"{id_} not found.")
        
        
    except Exception as error:
        raise Exception(error)

def remove_item(id_, item_):
    try:
        frameinfo = getframeinfo(currentframe())
    
        file_ = get_file()
        if not file_:
            raise Exception(f"Traceback: Error on line {frameinfo.lineno} in the function 'remove_item'.\nError: No file has been read.")
        id_ = str(id_).lower()
        new_string = ""
        current_cats = get_catagories()
        if f"[{id_}]" in current_cats:
            for cat in current_cats:
                if cat == f"[{id_}]":
                    cat_data = get_category_items(id_)
                    new_string += f"\ncategory:[{id_}]:data:\n"
                    for index, line in enumerate(cat_data):
                        line = str(line).replace("\n", "")
                        if line == item_:
                            pass
                        
                        elif "=" in line:
                            try:
                                log_ = line.split("=")
                                if log_[0].replace(" ", "") == item_:
                                    pass
                                else:
                                    new_string += f"{line}\n"
                            except:
                                pass
                        else:
                            new_string += f"{line}\n"
                        
                else:
                    cat_data = get_category_items(cat.replace("[","").replace("]",""))
                    new_string += f"\ncategory:{cat}:data:\n"
                    for index, line in enumerate(cat_data):
                        new_string += f"{line}\n"
            
            with open(file_, 'w') as f:
                f.write(new_string)        
            
        else:   
            raise Exception(f"{id_} not found.")
        
    except Exception as error:
        raise Exception(error)

def edit_value(id_, item_, to_value_):
    frameinfo = getframeinfo(currentframe())
    
    file_ = get_file()
    if not file_:
        raise Exception(f"Traceback: Error on line {frameinfo.lineno} in the function 'edit_value'.\nError: No file has been read.")
        
    try:
        new_string = ""
        current_cats = get_catagories()
        if f"[{id_}]" in current_cats:
            for cat in current_cats:
                if cat == f"[{id_}]":
                    cat_data = get_category_items(id_)
                    new_string += f"\ncategory:[{id_}]:data:\n"
                    for index, line in enumerate(cat_data):
                        line = str(line).replace("\n", "")
                        if not "=" in line:
                            if item_ == line:
                                new_string += f"{to_value_}\n"
                                
                            else:
                                new_string += f"{line}\n"
                                
                        else:
                            log = line.split("=")
                            if log[0][:-1] == item_ or log[0] == item_:
                                new_string += f"{item_} = {to_value_}\n"
                            else:
                                new_string += f"{line}\n"
                else:
                    cat_data = get_category_items(cat.replace("[","").replace("]",""))
                    new_string += f"\ncategory:{cat}:data:\n"
                    for index, line in enumerate(cat_data):
                        new_string += f"{line}\n"
            
            with open(file_, 'w') as f:
                f.write(new_string)
        
        else:   
            raise Exception(f"{id_} not found.")
        
    except Exception as error:
        raise Exception(error)

def get_catagories():
    cats = []
    try:
        frameinfo = getframeinfo(currentframe())
        file_ = get_file()
        
        if not file_:
            raise Exception(f"Traceback: Error on line {frameinfo.lineno} in the function 'get_catagories'.\nError: No file has been read.")
        
        with open(file_, 'r') as f:
            file_data_ = f.read()
            f.close()
        
        file_data_split_ = file_data_.split("category:")
        for index, data_ in enumerate(file_data_split_):
            log_ = data_.split(":data:")
            cats.append(log_[0].lower())
        
        cats.remove(cats[0])
        return cats
    
    except Exception as error:
        raise Exception(error)

def get_category_items(id_):
    try:
        data_ = []
        id_ = id_.lower()
        frameinfo = getframeinfo(currentframe())
        file_ = get_file()
        
        if not file_:
            raise Exception(f"Traceback: Error on line {frameinfo.lineno} in the function 'get_catagories'.\nError: No file has been read.")
        
        with open(file_, 'r') as f:
            file_data_ = f.read()
            f.close()
        
        file_data_split_ = file_data_.split("category:")
        
        for index, line in enumerate(file_data_split_):
            log_ = line.split(":data:")
            if log_[0] == f"[{id_}]":
                data_ = log_[1].splitlines()

            for i in data_:
                if i == "":
                    data_.remove(i)
        
        return data_
    
    except Exception as error:
       raise Exception(error)
    
def get(id_, item_):
    try:
        id_ = id_.lower()
        frameinfo = getframeinfo(currentframe())
        file_ = get_file()
        if not file_:
            raise Exception(f"Traceback: Error on line {frameinfo.lineno} in the function 'get'.\nError: No file has been read.")
        
        frameinfo = getframeinfo(currentframe())
        file_catagories_ = get_catagories()
        if str(f"[{id_}]") in file_catagories_:
            pass
        else:
            raise Exception(f"Traceback: Error on line {frameinfo.lineno} in the function 'get'.\nError: No ID named \"{id_}\".")
            
        cat_data = get_category_items(id_)
        
        for i in cat_data:
            log = i.split("=")
            if log[0] == item_ or log[0][:-1] == item_:
                if log[1] == " " or log[1] == "":
                    return ""
                else:
                    return log[1]
        
        raise Exception(f"Traceback: Error on line {frameinfo.lineno} in the function 'get'.\nError: Data not available.")
    
    except Exception as error:
        raise Exception(error)

def add_category(name_):
    try:
        frameinfo = getframeinfo(currentframe())
        file_ = get_file()
        if not file_:
            raise Exception(f"Traceback: Error on line {frameinfo.lineno} in the function 'add_category'.\nError: No file has been read.")
        
        with open(file_, 'r') as f:
            data = f.read()
            
        if not f"category:[{name_}]:data:" in data.splitlines():   
            if len(data.splitlines()) == 0:
                with open(file_, 'w') as f:
                    f.write(f"category:[{name_}]:data:")
            else:
                with open(file_, 'a') as f:
                    f.write(f"\n\ncategory:[{name_}]:data:")
                
            return True
        
        else:
            return False
        
    except Exception as error:
        raise Exception(error)


class userfiles():
    read = read
    add_category = add_category
    get = get
    get_category_items = get_category_items
    get_catagories = get_catagories
    remove_item = remove_item
    add_item = add_item
    get_file = get_file
    edit_value = edit_value

