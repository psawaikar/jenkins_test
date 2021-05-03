"""
This script is used to trigger AM Server builds.
It automatically generates build Tag, and pushes it to github repo
It stores the latest build_number in TAG file and appends TAG_HISTORY
"""

import os
from datetime import datetime

#Component Name in Git Tag
AM_SERVER_TXT = "amserver"
AM_SERVER_TAG_FILE = "TAG"

today = datetime.now()
dt = today.strftime("%y.%m.%d")

def exit_on_error():
      print("Some error occured. Build NOT triggered. Exiting...")

def write_to_tag_file():

      git_tag = None
      build_num = None

      if not os.path.exists(AM_SERVER_TAG_FILE):
            print("TAG file doesn't exist. Creating it")
            #First time Tag file is created
            num = '01'
            build_num = dt + '.' + num
            git_tag = AM_SERVER_TXT + '-' + build_num

      else:
            #Tag file exists
            with open(AM_SERVER_TAG_FILE) as f:
                  existing_build_num = f.read()
            print("existing_build_num = {}".format(existing_build_num))

            e_dt = existing_build_num.rsplit('.',1)[0]
            e_no = existing_build_num.rsplit('.',1)[1]

            if dt == e_dt:
                  print("dates are same. Incrementing number by 1")
                  e_no = int(e_no) + 1
                  num = str(e_no).zfill(2)
                  #print(num)

                  build_num = dt + '.' + num
                  git_tag = AM_SERVER_TXT + '-' + build_num

            else:
                  print("dates are not same. Updating build number for current date")
                  num = '01'
                  build_num = dt + '.' + num
                  git_tag = AM_SERVER_TXT + '-' + build_num


      print("Build Number = {}".format(build_num))
      print("Git_Tag = {}".format(git_tag))

      with open(AM_SERVER_TAG_FILE, 'w') as f:
            f.write(build_num)

      return git_tag

git_tag = write_to_tag_file()
#print("Outside function = {}".format(git_tag))


cmd_files_add_to_git = "git add tmp_build.py"
print(cmd_files_add_to_git)
error_code = os.system(cmd_files_add_to_git)
print("Error Code = {}".format(error_code))
if error_code != 0:
      exit_on_error()

cmd_commit = "git commit -m \"Updating tmp_build file\" "
print(cmd_commit)
error_code = os.system(cmd_commit)
print("Error Code = {}".format(error_code))
if error_code != 0:
      exit_on_error()


cmd_push = "git push origin"
print(cmd_push)
error_code = os.system(cmd_push)
print("Error Code = {}".format(error_code))
if error_code != 0:
      exit_on_error()


cmd_git_tag = "git tag -a " + "\"" + git_tag + "\"   -m \"Build for Tag " + git_tag + "\""
print(cmd_git_tag)
error_code = os.system(cmd_git_tag)
print("Error Code = {}".format(error_code))
if error_code != 0:
      exit_on_error()

cmd_git_tag_push = "git push origin " + git_tag
print(cmd_git_tag_push)
error_code = os.system(cmd_git_tag_push)
print("Error Code = {}".format(error_code))
if error_code != 0:
      exit_on_error()









