#!/usr/bin/env python

import re,sys

# The "database"
data = {}
# The "session"
session = {}

# Internal functions of the "server"-side application
def error_state():
    return "Something wrong", ["get", "default", None]

# The "server"-side application handlers
def default_get_handler(args):
    rep = "What would you like to do?"
    rep += "\n1 - Quit" + "\n2 - Upload File"
    links = {"1" : ["post", "execution", None], "2" : ["get", "file_form", None]}
    return rep, links

def quit_handler(args):
    for filename in data:
        with open(filename,"w") as f:
            for row in data[filename]:
                f.write(','.join(row))
                f.write("\n")

    sys.exit("Goodbye m'lord!")

def add_get_handler(args):
    rep = "Enter Name, Phone, Marks1, Marks2, Marks3, Marks4: "
    links = ["post", "add"]
    return rep, links

def add_post_handler(args):
    def add_to_data(new_data):
        for key in data:
            data[key].append(new_data[0].split(','))

    if args == None:
        return error_state()
    new_data = args
    try:
        add_to_data(new_data)
    except:
        return error_state()

    return main_get_handler([session['filename']]) 

def del_get_handler(args):
    rep = "Enter serial number of record to be deleted"
    links = ["post", "del"]
    return rep, links

def del_post_handler(args):
    def delete_record(key):
        for filename in data:
            data[filename].remove(data[filename][key])

    if args==None:
        return error_state()
    key = int(args[0])-1
    try:
        delete_record(key) 
    except:
        return error_state()

    return main_get_handler([session['filename']])

def upload_get_handler(args):
    return "Name of file to upload?", ["post", "file"]

def upload_post_handler(args):
    def create_data(filename):
        if filename in data:
            return
        with open(filename) as f:
            lines = f.readlines()
            student_list = filter(lambda z: z!= [], \
                    map(lambda y: filter(lambda x:x!='',y), \
                    map(lambda x: re.split("[^a-zA-Z0-9.]+", x), \
                    lines)))
        data[filename] = student_list
        session['filename'] = filename

    if args == None:
        return error_state()

    filename = args[0]
    try:
        create_data(filename)
    except:
        return error_state()

    return main_get_handler([filename])

def main_get_handler(args):

    filename = args[0]
    
    rep = "\nWhat would you like to do next?"
    rep += "\n1 - Quit" + "\n2 - Upload file"
    rep += "\n3 - See students"
    rep += "\n4 - Add Student"
    rep += "\n5 - Remove Student"
    links = {"1" : ["post", "execution", None],
             "2" : ["get", "file_form", None],
             "3" : ["get", "student", [filename, 0]],
             "4" : ["get", "add_form", None],
             "5" : ["get", "del_form", None] }

    return rep, links

def student_get_handler(args):
    def get_student(filename, student_index):
        if student_index < len(data[filename]):
            return data[filename][student_index]
        else:
            return "no more students"

    filename = args[0]; student_index = args[1]
    if student_index > len(data[filename]):
        return main_get_handler([filename])

    student_info = get_student(filename, student_index)
    rep = '\n#{0}: {1}'.format(student_index+1, student_info)
    rep += "\n\nWhat would you like to do next?"
    rep += "\n1 - Quit" + "\n2 - Upload file"
    rep += "\n3 - See next student"
    links = {"1" : ["post", "execution", None],
             "2" : ["get", "file_form", None],
             "3" : ["get", "student", [filename, student_index+1]]}

    return rep, links

# Handler registration
handlers = {"post_execution" : quit_handler,
            "get_default" : default_get_handler,
            "get_file_form" : upload_get_handler,
            "post_file" : upload_post_handler,
            "get_student" : student_get_handler,
            "get_main" : main_get_handler,
            "get_add_form" : add_get_handler,
            "post_add" : add_post_handler,
            "get_del_form" : del_get_handler,
            "post_del" : del_post_handler }

# The "server" core
def handle_request(verb, uri, args):
    def handler_key(verb, uri):
        return verb + "_" + uri

    if handler_key(verb, uri) in handlers:
        return handlers[handler_key(verb, uri)](args)
    else:
        return handlers[handler_key("get", "default")](args)

# A very simple client "browser"
def render_and_get_input(state_representation, links):
    print state_representation
    sys.stdout.flush()
    if type(links) is dict: #many possible next states
        input = sys.stdin.readline().strip()
        if input in links:
            return links[input]
        else:
            return ["get", "default", None]
    elif type(links) is list: #only one possible next state
        if links[0] == "post": #get "form" data
            input = sys.stdin.readline().strip()
            links.append([input])
            return links
        else:
            return ["get", "default", None]

request = ["get", "default", None]
while True:
    # "server"-side computation
    state_representation, links = handle_request(*request)
    # "client"-side computation
    request = render_and_get_input(state_representation, links)
