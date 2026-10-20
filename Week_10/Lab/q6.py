def extract_functions(python_filename, output_filename):
    with open(python_filename, "r") as python_file:
        def_list = []
        docstring_list = []
        doc_string_bool = False
        doc_string_counter = 0
        for line in python_file:
            if doc_string_counter == 2:
                doc_string_bool = False
                doc_string_counter = 0

            if "def" in line:
                def_list.append(line.strip().strip("def :"))
                docstring_list.append([])
                doc_string_bool = False
                doc_string_counter = 0

            if '"""' in line:
                doc_string_bool = True
                doc_string_counter+=1

            doc_string_count = line.count('"""')
            if doc_string_bool:
                if doc_string_count == 2:
                    docstring_list[-1].append(line.strip().strip('"""'))
                    doc_string_bool = False
                else:
                    if line.strip().strip('"""') != "":
                        docstring_list[-1].append(line.strip().strip('"""'))
            
        for i in range(len(def_list)):
            print(f"{i+1}. {def_list[i]}")
            for string in docstring_list[i]:
                print(f"    {string}")
            print()

extract_functions("python_script.py", "q6.txt")