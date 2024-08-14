def updateconf(path, key, value):
     key_value = f"{key}={value}"

     with open(path, "r") as file:
          lines_list = file.readlines()

     with open(path, "w") as file:
          for line in lines_list:
               
               if line.startswith(f"{key}="):
                    file.write(f"{key_value}\n")
                
               else:
                   file.write(line)


updateconf("server.conf", "MAX_CONNECTION", "1066600")












# def update_server_conf(file_path, key, value):

#     key_value = f"{key}={value}"

#     with open(file_path, "r") as file:
#          all_lines = file.readlines()

#     with open(file_path, "w") as file:
#          for line in all_lines:
#               if line.startswith(f"{key}="):
#                   file.write(f"{key_value}\n")
#                 #    file.write(key + "=" + value + "\n")
#               else:
#                    file.write(line)

# # if not updated:
# #     file.write(f"{key_value}\n")

