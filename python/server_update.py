def update_server_conf(file_path, key, value):

    key_value = f"{key}={value}"

    with open(file_path, "r") as file:
         all_lines = file.readlines()

    with open(file_path, "w") as file:
         for line in all_lines:
              if line.startswith(f"{key}="):
                  file.write(f"{key_value}\n")
                #    file.write(key + "=" + value + "\n")
              else:
                   file.write(line)

# if not updated:
#     file.write(f"{key_value}\n")

update_server_conf("server.conf", "MAX_CONNECTION", "800")